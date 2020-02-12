#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "luisfff29"

# import sys


def is_nested(line):
    # new_list = []
    while line:
        token = line[0]
        if line.startswith('(*'):
            print('(*')
            line = line[2:]
        elif line.startswith('*)'):
            print('*)')
            line = line[2:]
        else:
            print(token)
            line = line[1:]


is_nested('(*a++(*)')
# def main(args):
#     """Open the input file and call `is_nested()` for each line"""
#     # Results: print to console and also write to output file
#     pass


# if __name__ == '__main__':
#     main(sys.argv[1:])
