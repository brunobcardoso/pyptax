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
      historical  Provides bid and ask rates for the requested time period.

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

.. autofunction:: pyptax.cli.historical

Options:
  -sd, --start_date YYYY-MM-DD  [required]
  -ed, --end_date YYYY-MM-DD    [required]
  --help                  Show this message and exit.

Examples:
    .. code-block::

       $ pyptax historical --start_date 2020-01-02 --end_date 2020-01-28
       +-------------------------+--------+--------+
       | datetime                |    bid |    ask |
       |-------------------------+--------+--------|
       | 2020-01-02 13:11:10.762 | 4.0207 | 4.0213 |
       | 2020-01-03 13:06:22.606 | 4.0516 | 4.0522 |
       | 2020-01-06 13:03:22.271 | 4.0548 | 4.0554 |
       | 2020-01-07 13:06:14.601 | 4.0835 | 4.0841 |
       | 2020-01-08 13:03:56.075 | 4.0666 | 4.0672 |
       | 2020-01-09 13:03:52.663 | 4.0738 | 4.0744 |
       | 2020-01-10 13:10:19.927 | 4.0739 | 4.0745 |
       +-------------------------+--------+--------+
