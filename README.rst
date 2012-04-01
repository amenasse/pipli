pipli
=====

Turns a pip cache into a pypi index.

The pip cache location is derived from your pip configuration or the PIP_DOWNLOAD_CACHE environment variable.
It can also be overridden via the `--pip-cache` option.

Example::

    $ pipli ~/kami/pypi


Serving the index
-----------------

SimpleHTTPServer which comes with python may suffice::

     $ python -m SimpleHTTPServer  ~/kami/pypi/
     Serving HTTP on 0.0.0.0 port 8000 ...


Using with pip
---------------

Use the `--index-url` option to point pip to your package index::

    pip install --index-url http://0.0.0.0:8000

Alternatively you can use the `find-links` option to refer to a package location::

    pip install --find-links file:///home/kami/pep8/ pep8
