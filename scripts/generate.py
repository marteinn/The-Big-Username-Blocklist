#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json


def convert(path=None):
    # Load raw
    file_path = os.path.join(path, "list_raw.txt")
    with open(file_path, "r") as f:
        usernames = f.readlines()

        # Remote newline
        usernames = [x.strip("\n") for x in usernames]

        # Remove trailing #
        usernames = [x for x in usernames if x and not x.startswith("#")]

        # Sort list
        usernames.sort()

    # Write optimized newline file
    file_path = os.path.join(path, "list.txt")

    optimized_data = "".join("%s\n" % e for e in usernames)
    optimized_data = optimized_data.strip()

    with open(file_path, "w") as f:
        f.write(optimized_data)

    # Write optimized json file
    file_path = os.path.join(path, "list.json")

    with open(file_path, "w") as f:
        json.dump(usernames, f, indent=4, ensure_ascii=False)

    # Write python file
    file_path = os.path.join(path, "list.py")

    with open(file_path, "w") as f:
        f.write("data = %s" % str(usernames))

    # Write es6 module
    file_path = os.path.join(path, "list.js")

    with open(file_path, "w") as f:
        f.write("export default %s;" % str(usernames))


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath(__file__))
    list_dir = os.path.join(current_dir, os.pardir)

    # __file__.startswith("scripts")

    convert(path=list_dir)
