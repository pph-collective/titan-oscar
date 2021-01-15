#!/usr/bin/env pypy3
import sys
import subprocess

if sys.version_info < (3, 0, 0):
    raise Exception("Please use Pypy 3.")

TITAN_PATH = "git+https://github.com/marshall-lab/TITAN"

def install_titan(version):
    package = f"{TITAN_PATH}@{version}"

    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])


def parse_version(args):
    if len(args) != 2:
        print("\x1B[31mERROR:\x1B[0m Arguments don't match expected")
        print("\x1B[96mUsage:\x1B[0m ./installTitan.py <version>")
        print("Example: ./installTitan.py v2.0.0")
        exit(1)

    version = args[1].strip()

    return version

if __name__ == '__main__':
    version = parse_version(sys.argv)
    install_titan(version)
