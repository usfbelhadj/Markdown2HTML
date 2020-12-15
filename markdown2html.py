#!/usr/bin/python3

import sys
import glob

list_file = []
if len(sys.argv) < 2:
    print("Usage: ./markdown2html.py README.md README.html ", file=sys.stderr)
    exit(1)
for file in glob.glob("*.*"):
    list_file.append(file)
for i in range(1, len(sys.argv)):
    if sys.argv[i] not in list_file:
        print("Missing {}".format(sys.argv[i]))
    else:
        pass
