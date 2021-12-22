# -*- coding:utf-8 -*-

name = "create_proj"
version = "1.0.1"

build_command = "python -m rezutil build {root}"
private_build_requires = ["python-2.7+<4", "rezutil-1"]

category = "int"


def commands():
    env = globals()["env"]
    alias = globals()["alias"]

    # For Windows
    env.PATH.prepend("{root}/bin")

    # For Unix
    alias("create", "python {root}/bin/create.py")
