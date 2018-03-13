# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named EWA_GLExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from EWA_GLExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.EWA_GL"

def getLabel():
    return "EWA_GL"

def getVersion():
    return 1.0

def getIconPath():
    return "EWA_GL.png"

def getGrouping():
    return "Community/GLSL/Effect"

def getPluginDescription():
    return "GPU accelerated EWA antialiasing effect based on Shadertoy."

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

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat0", "Filter width : ")
    param.setMinimum(0, 0)
    param.setMaximum(32, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(32, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat0 = param
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

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat1", "Filter sharpness : ")
    param.setMinimum(0, 0)
    param.setMaximum(32, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(32, 0)
    param.setDefaultValue(4, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat1 = param
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

    param = lastNode.createIntParam("Shadertoy1_2paramValueInt2", "Texel limit : ")
    param.setMinimum(1, 0)
    param.setMaximum(4096, 0)
    param.setDisplayMinimum(1, 0)
    param.setDisplayMaximum(4096, 0)
    param.setDefaultValue(16, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueInt2 = param
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

    param = lastNode.createSeparatorParam("NAME", "EWA_GL v1.0")

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
    lastNode.setPosition(4139, 3997)
    lastNode.setSize(80, 44)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput2 = lastNode

    del lastNode
    # End of node "Output2"

    # Start of node "Source"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source")
    lastNode.setLabel("Source")
    lastNode.setPosition(4139, 3697)
    lastNode.setSize(80, 44)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSource = lastNode

    del lastNode
    # End of node "Source"

    # Start of node "Shadertoy1_2"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Shadertoy1_2")
    lastNode.setLabel("Shadertoy1_2")
    lastNode.setPosition(4139, 3856)
    lastNode.setSize(80, 44)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShadertoy1_2 = lastNode

    param = lastNode.getParam("paramValueFloat0")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramValueFloat1")
    if param is not None:
        param.setValue(4, 0)
        del param

    param = lastNode.getParam("paramValueInt2")
    if param is not None:
        param.setValue(16, 0)
        del param

    param = lastNode.getParam("imageShaderFileName")
    if param is not None:
        param.setValue("/users/ffernandez/Natron2-3-6/Plugins/OFX/Natron/Shadertoy.ofx.bundle/Contents/Resources/presets/Shadertoy/EWA.frag.glsl")
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("//\n//\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//                        MM.                          .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                     MM.  .MMMM        MMMMMMM    MMM.  .MM\n//                    MM.  .MMM           MMMMMM     MMM.  .MM\n//                   MM.  .MmM              MMMM      MMM.  .MM\n//                  MM.  .MMM                 MM       MMM.  .MM\n//                 MM.  .MMM                   M        MMM.  .MM\n//                MM.  .MMM                              MMM.  .MM\n//                 MM.  .MMM                            MMM.  .MM\n//                  MM.  .MMM       M                  MMM.  .MM\n//                   MM.  .MMM      MM                MMM.  .MM\n//                    MM.  .MMM     MMM              MMM.  .MM\n//                     MM.  .MMM    MMMM            MMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                        MM.                          .MM\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//\n//\n//\n//\n// Adaptation pour Natron par F. Fernandez\n//\n// Adapted to Natron by F.Fernandez\n//\n// EWA filtering\n// Filtering code originally from http://www.pmavridis.com/ewa.html\n// Hacked up extensively to work on old GPUs by lewis@lewissaunders.com\n\n\n// iChannel0: front, filter = nearest, wrap=clamp\n// BBox: iChannel0\n\n\n\nuniform float filterwidth = 1; // Filter width : (filter width), min=0, max=32\nuniform float filtersharpness = 4; // Filter sharpness : (filter sharpness), min=0, max=32\nuniform int texellimit = 16; // Texel limit : (texel limit), min=1, max=4096\n\n\n\nvec4 texture2DEWA(sampler2D tex0, vec2 p0) {\n\tvec2 du = dFdx(p0);\n\tvec2 dv = dFdy(p0);\n\tfloat scale = iResolution.x;\n\n\tp0 -=vec2(0.5,0.5)/scale;\n\tvec2 p = scale * p0;\n\n\tfloat ux = filterwidth * du.s * scale;\n\tfloat vx = filterwidth * du.t * scale;\n\tfloat uy = filterwidth * dv.s * scale;\n\tfloat vy = filterwidth * dv.t * scale;\n\n\t// compute ellipse coefficients \n\t// A*x*x + B*x*y + C*y*y = F.\n\tfloat A = vx*vx+vy*vy+1.0;\n\tfloat B = -2.0*(ux*vx+uy*vy);\n\tfloat C = ux*ux+uy*uy+1.0;\n\tfloat F = A*C-B*B/4.0;\n\n\t// Compute the ellipse\'s (u,v) bounding box in texture space\n\tfloat bbox_du = 2.0 / (-B*B+4.0*C*A) * sqrt((-B*B+4.0*C*A)*C*F);\n\tfloat bbox_dv = 2.0 / (-B*B+4.0*C*A) * sqrt(A*(-B*B+4.0*C*A)*F);\n\n\t// Clamp the ellipse so that the bbox includes at most TEXEL_LIMIT texels.\n\t// This is necessary in order to bound the run-time, since the ellipse can be arbitrarily large\n\t// Note that here we are actually clamping the bbox directly instead of the ellipse.\n\tif(bbox_du*bbox_dv>float(texellimit)) {\n\t\tfloat ll = sqrt(bbox_du*bbox_dv / float(texellimit));\n\t\tbbox_du/=ll;\n\t\tbbox_dv/ll;\n\t}\n\n\t// The ellipse bbox\t\t\t    \n\tint u0 = int(floor(p.s - bbox_du));\n\tint u1 = int(ceil (p.s + bbox_du));\n\tint v0 = int(floor(p.t - bbox_dv));\n\tint v1 = int(ceil (p.t + bbox_dv));\n\n\t// Heckbert MS thesis, p. 59; scan over the bounding box of the ellipse\n\t// and incrementally update the value of Ax^2+Bxy*Cy^2; when this\n\t// value, q, is less than F, we\'re inside the ellipse so we filter\n\t// away...\n\tvec4 num= vec4(0.0, 0.0, 0.0, 1.0);\n\tfloat den = 0.0;\n\tfloat ddq = 2.0 * A;\n\tfloat U = float(u0) - p.s;\n\n\tfor (int v = v0; v <= v1; ++v) {\n\t\tfloat V = float(v) - p.t;\n\t\tfloat dq = A*(2.0*U+1.0) + B*V;\n\t\tfloat q = (C*V + B*U)*V + A*U*U;\n\t\tfor (int u = u0; u <= u1; ++u) {\n\t\t\tif (q < F) {\n\t\t\t\tfloat r2 = q / F;\n\t\t\t\t// Gaussian filter weights\n\t\t\t\tfloat weight = exp(-filtersharpness * r2);\n\t\t\t\n\t\t\t\tnum += weight * texture2D(tex0, vec2(float(u)+0.5,float(v)+0.5)/scale);\n\t\t\t\tden += weight;\n\t\t\t}\n\t\t\tq += dq;\n\t\t\tdq += ddq;\n\t\t}\n\t}\n\tvec4 color = num*(1./den);\n\treturn color;\n}\n\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\n\tvec2 uv = fragCoord.xy / iResolution.xy;\n\tvec4 ewa = texture2DEWA(iChannel0, uv);\n\n\tfragColor = vec4(ewa);\n}")
        del param

    param = lastNode.getParam("mipmap0")
    if param is not None:
        param.set("nearest")
        del param

    param = lastNode.getParam("inputLabel0")
    if param is not None:
        param.setValue("front")
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

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("iChannel0")
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
        param.setValue(3, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("filterwidth")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Filter width :")
        del param

    param = lastNode.getParam("paramHint0")
    if param is not None:
        param.setValue("filter width")
        del param

    param = lastNode.getParam("paramDefaultFloat0")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramMinFloat0")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat0")
    if param is not None:
        param.setValue(32, 0)
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("filtersharpness")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("Filter sharpness :")
        del param

    param = lastNode.getParam("paramHint1")
    if param is not None:
        param.setValue("filter sharpness")
        del param

    param = lastNode.getParam("paramDefaultFloat1")
    if param is not None:
        param.setValue(4, 0)
        del param

    param = lastNode.getParam("paramMinFloat1")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat1")
    if param is not None:
        param.setValue(32, 0)
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("texellimit")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("Texel limit :")
        del param

    param = lastNode.getParam("paramHint2")
    if param is not None:
        param.setValue("texel limit")
        del param

    param = lastNode.getParam("paramDefaultInt2")
    if param is not None:
        param.setValue(16, 0)
        del param

    param = lastNode.getParam("paramMinInt2")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramMaxInt2")
    if param is not None:
        param.setValue(4096, 0)
        del param

    del lastNode
    # End of node "Shadertoy1_2"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput2.connectInput(0, groupShadertoy1_2)
    groupShadertoy1_2.connectInput(0, groupSource)

    param = groupShadertoy1_2.getParam("paramValueFloat0")
    group.getParam("Shadertoy1_2paramValueFloat0").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat1")
    group.getParam("Shadertoy1_2paramValueFloat1").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueInt2")
    group.getParam("Shadertoy1_2paramValueInt2").setAsAlias(param)
    del param

    try:
        extModule = sys.modules["EWA_GLExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
