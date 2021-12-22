# -*- coding:utf-8 -*-

name = "graphviz"
version = "2.49.1"
description = "Graphviz - Graph Visualization Software"

url = "https://www.graphviz.org/"

variants = [
    ["platform-*"],
]

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1", "python-3.7"]


def commands():
    env = globals()["env"]

    env.PATH.append(r"C:\Program Files\Graphviz\bin")