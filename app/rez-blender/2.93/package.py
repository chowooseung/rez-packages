# -*- coding: utf-8 -*-

late = globals()["late"]

name = "blender"
version = "2.93"
description = "Blender 2.93LTs"

_data = {
    # Allzpark
    "label": "Blender",
    "icon": "{root}/resources/blenderico.png"
}

tools = [
    "blender",
]

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1", "python"]


def commands():
    env = globals()["env"]
    alias = globals()["alias"]
    system = globals()["system"]

    if system.platform == "windows":
        # Escape spaces for PowerShell
        env.BLENDER_LOCATION = "C:/Program` Files/Blender` Foundation/Blender` {this.version}"
        alias("blender", "{env.BLENDER_LOCATION}/blender.exe")