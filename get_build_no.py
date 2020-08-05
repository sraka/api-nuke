#!/usr/bin/env python
# coding=utf-8
"""
This file :
returns the latest build number to sh file
updates the __version__ file with latest release no
"""

import os
import sys
import glob
import subprocess


build_dir = sys.argv[1]   # /mnt/e/programming/code/star/dev/builds/tools/master/
print(build_dir)

def update_version_file(new_version):
    """
    # Write the latest version in the __version__ file
    :return:
    """
    with open("__version__", 'w') as f:
        f.write("__version__=\"{}\"".format(str(new_version)))

if not os.path.exists(build_dir):
    # For a fresh module , if the build dir is not there , then create it
    os.makedirs(build_dir)
    sys.exit(str(1))
else:
    print("------")
    # get the latest folder created by date
    # full_path = /mnt/e/programming/code/star/dev/builds/tools/master/0.0.3-4/
    full_path = max(glob.glob(os.path.join(build_dir, '*/')), key=os.path.getmtime)
    cur_build_no = full_path.split("/")[-2].split("-")[1]
    print(full_path, "current build no : {}".format(cur_build_no))
    new_build_no = (int(cur_build_no) + 1)
    base_name = os.path.basename(os.path.dirname(full_path))      # base_name = 0.0.7-17

    # Get the tag version
    tag_version = subprocess.check_output("git describe --tags", stderr=subprocess.STDOUT, shell=True)
    tag_version = tag_version.strip()

    # Build the new version name and update in __version__ file
    new_version = "{}-{}".format(tag_version, new_build_no)
    print(base_name, new_version)
    update_version_file(new_version)

    # return
    sys.exit(str(new_build_no))