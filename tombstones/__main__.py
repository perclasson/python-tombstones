from __future__ import print_function

import os
import sys

from tombstones.analysis import find_tombstones


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    dirname = args[0]

    if not dirname or not os.path.isdir(dirname):
        print("You must give a directory as first argument.")
        return

    find_tombstones(os.path.realpath(dirname))

if __name__ == "__main__":
    main()
