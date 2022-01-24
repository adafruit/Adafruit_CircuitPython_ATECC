Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-atecc/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/atecc/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_ATECC/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_ATECC/actions
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

Examples of using this module are in examples folder.

Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/atecc/en/latest/>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_ATECC/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

License
========

This library was written by Arduino SA. We've converted it to work with Adafruit CircuitPython and made
changes for it to work with CircuitPython devices and single-board linux computers running CircuitPython libraries. We've
added examples to demonstrate using the nonce, random, monotonic counter and SHA256 security functions within the library.

This open source code is licensed under the LGPL License (see LICENSE for details).
