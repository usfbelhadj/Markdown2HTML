#!/usr/bin/python3
''' Markdown to HTML '''
import sys
from os import path


if __name__ == "__main__":
    line_list = []
    '''the number of arguments is less than 2'''
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.mdREADME.html", file=sys.stderr)
        exit(1)
    '''Markdown file doesn’t exist'''
    path_file = sys.argv[1]
    if not path.exists(path_file):
        print("Missing {}".format(sys.argv[1]), file=sys.stderr)
        exit(1)
    '''Headings Markdown'''
    with open(sys.argv[1], 'r') as read_file:
        for lines in read_file.readlines():
            cout_cra = 0
            for line in lines:
                for car in range(len(line)):
                    if line[car] == '#':
                        cout_cra += 1
            lines = lines.rstrip('\r\n')
            line_list.append(f"<h{cout_cra}>{lines.replace('#','')}</h{cout_cra}>")
        with open(sys.argv[2], 'a') as write_file:
            for line in line_list:
                write_file.write(f'{line}\n')
