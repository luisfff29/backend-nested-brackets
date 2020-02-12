#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "luisfff29"

# import sys


def is_nested(line):
    a = ("(*", "[", "{", "<", "(")
    b = ("*)", "]", "}", ">", ")")
    new_list = []
    while line:
        token = line[0]
        if line.startswith(a):
            if line.startswith('(*'):
                new_list.append('(*')
                line = line[2:]
                continue
            new_list.append(token)
            line = line[1:]
        elif line.startswith(b):
            if line.startswith('*)'):
                new_list.append('*)')
                line = line[2:]
                continue
            new_list.append(token)
            line = line[1:]
        else:
            new_list.append(token)
            line = line[1:]
    print(new_list)

    a = dict(zip(a, b))
    tok = []
    for i, x in enumerate(new_list):
        if x in a:
            tok += [x]
        elif x in b:
            if tok == []:
                print("NO " + str(i+1))
                break
            if x == a.get(tok[-1]):
                tok.pop()
            else:
                print("NO " + str(i+1))
                break
    print(tok)


is_nested('  a(()))-')
# def main(args):
#     """Open the input file and call `is_nested()` for each line"""
#     # Results: print to console and also write to output file
#     pass


# if __name__ == '__main__':
#     main(sys.argv[1:])
