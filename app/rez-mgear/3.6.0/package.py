# -*- coding:utf-8 -*-

late = globals()["late"]

name = "mgear"
version = "3.6.0"
description = "mgear download"

build_command = "python {root}/rezbuild.py {install}"
private_build_requires = ["rezutil-1", "python"]

_environ = {
    "MAYA_MODULE_PATH": [
        "{root}/payload/release"
    ],
}

def commands():
    env = globals()["env"]
    this = globals()["this"]
    expandvars = globals()["expandvars"]
    
    _environ = this._environ

    for key, value in _environ.items():
        if isinstance(value, (tuple, list)):
            [env[key].append(expandvars(v)) for v in value]
        else:
            env[key] = expandvars(value)