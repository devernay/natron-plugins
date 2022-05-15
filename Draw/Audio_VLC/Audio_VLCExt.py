import os
from sys import platform
import subprocess
from NatronEngine import *

# Try to import GUI stuff, as VLC will be unnecessary in command-line mode.
try:
    from NatronGui import *
except ImportError:
    pass


def get_command(sound_file, fps, range_start, range_end):
    start_frame = range_start / fps
    end_frame = (range_end - 1) / fps
    # length = end_frame - start_frame
    if platform == "win32":
        return (
            'vlc --intf="dummy" --repeat --no-video \
            --start-time="%f" --stop-time="%f" "%s"'
            % (start_frame, end_frame, os.path.abspath(sound_file))
        )
    return (
        'vlc --intf="dummy" --repeat --no-video \
        --start-time="%f" --stop-time="%f" "%s"'
        % (start_frame, end_frame, sound_file)
    )


def get_viewer(app):
    return app.getActiveViewer() or app.getViewer("Viewer1")


# Popen object that we take great effort to prevent from pop-ening.
_proc = None


def open_vlc(sound_file, fps, range_start, range_end):
    global _proc
    cmd = get_command(sound_file, fps, range_start, range_end)
    if platform == "win32":
        _proc = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            shell=True,
        )
    else:
        _proc = subprocess.Popen(
            "exec " + cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            shell=True,
        )
    print("Playing process pid %s " % (_proc.pid))


def play_natron(viewer, thisNode, sound_file, fps, range_start, range_end):
    if range_start > range_end:
        natron.errorDialog(
            "Error", "The end frame should not come before the start frame."
        )
        return

    thisNode.start_frame.set(range_start)
    thisNode.end_frame.set(range_end)
    thisNode.FPS.set(fps)
    viewer.seek(range_start)
    viewer.startForward()
    open_vlc(sound_file, fps, range_start, range_end)


def close_vlc():
    if _proc.poll() is None:
        print("Killing process pid %s " % (_proc.pid))
        # os.kill(proc.pid, signal.SIGKILL)

        if platform == "win32":
            subprocess.Popen("TASKKILL /F /PID {pid} /T".format(pid=_proc.pid))
        else:
            _proc.kill()


def panic_vlc():
    if platform == "win32":
        subprocess.Popen("Taskkill /IM vlc.exe /f")
    else:
        subprocess.Popen(
            "killall vlc", stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True
        )


def vlc_callback(thisParam, thisNode, thisGroup, app, userEdited):
    viewer = get_viewer(app)
    if not viewer:
        if userEdited and thisParam == thisNode.play_song:
            natron.errorDialog(
                "Error",
                "Unable to find active viewer.  Try attaching something to a viewer and playing it without this plugin, then render the first few frames and seek back to the beginning.",
            )
        return

    if thisParam == thisNode.play_song:
        play_natron(
            viewer,
            thisNode,
            thisNode.Sound_File.get(),
            app.frameRate.get(),
            viewer.getCurrentFrame(),
            viewer.getFrameRange()[1],
        )

    if thisParam == thisNode.start_song:
        play_natron(
            viewer,
            thisNode,
            thisNode.Sound_File.get(),
            app.frameRate.get(),
            viewer.getFrameRange()[0],
            viewer.getFrameRange()[1],
        )

    if thisParam == thisNode.stop_song:
        viewer.pause()
        close_vlc()

    if thisParam == thisNode.panic:
        viewer.pause()
        close_vlc()
