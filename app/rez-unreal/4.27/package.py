# -*- coding: utf-8 -*-

late = globals()["late"]

name = "unreal"
version = "4.27"
description = "Unreal Engine 4.27"

_data = {
    # Allzpark
    "label": "Unreal Engine",
    "icon": "{root}/resources/unrealico.jpg"
}

tools = [
    "unreal",
]

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1", "python"]


def commands():
    env = globals()["env"]
    alias = globals()["alias"]
    system = globals()["system"]

    if system.platform == "windows":
        # Escape spaces for PowerShell
        env.UNREAL_LOCATION = "C:/Program` Files/Epic` Games/UE_{this.version}"
        alias("unreal", "{env.UNREAL_LOCATION}/Engine/Binaries/Win64/UE4Editor.exe")
