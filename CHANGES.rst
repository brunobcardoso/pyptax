=============
Release Notes
=============

Version 0.2.0
=============
-   ``ptax.close`` returns an instance of the `CloseReport`` model instead of a dict.

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
