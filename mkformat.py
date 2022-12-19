#!/usr/bin/env python

import sys
import pymake.parser


def main():
    for f in sys.argv[1:]:
        filename = f
        source = None
        with open(filename, 'r') as fh:
            source = fh.read()

        statements = pymake.parser.parsestring(source, filename)
        print(statements.to_source())


if __name__ == "__main__":
    main()
