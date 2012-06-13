#!/usr/bin/python2
""" turn a pip cache into a pypi index.. """
import os
import shutil
import argparse

from pip.commands.install import InstallCommand

def main():
    pip_install = InstallCommand()
    o,a = pip_install.parser.parse_args([])

    parser = argparse.ArgumentParser(description="turn a pip cache into a pypi index")
    parser.add_argument('dest', metavar='DEST_DIR', nargs=1,help="destination directory")
    parser.add_argument('-v','--verbose',action='store_true',default=False,help="verbose output")
    parser.add_argument('-p','--pip-cache',default=o.download_cache)

    args = parser.parse_args()

    dest = args.dest[0]
    verbose = args.verbose

    PIP_CACHE = os.path.expanduser(args.pip_cache)


    if not os.path.exists(dest):
        os.mkdir(dest)

    cache_contents = os.listdir(PIP_CACHE)
    for cache_entry in cache_contents:
        filename = cache_entry.split("%2F")[-1]
        cache_path = os.path.join(PIP_CACHE,cache_entry)
        if filename.endswith('content-type'):
            continue
        components = filename.split('-')[0:-1]
        pkg_name = '-'.join(components)
        pkg_dir = os.path.join(dest,pkg_name)
        pkg_path = os.path.join(pkg_dir,filename)
        if not os.path.exists(pkg_dir):
            os.mkdir(pkg_dir)
        if verbose:
            print filename
        shutil.copy(cache_path,pkg_path)

if __name__ == '__main__':
    main()
