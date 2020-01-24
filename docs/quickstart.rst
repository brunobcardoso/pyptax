Quickstart
==========

Closing Ptax rates for a requested date
---------------------------------------

As a simple example, we'll request closing information on Ptax rates on January 20, 2020.
We have to inform the date in the format YYYY-MM-DD.

    >>> from pyptax import ptax
    >>> close_report = ptax.close('2020-01-20')
    >>> close_report
    CloseReport(datetime='2020-01-20 13:09:02.871', bid='4.1823', ask='4.1829')

The ptax.close returns an instance of CloseReport:

    >>> close_report.datetime
    '2020-01-20 13:09:02.871'
    >>> close_report.bid
    '4.1823'
    >>> close_report.ask
    '4.1829'

It's also possible to process the information as a dictionary:

    >>> close_report.as_dict
    {'datetime': '2020-01-20 13:09:02.871', 'bid': '4.1823', 'ask': '4.1829'}
