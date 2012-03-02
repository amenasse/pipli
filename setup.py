import os
from setuptools import setup

version = "0.0.1"

doc_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "docs")
long_description = """

turns a pip cache into a pypi index.

The pip cache loation is derived from your pip configuration or the PIP_DOWNLOAD_CACHE environment variable. It can also be overriden via the --pip-cache option.

"""

setup(name="pipli",
      version=version,
      description="pipli creates a pypi compatible index from a pip cache",
      long_description=long_description,
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='pip pypi',
      author='anthony menasse',
      author_email='amenasse@gmail.com',
      url='http://www.github.com/amenasse/pipli',
      license='MIT',
      packages=['pipli'],
      entry_points=dict(console_scripts=['pipli=pipli.__main__:main'])
)
