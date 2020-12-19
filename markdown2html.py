#!/usr/bin/python3
''' Markdown to HTML '''
import sys
from os import path


if __name__ == "__main__":
    '''the number of arguments is less than 2'''
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.mdREADME.html", file=sys.stderr)
        exit(1)
    '''Markdown file doesn’t exist'''
    for i in range(1, len(sys.argv)):
        path_file = f"/home/djo/Specializations/Markdown2HTML/{sys.argv[i]}"
        if not path.exists(path_file):
            print(f"Missing {sys.argv[i]}", file=sys.stderr)
            exit(1)
