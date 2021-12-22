# -*- coding: utf-8 -*-

late = globals()["late"]

name = "maya"
version = "2022"
description = "Autodesk Maya 2022"

_data = {
    # Allzpark
    "label": "Maya",
    "icon": "{root}/resources/mayaico.png"
}

tools = [
    "maya",
]

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1", "python"]


def commands():
    env = globals()["env"]
    alias = globals()["alias"]
    system = globals()["system"]

    if system.platform == "windows":
        # Escape spaces for PowerShell
        env.MAYA_LOCATION = "C:/Program` Files/Autodesk/Maya{this.version}"
        alias("maya", "{env.MAYA_LOCATION}/bin/maya.exe")

    # untest
    elif system.platform == "linux":
        env.MAYA_LOCATION = "/usr/autodesk/maya{env.MAYA_VERSION}"

    # untest
    elif system.platform == "osx":
        env.MAYA_LOCATION = "/Applications/Autodesk/maya{env.MAYA_VERSION}"\
                            "/Maya.app/Contents"
        env.DYLD_LIBRARY_PATH = "{env.MAYA_LOCATION}/MacOS"


    # clean Maya.env
    env.MAYA_ENV_DIR = "{root}/resources"

    # Override some Maya default settings (optimization)
    # todo: These might need to be moved out to be left to company specific choices
    env.MAYA_DISABLE_CLIC_IPM = "Yes"
    env.MAYA_DISABLE_CIP = "Yes"
    env.MAYA_DISABLE_CER = "Yes"
    env.PYMEL_SKIP_MEL_INIT = "Yes"
    env.LC_ALL = "C"

    # Enable OpenGL in remote desktop
    env.MAYA_ALLOW_OPENGL_REMOTE_SESSION = "Yes"
