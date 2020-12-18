#!/usr/bin/python3

import sys
import glob


if __name__ == "__main__":
    list_file = []
    if len(sys.argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html ", file=sys.stderr)
        exit(1)
    for file in glob.glob("*.*"):
        list_file.append(file)
    for i in range(1, len(sys.argv)):
        if sys.argv[i] not in list_file:
            print("Missing {}".format(sys.argv[i]))
            exit(1)
    h = 0
    x = ''
    m = ''
    st = ''
    t = []
    with open(sys.argv[1], "r") as main_file:
        for line in main_file.readlines():
            for c in line:
                if c == '#':
                    h+=1
                if c !='#':
                    st+=c
                t = st.split('\n')
            m += str(h)
            h = 0
        for i in range(len(t)):
            with open(sys.argv[2], "a") as put_file:
                put_file.write("<h{}>{}<h{}/>".format(1*(int(x) for j in m),t[i], 1*(int(x) for j in m))
