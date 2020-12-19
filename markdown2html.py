#!/usr/bin/python3

import sys
from os import path


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html")
        exit(1)
    for i in range(1, len(sys.argv)):
        path_file = f"/home/djo/Specializations/Markdown2HTML/{sys.argv[i]}"
        if path.exists(path_file) == True:
            print(f"Missing {sys.argv[i]}")
        exit(1)