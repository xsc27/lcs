===
LCS
===
.. image:: https://github.com/cmeza99/lcs/workflows/Tests/badge.svg?branch=master
     :target: https://github.com/cmeza99/lcs/actions?workflow=Tests
     :alt: CI Status

Longest Common Substring and API

Installation
============
.. code-block:: console

   pip install git+https://github.com/cmeza99/lcs.git

Usage
=====

CLI
---

`lcs`

.. code-block:: console

   usage: lcs [-h] [-v] STRING STRING [STRING ...]

   LCS CLI Help

   positional arguments:
     STRING
     STRING         Strings to be queried (at least 2).

   optional arguments:
     -h, --help     show this help message and exit
     -v, --version  show program's version number and exit

Module
------
.. code-block:: console

   python3 -m lcs --help

API Server
==========

Start Locally
-------------

To start the web app at http://localhost:8000/:

.. code-block:: console

   pip3 install uvicorn
   uvicorn lcs.web:app --reload

API CLI
-------

`lcs-api`

.. code-block:: console

   usage: lcs-api [-h] [-v] [--url URL] FILE

   LCS CLI Help

   positional arguments:
     FILE           JSON data.

   optional arguments:
     -h, --help     show this help message and exit
     -v, --version  show program's version number and exit
     --url URL      Url for the LCS web app (default: http://localhost:8000).

License
=======
Copyright 2020 Carlos Meza

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
