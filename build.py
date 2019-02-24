#!/usr/bin/env python3

import argparse
import glob
import os
import util


dirs = ["c", "cpp", "go", "py"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')
    parser.add_argument('--type')
    args = parser.parse_args()

    files = []
    if args.file is not None:
        files.append(args.file)
    elif args.type is not None:
        found = glob.glob(f"{args.type}/*.*")
        files.extend([os.path.basename(x) for x in found])
    else:
        for d in dirs:
            found = glob.glob(f"{d}/*.*")
            files.extend([os.path.basename(x) for x in found])

    util.build(".", "tmp", files)
