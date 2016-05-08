#!/usr/bin/env python3
"""
Fashion Police problem
for Google Code Jam 2016
Round 1C

Link to problem description:
https://code.google.com/codejam/contest/4314486/dashboard#s=p2

Author:
  Chris Nitsas
  (nitsas)

Language:
  Python 3(.4)

Date:
  May, 2016

Usage:
  python3 runme.py input_file
"""


import sys
import argparse
# modules I've written:
from helpful import *


_program_description = \
'''TEMPLATE PROGRAM DESCRIPTION'''


_input_file_description = \
'''TEMPLATE INPUT FILE DESCRIPTION'''


def parse_args():
    """
    Parse the command line arguments and return them in a namespace.
    """
    parser = argparse.ArgumentParser(description=_program_description)
    parser.add_argument('input_file', help=_input_file_description)
    #parser.add_argument('-v', '--verbose', action='store_true',
    #                    default=False, help='show progress')
    args = parser.parse_args()
    return args


def main(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        raise NotImplementedError()
    return 0


if __name__ == "__main__":
    status = main(parse_args().input_file)
    sys.exit(status)
