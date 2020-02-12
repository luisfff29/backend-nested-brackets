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

    a = dict(zip(a, b))
    tok = []
    for i, x in enumerate(new_list):
        if x in a:
            tok += [x]
        elif x in b:
            if tok == []:
                tok += [x]
                return "NO " + str(i+1)
            if x == a.get(tok[-1]):
                tok.pop()
            else:
                return "NO " + str(i+1)
    if tok == []:
        return "YES"
    elif tok == new_list:
        return "NO " + str(len(new_list))
    elif tok:
        return "NO " + str(len(new_list)+1)


print(is_nested('(([('))
# def main(args):
#     """Open the input file and call `is_nested()` for each line"""
#     # Results: print to console and also write to output file
#     pass


# if __name__ == '__main__':
#     main(sys.argv[1:])
