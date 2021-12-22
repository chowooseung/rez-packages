
name = "rezutil"

version = "1.4.5"


# build with bez build system
build_command = "python {root}/rezbuild.py"
private_build_requires = ["python-2.7+<4"]


def commands():
    env = globals()["env"]
    env.PYTHONPATH.prepend("{root}/python")
