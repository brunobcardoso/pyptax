=============
Release Notes
=============

Version 0.5.0
=============
- Add resource to provide historical bid and ask rates for a requested time period.
- Add resource to provide intermediary rates for a requested date.
- Rename `CloseReport` to `Bulletin` and define its type on the internal attribute `bulletin_type`.
- Remove string conversion on bid and ask rates retrieved.
- Fix development installation docs.

Version 0.4.0
=============
- Add Command line interface.
- Improve exceptions handling.

  - Add ``ClientException`` to deal with response error.
  - Add ``UnavailableDataError`` to handle empty data returned.

- Add ``Close.display`` method to show data as a fixed width table for pretty printing.

Version 0.3.0
=============
- ``ptax.close`` requires date in the format YYYY-MM-DD
- Requires Python 3.7 or later
- Add documentation to readthedocs https://pyptax.readthedocs.io/.

Version 0.2.0
=============
-   ``ptax.close`` returns an instance of the ``CloseReport`` model instead of a dict.

Before:

    >>> from pyptax import ptax
    >>> ptax.close('01-20-2020')
    >>> {'datetime': '2020-01-20 13:09:02.871', 'bid': '4.1823', 'ask': '4.1829'}

After:

    >>> from pyptax import ptax
    >>> ptax.close('01-20-2020')
    >>> CloseReport(datetime='2020-01-20 13:09:02.871', bid='4.1823', ask='4.1829')
    >>> ptax.close('01-20-2020').as_dict
    >>> {'datetime': '2020-01-20 13:09:02.871', 'bid': '4.1823', 'ask': '4.1829'}

-   Create a client to deal with service request to add support for new features.
-   Add PyPI publish commands.
-   Fix typo in documentation

Version 0.1.0
=============

-   First public release.
