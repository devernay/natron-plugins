# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named Crok_perlin_GLExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from Crok_perlin_GLExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.Crok_perlin_GL"

def getLabel():
    return "Crok_perlin_GL"

def getVersion():
    return 1.0

def getIconPath():
    return "Crok_perlin_GL.png"

def getGrouping():
    return "Community/GLSL/Source"

def getPluginDescription():
    return "Creates a perlin noise like pattern."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Controls")
    param = lastNode.createStringParam("sep01", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep01 = param
    del param

    param = lastNode.createStringParam("sep02", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep02 = param
    del param

    param = lastNode.createSeparatorParam("PATTERN", "Pattern")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.PATTERN = param
    del param

    param = lastNode.createStringParam("sep03", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep03 = param
    del param

    param = lastNode.createStringParam("sep04", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep04 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1paramValueFloat2", "Frequency : ")
    param.setMinimum(-1000, 0)
    param.setMaximum(1000, 0)
    param.setDisplayMinimum(-1000, 0)
    param.setDisplayMaximum(1000, 0)
    param.setDefaultValue(3, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueFloat2 = param
    del param

    param = lastNode.createStringParam("sep05", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep05 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1paramValueFloat3", "Gain : ")
    param.setMinimum(0, 0)
    param.setMaximum(5, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(5, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueFloat3 = param
    del param

    param = lastNode.createStringParam("sep06", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep06 = param
    del param

    param = lastNode.createStringParam("sep07", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep07 = param
    del param

    param = lastNode.createSeparatorParam("TIMING", "Timing")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.TIMING = param
    del param

    param = lastNode.createStringParam("sep08", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep08 = param
    del param

    param = lastNode.createStringParam("sep09", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep09 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1paramValueFloat0", "Speed : ")
    param.setMinimum(-99.99999999999999, 0)
    param.setMaximum(99.99999999999999, 0)
    param.setDisplayMinimum(-99.99999999999999, 0)
    param.setDisplayMaximum(99.99999999999999, 0)
    param.setDefaultValue(30, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueFloat0 = param
    del param

    param = lastNode.createStringParam("sep10", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep10 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1paramValueFloat1", "Offset : ")
    param.setMinimum(-99.99999999999999, 0)
    param.setMaximum(99.99999999999999, 0)
    param.setDisplayMinimum(-99.99999999999999, 0)
    param.setDisplayMaximum(99.99999999999999, 0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueFloat1 = param
    del param

    param = lastNode.createStringParam("sep11", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep11 = param
    del param

    param = lastNode.createStringParam("sep12", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep12 = param
    del param

    param = lastNode.createSeparatorParam("COLOUR", "Colour")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.COLOUR = param
    del param

    param = lastNode.createStringParam("sep13", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep13 = param
    del param

    param = lastNode.createStringParam("sep14", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep14 = param
    del param

    param = lastNode.createColorParam("Shadertoy1paramValueVec34", "Colour : ", False)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)
    param.setDefaultValue(1, 1)
    param.restoreDefaultValue(1)
    param.setDefaultValue(1, 2)
    param.restoreDefaultValue(2)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueVec34 = param
    del param

    param = lastNode.createStringParam("sep15", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep15 = param
    del param

    param = lastNode.createStringParam("sep16", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep16 = param
    del param

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("sep101", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep101 = param
    del param

    param = lastNode.createStringParam("sep102", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep102 = param
    del param

    param = lastNode.createSeparatorParam("NAME", "Crok_perlin_GL v1.0")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.NAME = param
    del param

    param = lastNode.createStringParam("sep103", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep103 = param
    del param

    param = lastNode.createStringParam("sep104", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep104 = param
    del param

    param = lastNode.createSeparatorParam("LINE01", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.LINE01 = param
    del param

    param = lastNode.createStringParam("sep105", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep105 = param
    del param

    param = lastNode.createStringParam("sep106", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep106 = param
    del param

    param = lastNode.createSeparatorParam("FR", "ShaderToy 0.8.8")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.FR = param
    del param

    param = lastNode.createStringParam("sep107", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep107 = param
    del param

    param = lastNode.createStringParam("sep108", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep108 = param
    del param

    param = lastNode.createSeparatorParam("CONVERSION", " (Fabrice Fernandez - 2018)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.CONVERSION = param
    del param

    param = lastNode.createStringParam("sep109", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep109 = param
    del param

    param = lastNode.createStringParam("sep110", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep110 = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output2"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output2")
    lastNode.setPosition(4139, 4048)
    lastNode.setSize(80, 44)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput2 = lastNode

    del lastNode
    # End of node "Output2"

    # Start of node "Shadertoy1"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Shadertoy1")
    lastNode.setLabel("Shadertoy1")
    lastNode.setPosition(4139, 3880)
    lastNode.setSize(80, 44)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShadertoy1 = lastNode

    param = lastNode.getParam("paramValueFloat0")
    if param is not None:
        param.setValue(30, 0)
        del param

    param = lastNode.getParam("paramValueFloat1")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramValueFloat2")
    if param is not None:
        param.setValue(3, 0)
        del param

    param = lastNode.getParam("paramValueFloat3")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramValueVec34")
    if param is not None:
        param.setValue(1, 0)
        param.setValue(1, 1)
        param.setValue(1, 2)
        del param

    param = lastNode.getParam("imageShaderFileName")
    if param is not None:
        param.setValue("/users/ffernandez/Natron2-3-6/Plugins/OFX/Natron/Shadertoy.ofx.bundle/Contents/Resources/presets/Shadertoy/Crok_perlin.frag.glsl")
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("\n//\n//\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//                        MM.                          .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                     MM.  .MMMM        MMMMMMM    MMM.  .MM\n//                    MM.  .MMM           MMMMMM     MMM.  .MM\n//                   MM.  .MmM              MMMM      MMM.  .MM\n//                  MM.  .MMM                 MM       MMM.  .MM\n//                 MM.  .MMM                   M        MMM.  .MM\n//                MM.  .MMM                              MMM.  .MM\n//                 MM.  .MMM                            MMM.  .MM\n//                  MM.  .MMM       M                  MMM.  .MM\n//                   MM.  .MMM      MM                MMM.  .MM\n//                    MM.  .MMM     MMM              MMM.  .MM\n//                     MM.  .MMM    MMMM            MMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                        MM.                          .MM\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//\n//\n//\n//\n// Adaptation pour Natron par F. Fernandez\n// Code original : crok_perlin Matchbox pour Autodesk Flame\n\n// Adapted to Natron by F.Fernandez\n// Original code : crok_perlin Matchbox for Autodesk Flame\n\n\nuniform float Speed = 30.0; // Speed : (speed), min=-100, max=100\nuniform float Offset = 0.0; // Offset : (offset), min=-100, max=100\nuniform float Frequency = 3.0; // Frequency : (frequency), min=-1000, max=1000\nuniform float Gain = 1.0; // Gain : (gain), min=0, max=5\nuniform vec3 Colour = vec3(1,1,1); // Colour : (colour)\n\n\nfloat Time = iTime *.05 * Speed + Offset;\n\n//\n// GLSL textureless classic 3D noise \"cnoise\",\n// with an RSL-style periodic variant \"pnoise\".\n// Author:  Stefan Gustavson (stefan.gustavson@liu.se)\n// Version: 2011-10-11\n//\n// Many thanks to Ian McEwan of Ashima Arts for the\n// ideas for permutation and gradient selection.\n//\n// Copyright (c) 2011 Stefan Gustavson. All rights reserved.\n// Distributed under the MIT license. See LICENSE file.\n// https://github.com/ashima/webgl-noise\n//\n\nvec3 mod289(vec3 x)\n{\n  return x - floor(x * (1.0 / 289.0)) * 289.0;\n}\n\nvec4 mod289(vec4 x)\n{\n  return x - floor(x * (1.0 / 289.0)) * 289.0;\n}\n\nvec4 permute(vec4 x)\n{\n  return mod289(((x*34.0)+1.0)*x);\n}\n\nvec4 taylorInvSqrt(vec4 r)\n{\n  return 1.79284291400159 - 0.85373472095314 * r;\n}\n\nvec3 fade(vec3 t) {\n  return t*t*t*(t*(t*6.0-15.0)+10.0);\n}\n\n// Classic Perlin noise\nfloat cnoise(vec3 P)\n{\n  vec3 Pi0 = floor(P); // Integer part for indexing\n  vec3 Pi1 = Pi0 + vec3(1.0); // Integer part + 1\n  Pi0 = mod289(Pi0);\n  Pi1 = mod289(Pi1);\n  vec3 Pf0 = fract(P); // Fractional part for interpolation\n  vec3 Pf1 = Pf0 - vec3(1.0); // Fractional part - 1.0\n  vec4 ix = vec4(Pi0.x, Pi1.x, Pi0.x, Pi1.x);\n  vec4 iy = vec4(Pi0.yy, Pi1.yy);\n  vec4 iz0 = Pi0.zzzz;\n  vec4 iz1 = Pi1.zzzz;\n\n  vec4 ixy = permute(permute(ix) + iy);\n  vec4 ixy0 = permute(ixy + iz0);\n  vec4 ixy1 = permute(ixy + iz1);\n\n  vec4 gx0 = ixy0 * (1.0 / 7.0);\n  vec4 gy0 = fract(floor(gx0) * (1.0 / 7.0)) - 0.5;\n  gx0 = fract(gx0);\n  vec4 gz0 = vec4(0.5) - abs(gx0) - abs(gy0);\n  vec4 sz0 = step(gz0, vec4(0.0));\n  gx0 -= sz0 * (step(0.0, gx0) - 0.5);\n  gy0 -= sz0 * (step(0.0, gy0) - 0.5);\n\n  vec4 gx1 = ixy1 * (1.0 / 7.0);\n  vec4 gy1 = fract(floor(gx1) * (1.0 / 7.0)) - 0.5;\n  gx1 = fract(gx1);\n  vec4 gz1 = vec4(0.5) - abs(gx1) - abs(gy1);\n  vec4 sz1 = step(gz1, vec4(0.0));\n  gx1 -= sz1 * (step(0.0, gx1) - 0.5);\n  gy1 -= sz1 * (step(0.0, gy1) - 0.5);\n\n  vec3 g000 = vec3(gx0.x,gy0.x,gz0.x);\n  vec3 g100 = vec3(gx0.y,gy0.y,gz0.y);\n  vec3 g010 = vec3(gx0.z,gy0.z,gz0.z);\n  vec3 g110 = vec3(gx0.w,gy0.w,gz0.w);\n  vec3 g001 = vec3(gx1.x,gy1.x,gz1.x);\n  vec3 g101 = vec3(gx1.y,gy1.y,gz1.y);\n  vec3 g011 = vec3(gx1.z,gy1.z,gz1.z);\n  vec3 g111 = vec3(gx1.w,gy1.w,gz1.w);\n\n  vec4 norm0 = taylorInvSqrt(vec4(dot(g000, g000), dot(g010, g010), dot(g100, g100), dot(g110, g110)));\n  g000 *= norm0.x;\n  g010 *= norm0.y;\n  g100 *= norm0.z;\n  g110 *= norm0.w;\n  vec4 norm1 = taylorInvSqrt(vec4(dot(g001, g001), dot(g011, g011), dot(g101, g101), dot(g111, g111)));\n  g001 *= norm1.x;\n  g011 *= norm1.y;\n  g101 *= norm1.z;\n  g111 *= norm1.w;\n\n  float n000 = dot(g000, Pf0);\n  float n100 = dot(g100, vec3(Pf1.x, Pf0.yz));\n  float n010 = dot(g010, vec3(Pf0.x, Pf1.y, Pf0.z));\n  float n110 = dot(g110, vec3(Pf1.xy, Pf0.z));\n  float n001 = dot(g001, vec3(Pf0.xy, Pf1.z));\n  float n101 = dot(g101, vec3(Pf1.x, Pf0.y, Pf1.z));\n  float n011 = dot(g011, vec3(Pf0.x, Pf1.yz));\n  float n111 = dot(g111, Pf1);\n\n  vec3 fade_xyz = fade(Pf0);\n  vec4 n_z = mix(vec4(n000, n100, n010, n110), vec4(n001, n101, n011, n111), fade_xyz.z);\n  vec2 n_yz = mix(n_z.xy, n_z.zw, fade_xyz.y);\n  float n_xyz = mix(n_yz.x, n_yz.y, fade_xyz.x); \n  return 2.2 * n_xyz;\n}\n\nfloat surface3 ( vec3 coord ) {\n\t\n\tfloat n = 1.0 * Gain;\t\n\t\t\n\tn -= 1.0\t* abs( cnoise( coord * Frequency ) );\n\tn -= 1.5\t* abs( cnoise( coord * Frequency * 2.0 ) );\n\tn -= 1.25\t* abs( cnoise( coord * Frequency * 2.0 ) );\n\t\n\t\n\treturn n;\n}\n\t\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\n\n\tvec2 position = fragCoord.xy / iResolution.xy;\n\tfloat n = surface3(vec3(position, Time * 0.03));\n\tfragColor = vec4(n * Colour.r , n * Colour.g, n * Colour.b, n);\n}\n")
        del param

    param = lastNode.getParam("inputEnable0")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable1")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable2")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable3")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("mouseParams")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(5, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("Speed")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Speed :")
        del param

    param = lastNode.getParam("paramHint0")
    if param is not None:
        param.setValue("speed")
        del param

    param = lastNode.getParam("paramDefaultFloat0")
    if param is not None:
        param.setValue(30, 0)
        del param

    param = lastNode.getParam("paramMinFloat0")
    if param is not None:
        param.setValue(-99.99999999999999, 0)
        del param

    param = lastNode.getParam("paramMaxFloat0")
    if param is not None:
        param.setValue(99.99999999999999, 0)
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("Offset")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("Offset :")
        del param

    param = lastNode.getParam("paramHint1")
    if param is not None:
        param.setValue("offset")
        del param

    param = lastNode.getParam("paramMinFloat1")
    if param is not None:
        param.setValue(-99.99999999999999, 0)
        del param

    param = lastNode.getParam("paramMaxFloat1")
    if param is not None:
        param.setValue(99.99999999999999, 0)
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("Frequency")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("Frequency :")
        del param

    param = lastNode.getParam("paramHint2")
    if param is not None:
        param.setValue("frequency")
        del param

    param = lastNode.getParam("paramDefaultFloat2")
    if param is not None:
        param.setValue(3, 0)
        del param

    param = lastNode.getParam("paramMinFloat2")
    if param is not None:
        param.setValue(-1000, 0)
        del param

    param = lastNode.getParam("paramMaxFloat2")
    if param is not None:
        param.setValue(1000, 0)
        del param

    param = lastNode.getParam("paramType3")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName3")
    if param is not None:
        param.setValue("Gain")
        del param

    param = lastNode.getParam("paramLabel3")
    if param is not None:
        param.setValue("Gain :")
        del param

    param = lastNode.getParam("paramHint3")
    if param is not None:
        param.setValue("gain")
        del param

    param = lastNode.getParam("paramDefaultFloat3")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramMinFloat3")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat3")
    if param is not None:
        param.setValue(5, 0)
        del param

    param = lastNode.getParam("paramType4")
    if param is not None:
        param.set("vec3")
        del param

    param = lastNode.getParam("paramName4")
    if param is not None:
        param.setValue("Colour")
        del param

    param = lastNode.getParam("paramLabel4")
    if param is not None:
        param.setValue("Colour :")
        del param

    param = lastNode.getParam("paramHint4")
    if param is not None:
        param.setValue("colour")
        del param

    param = lastNode.getParam("paramDefaultVec34")
    if param is not None:
        param.setValue(1, 0)
        param.setValue(1, 1)
        param.setValue(1, 2)
        del param

    del lastNode
    # End of node "Shadertoy1"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput2.connectInput(0, groupShadertoy1)

    param = groupShadertoy1.getParam("paramValueFloat0")
    group.getParam("Shadertoy1paramValueFloat0").setAsAlias(param)
    del param
    param = groupShadertoy1.getParam("paramValueFloat1")
    group.getParam("Shadertoy1paramValueFloat1").setAsAlias(param)
    del param
    param = groupShadertoy1.getParam("paramValueFloat2")
    group.getParam("Shadertoy1paramValueFloat2").setAsAlias(param)
    del param
    param = groupShadertoy1.getParam("paramValueFloat3")
    group.getParam("Shadertoy1paramValueFloat3").setAsAlias(param)
    del param
    param = groupShadertoy1.getParam("paramValueVec34")
    group.getParam("Shadertoy1paramValueVec34").setAsAlias(param)
    del param

    try:
        extModule = sys.modules["Crok_perlin_GLExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
