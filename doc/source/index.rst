.. _index:

=======================================
qiutil - Quantitative Imaging Utilities
=======================================

********
Synopsis
********
qiutil provides helper modules for processing images.

:API: http://quip1.ohsu.edu:8080/qiutil/api

:Git: git\@quip1.ohsu.edu:qiutil
      (`Browse <http://quip1.ohsu.edu:6060/qiutil>`__)


************
Feature List
************
1. XNAT_ facade API.

2. XNAT list, transfer and delete.

3. DICOM metadata list and edit.

4. Python logging configuration.


************
Installation
************
1. Install Git_ on your workstation, if necessary.

2. Contact the qiutil `OHSU QIN Git administrator`_ to get permission to
   access the qiutil Git repository.

3. Clone the `qiutil repository`_::

       cd ~/workspace
       git clone git@quip1:qiutil

4. Install the Python_ pip_ package on your workstation, if necessary.
   
5. Install virtualenv_ package on your workstation, if necessary.

6. Activate a new virtual environment, e.g.::

       virtualenv ~/qiutil
       source ~/qiutil/bin/activate

7. Install the ``qiutil`` package::

       pip install -e .

   This step installs the dependencies in ``requirements.txt``.

*****
Usage
*****
Run the following command for the utility options::

    lsdicom --help
    qicp --help
    qils --help
    qirm --help

---------

.. container:: copyright

  Copyright (C) 2014 Oregon Health & Science University
  `Knight Cancer Institute`_. All rights reserved. ``qiutil`` is confidential
  and may not be distributed in any form without authorization.


.. Targets:

.. _Git: http://git-scm.com

.. _Knight Cancer Institute: http://www.ohsu.edu/xd/health/services/cancer

.. _OHSU QIN Git administrator: loneyf@ohsu.edu

.. _pip: https://pypi.python.org/pypi/pip

.. _Python: http://www.python.org

.. _qiutil repository: http://quip1.ohsu.edu:6060/qiutil


.. toctree::
  :hidden:

  api/index
