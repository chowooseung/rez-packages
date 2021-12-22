# -*- coding:utf-8 -*-

import os
import sys

url_prefix = "https://github.com/mgear-dev/mgear4/releases/download/{0}".format(os.environ["REZ_BUILD_PROJECT_VERSION"])


def build(source_path, build_path, install_path, targets=None):
    from rezutil import lib
    
    targets = targets or []

    if "install" in targets:
        dst = install_path + "/payload"
    else:
        dst = build_path + "/payload"
    dst = os.path.normpath(dst)

    if os.path.isdir(dst):
        lib.clean(dst)

    filename = "mgear_%s.zip" % (os.environ["REZ_BUILD_PROJECT_VERSION"])
    # Download the source
    url = "%s/%s" % (url_prefix, filename)

    if not os.path.exists(os.path.join(build_path, "download")):
        os.mkdir(os.path.join(build_path, "download"))
    archive = lib.download(url, filename, "download")
    # Unzip the source
    source_root = lib.open_archive(archive)

    # Deploy
    # (we cannot use setup.py to install avalon, there are additional files
    # currently not being installed by it)
    lib.copy_dir(source_root, dst)


if __name__ == "__main__":
    build(source_path=os.environ["REZ_BUILD_SOURCE_PATH"],
          build_path=os.environ["REZ_BUILD_PATH"],
          install_path=os.environ["REZ_BUILD_INSTALL_PATH"],
          targets=sys.argv[1:])