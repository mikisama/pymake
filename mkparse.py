#!/usr/bin/env python

import sys
import pymake.parser


def main():
    for f in sys.argv[1:]:
        print("Parsing %s" % f)
        fd = open(f, 'r')
        s = fd.read()
        fd.close()
        stmts = pymake.parser.parsestring(s, f)
        print(stmts)


if __name__ == "__main__":
    main()
