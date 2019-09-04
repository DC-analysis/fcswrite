fcswrite
========

|PyPI Version| |Tests| |Coverage Status|


fcswrite allows you to write .fcs files, a file format used in flow cytometry.
Currently, fcswrite partially supports the `FCS3.0
<https://doi.org/10.1002%2F%28SICI%291097-0320%2819970601%2928%3A2%3C118%3A%3AAID-CYTO3%3E3.0.CO%3B2-B>`__
file format - Contributions to fcswrite are welcome.


Compatibility
-------------
fcswrite was tested (not thoroughly) with these softwares/libraries:

- FlowJo: `<https://www.flowjo.com/>`__
- Flowing Software: `<http://flowingsoftware.btk.fi>`__
- fcsparser: `<https://pypi.org/project/fcsparser/>`__
  (and thus `FlowCytometryTools <https://pypi.org/project/FlowCytometryTools/>`__)
- Python Flow Cytometry (FCM) Tools: `<https://pypi.python.org/pypi/fcm>`__
  (please note that FCM is horribly outdated)


Installation
------------
Install with pip:
::

    pip install fcswrite


Requirements:

- Python 2.7 or Python 3.x
- `numpy <https://github.com/numpy/numpy>`__


Testing
-------
Running tests

::

    python setup.py test

    

.. |PyPI Version| image:: https://img.shields.io/pypi/v/fcswrite.svg
   :target: https://pypi.python.org/pypi/fcswrite
.. |Tests| image:: https://img.shields.io/travis/ZELLMECHANIK-DRESDEN/fcswrite.svg
   :target: https://travis-ci.org/ZELLMECHANIK-DRESDEN/fcswrite
.. |Coverage Status| image:: https://img.shields.io/codecov/c/github/ZELLMECHANIK-DRESDEN/fcswrite/master.svg
   :target: https://codecov.io/gh/ZELLMECHANIK-DRESDEN/fcswrite

