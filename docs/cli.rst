Command Line Interface
======================

After installing the package, the ``pyptax`` command becomes available:

.. code-block::

    $ pyptax

     /$$$$$$$            /$$$$$$$    /$$
    | $$__  $$          | $$__  $$  | $$
    | $$  \ $$ /$$   /$$| $$  \ $$ /$$$$$$    /$$$$$$  /$$   /$$
    | $$$$$$$/| $$  | $$| $$$$$$$/|_  $$_/   |____  $$|  $$ /$$/
    | $$____/ | $$  | $$| $$____/   | $$      /$$$$$$$ \  $$$$/
    | $$      | $$  | $$| $$        | $$ /$$ /$$__  $$  >$$  $$
    | $$      |  $$$$$$$| $$        |  $$$$/|  $$$$$$$ /$$/\  $$
    |__/       \____  $$|__/         \___/   \_______/|__/  \__/
               /$$  | $$
              |  $$$$$$/
               \______/

    Usage: pyptax [OPTIONS] COMMAND [ARGS]...

      PyPtax Command Line Interface

      PyPtax is a Python library to retrieve information on Ptax rates.

    Options:
      -v, --version
      --help         Show this message and exit.

    Commands:
      close  Provides bid and ask rates for the requested date.

.. autofunction:: pyptax.cli.close

Options:
  -d, --date YYYY-MM-DD  [required]
  --help           Show this message and exit.

Examples:
    .. code-block::

       $ pyptax close --date 2020-01-02
       +----------+-------------------------+
       | datetime | 2020-01-02 13:11:10.762 |
       | bid      | 4.0207                  |
       | ask      | 4.0213                  |
       +----------+-------------------------+
