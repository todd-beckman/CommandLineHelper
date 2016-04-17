#!/usr/bin/python

import sys

def get_flags():
    flags = []
    for i in range (1, len(sys.argv)):
        word = sys.argv[i]
        if word[0] == "-":
            for j in range(1, len(word)):
                try:
                    flags.index(word[j])
                except:
                    flags.append(word[j])
    return flags

def get_args():
    return sys.argv