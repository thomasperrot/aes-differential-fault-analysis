*******************************
AES Differential Fault Analysis
*******************************

.. image:: https://img.shields.io/badge/python-3.6+-blue
   :target: https://www.python.org/downloads/release/python-350/
   :alt: Python3.6+ compatible

.. image:: https://travis-ci.com/thomasperrot/aes-differential-fault-analysis.svg?branch=master
   :target: https://travis-ci.org/thomasperrot/aes-differential-fault-analysis
   :alt: Continuous Integration Status

.. image:: https://codecov.io/gh/thomasperrot/aes-differential-fault-analysis/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/thomasperrot/aes-differential-fault-analysis
   :alt: Coverage Status

.. image:: https://img.shields.io/badge/License-MIT-green.svg
   :target: https://github.com/thomasperrot/aes-differential-fault-analysis/blob/master/LICENSE.rst
   :alt: MIT License

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style black


Differential Fault Analysis of AES using a single fault

Overview
********

This repository is an implementation of a Differential Fault Analysis on AES, using a single fault. It is based on the
research paper `Differential Fault Analysis of the Advanced EncryptionStandard using a Single Fault`_. This approach
boils down to reducing the set of possible keys to :math:`2^32` thanks to a first set of equations, then reducing this
set to :math:`2^8` possible keys thanks to a second set of equations. It relies on a single fault introduced in AES
8th round, before Sub Bytes.

**N.B:** The research paper contains several mistakes in the equations it provides. I corrected them in my source code.

.. _Differential Fault Analysis of the Advanced EncryptionStandard using a Single Fault: https://eprint.iacr.org/2009/575.pdf

Quickstart
**********

To install the package:

.. code-block:: bash

   pip install .

Then run the attack:

.. code-block:: python

    >>> from aes_dfa.attack import attack
    >>> normal_cipher_text = "81d6cdc3bd16fb8d72b9bb88818b5be9"
    >>> faulty_cipher_text = "eff93508630187b8d3494e8b70e6887e"
    >>> keys = attack(normal_cipher_text, faulty_cipher_text)
    [ ] Computing all possible keys...
    [ ] Reducing key space...
    [+] Finished !
    >>> print(len(keys))
    256
    >>> print(keys[0])
    41414141414141414141414141414141




Disclaimer
**********

The source code has absolutely no documentation, as all you need is already provided in paper, and documenting is
pretty boring.

Performance
***********

The program takes on average 8h to run on my computer. Multiprocessing can be easily added in the second step to reduce
this duration linearly with your number of cores.

Issues
******

If you encounter an issue, please fill free to open an issue_.

.. _issue: https://github.com/thomasperrot/aes-differential-fault-analysis/issues