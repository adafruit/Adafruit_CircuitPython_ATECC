Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-atecc/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/atecc/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://travis-ci.com/adafruit/Adafruit_CircuitPython_ATECC.svg?branch=master
    :target: https://travis-ci.com/adafruit/Adafruit_CircuitPython_ATECC
    :alt: Build Status

Driver for `Microchip's ATECCx08 cryptographic co-processors with secure hardware-based key storage <https://www.adafruit.com/product/4314>`_.

Note: This library was developed and tested with an ATECC608A, but should work for ATECC508 modules as well.


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
=====================
.. note:: This library is not available on PyPI yet. Install documentation is included
   as a standard element. Stay tuned for PyPI availability!

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-atecc/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-atecc

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-atecc

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-atecc

Usage Example
=============

.. todo:: Add a quick, simple example. It and other examples should live in the examples folder and be included in docs/examples.rst.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_ATECC/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Sphinx documentation
-----------------------

Sphinx is used to build the documentation based on rST files and comments in the code. First,
install dependencies (feel free to reuse the virtual environment from above):

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install Sphinx sphinx-rtd-theme

Now, once you have the virtual environment activated:

.. code-block:: shell

    cd docs
    sphinx-build -E -W -b html . _build/html

This will output the documentation to ``docs/_build/html``. Open the index.html in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass.

License
========

This library was written by Arduino SA. We've converted it to work with Adafruit CircuitPython and made
changes for it to work with CircuitPython devices and single-board linux computers running CircuitPython libraries. We've
added examples to demonstrate using the nonce, random, monotonic counter and SHA256 security functions within the library.

This open source code is licensed under the LGPL License (see LICENSE for details).