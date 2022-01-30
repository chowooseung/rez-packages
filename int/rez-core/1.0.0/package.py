# -*- coding:utf-8 -*-

"""
환경변수나 하드코딩이 필요한것들.
"""

name = "core"
version = "1.4.5"
author = "chowooseoung"

environ = {
    "any": {
        "SHOW_PATH": "C:/Users/chowo/production/show",

        "INHOUSE_PATH": "C:/Users/chowo/production/inhouse",
        "DCC_PATH": "C:/Users/chowo/production/inhouse/DCC",
        "MAYA_PATH": "C:/Users/chowo/production/inhouse/DCC/maya",

        "NOLAVA_PATH": "C:/Users/chowo/production/inhouse/nolava_config",

        "MONGO": "localhost:27017",
    },

    "maya": {
        "XBMLANGPATH": [
            "{env.MAYA_PATH}/icons"
        ]
    }
}

environ_ = {
    "any": {

    },

    "maya": {
        "MAYA_MODULE_PATH": [
            "{env.MAYA_PATH}/ext/modules/animation",
            "{env.MAYA_PATH}/ext/modules/common",
            "{env.MAYA_PATH}/ext/modules/modeling",
            "{env.MAYA_PATH}/ext/modules/rigging",
            "{env.MAYA_PATH}/ext/modules/CFX",
            "{env.MAYA_PATH}/int/modules/animation",
            "{env.MAYA_PATH}/int/modules/common",
            "{env.MAYA_PATH}/int/modules/modeling",
            "{env.MAYA_PATH}/int/modules/rigging",
            "{env.MAYA_PATH}/int/modules/CFX"
        ],

        "PYTHONPATH": [
            "{env.MAYA_PATH}/ext/scripts",
            "{env.MAYA_PATH}/int/scripts"
        ],

        "MAYA_PLUG_IN_PATH": [
            "{env.MAYA_PATH}/ext/plug-ins/animation",
            "{env.MAYA_PATH}/ext/plug-ins/common",
            "{env.MAYA_PATH}/ext/plug-ins/modeling",
            "{env.MAYA_PATH}/ext/plug-ins/rigging",
            "{env.MAYA_PATH}/ext/plug-ins/CFX",
            "{env.MAYA_PATH}/int/plug-ins/animation",
            "{env.MAYA_PATH}/int/plug-ins/common",
            "{env.MAYA_PATH}/int/plug-ins/modeling",
            "{env.MAYA_PATH}/int/plug-ins/rigging",
            "{env.MAYA_PATH}/int/plug-ins/CFX"
        ],
    }
}

build_command = "python -m rezutil build {root}"
private_build_requires = ["python-2.7+<4", "rezutil-1"]


def commands():
    import os

    env = globals()["env"]
    this = globals()["this"]
    request = globals()["request"]
    expandvars = globals()["expandvars"]

    environ = this.environ
    result = list(environ["any"].items())

    # Add request-specific environments
    for key, values in environ.items():
        if key not in request:
            continue

        result += list(values.items())

    for key, value in result:
        if isinstance(value, (tuple, list)):
            [env[key].append(expandvars(v)) for v in value]
        else:
            env[key] = expandvars(value)

    environ_ = this.environ_
    result1 = list()
    for key, values in environ_.items():
        if key not in request:
            continue
        for k, v in values.items():
            paths = list()
            for path in v:
                if os.path.exists(expandvars(path)):
                    [paths.append(os.path.join(expandvars(path), x)) for x in os.listdir(expandvars(path)) if
                     os.path.isdir(os.path.join(expandvars(path), x))]
            result1.append((k, paths))

    for key, value in result1:
        if isinstance(value, (tuple, list)):
            [env[key].append(expandvars(v)) for v in value]
        else:
            env[key] = expandvars(value)
