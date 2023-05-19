#!/usr/bin/env python

import os
import subprocess
import numpy as np

my_dict = {}

names = ["files", "readlinks"]

for name in names:

    my_dict[name] = []

    with open(os.path.expanduser("~/scripts/" + name)) as file:
        for item in file:
            my_dict[name].append(item.splitlines()[0])

my_dict["projects_files"] = []
my_dict["projects_readlinks"] = []

for i in range(len(my_dict["readlinks"])):
    if "/projects" in my_dict["readlinks"][i]:
        my_dict["projects_readlinks"].append(my_dict["readlinks"][i])
        my_dict["projects_files"].append(my_dict["files"][i])

    my_dict["projects_readlinks"][i] = my_dict["projects_readlinks"][i].replace(
        "/projects/ocean", "/gws/nopw/j04/tids/OCEAN"
    )

for name in names:

    with open(os.path.expanduser("~/scripts/projects_" + name), "w") as fp:
        for item in my_dict["projects_" + name]:
            fp.write("%s\n" % item)

with open(os.path.expanduser("~/scripts/projects_files")) as f:
    projects_files = f.read().splitlines()

with open(os.path.expanduser("~/scripts/projects_readlinks")) as f:
    projects_files = f.read().splitlines()

for i in range(len(projects_files)):
    src = projects_readlinks[i]
    dest = projects_files[i]
    try:
        os.remove(dest)
    except OSError:
        pass
    os.symlink(src, dest)
