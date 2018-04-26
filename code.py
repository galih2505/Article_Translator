#!/usr/bin/env python3

import argparse
import os
import sys


def is_file(fileName, extension):
    fileName=fileName.split(".")
    if fileName[-1] == extension:
        return True
    else
        print("Please give me correct file !!!")
        print("Programme is terminated.")
        sys.exit()

class Translator(object):
    """Article Translator"""
    def __init__(self):
        self.currPath = os.getcwd()





if __name__ == '__main__':
    trs = Translator()

    parser = argparse.ArgumentParser(description="Article Translator")
    parser.add_argument("-s", "--string", help="Girdi olarak string ver.", action="store_true")
    parser.add_argument("-p", "--pdf", help="Girdi olarak PDF belgesi ver.", action="store_true")
    parser.add_argument("-t", "--text", help="Girdi olarak text belgesi ver.", action="store_true")
    parser.add_argument("-c", "--outclew", help="ClewWord için çıktı al.", action="store_true")
    args = parser.parse_args()

    if args.string:
        pass

    if args.pdf:
        pass

    if args.text:
        pass

    if args.outclew:
        pass