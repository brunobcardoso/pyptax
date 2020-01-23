Contributing
============

Contributions are always welcome and appreciated. You can contribute with pull requests, bug reports,
features requests, and feedback.

Development installation
------------------------
- Fork PyPtax to your GitHub account
- Clone your fork and create a branch for the code you want to add
- Create a new virtualenv and install the package in development mode

.. code-block:: bash

    $ git clone git@github.com:your_user_name/pyptax.git
    $ cd pyptax
    $ git checkout -b your_contribution_branch
    $ python -m venv .venv
    $ source .venv/bin/activate
    (.venv) $ python -m pip install -U pip setuptools
    (.venv) $ pip install -U -e .[dev]

Testing
-------
PyPtax uses tox for testing and development. With tox installed, just execute:

.. code-block:: bash

    $ tox

It'll run the tests in all supported Python versions and pre-commit checks.

You can run against a specific available version, by executing:

.. code-block:: bash

    $ tox -e py38
