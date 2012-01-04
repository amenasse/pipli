#!/usr/bin/python2
""" turn a pip cache into a pypi index.. """
import os
import shutil

from pip.commands.install import InstallCommand

pip_install = InstallCommand()
o,a = pip_install.parser.parse_args()
PIP_CACHE = o.download_cache
PYPI_DIR = '/usr/local/pypi'

cache_contents = os.listdir(PIP_CACHE)
for cache_entry in cache_contents:
    filename = cache_entry.split("%2F")[-1]
    cache_path = os.path.join(PIP_CACHE,cache_entry)
    if filename.endswith('content-type'):
        continue
    components = filename.split('-')[0:-1]
    pkg_name = '-'.join(components)
    pkg_path = os.path.join(PYPI_DIR,pkg_name,filename)
    if not os.path.exists(pkg_path):
        os.mkdir(pkg_path)
    print (cache_path,pkg_path)
    shutil.copy(cache_path,pkg_path)

