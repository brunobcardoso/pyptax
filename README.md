<h1 align="center">
  PyPtax
</h1>

<h4 align="center">PyPtax is a Python library and CLI to retrieve information on <i><a href="#what-is-ptax">Ptax rates</a></i></h4>

<p align="center">
  <a href="https://pypi.python.org/pypi/pyptax">
    <img src="https://img.shields.io/pypi/v/pyptax.svg?style=flat-square" alt="Latest Version"/>
  </a>
  <a href="https://travis-ci.org/brunobcardoso/pyptax">
    <img src="https://img.shields.io/travis/brunobcardoso/pyptax/master.svg?style=flat-square" alt="Build Status"/>
  </a>
  <a href="https://codecov.io/gh/brunobcardoso/pyptax">
    <img src="https://codecov.io/gh/brunobcardoso/pyptax/branch/master/graph/badge.svg" alt="Coverage"/>
  </a>
  <a href="https://pypi.python.org/pypi/pyptax/">
    <img src="https://img.shields.io/pypi/pyversions/pyptax.svg?style=flat-square" alt="Supported Versions"/>
  </a>
  <a href='https://pyptax.readthedocs.io/en/latest/?badge=latest'>
    <img src='https://img.shields.io/readthedocs/pyptax/latest?style=flat-square' alt='Documentation Status'/>
  </a>
  <a href='https://github.com/psf/black'>
    <img src='https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square' alt='Code Style'/>
  </a>
</p>

<p align="center">
  <a href="#features">Features</a> |
  <a href="#installation">Installation</a> |
  <a href="#quickstart">Quickstart</a> |
  <a href="#documentation">Documentation</a> |
  <a href="#contributing">Contributing</a>
</p>

## What is Ptax?

[Ptax exchange rate](https://www.bcb.gov.br/conteudo/relatorioinflacao/EstudosEspeciais/EE042_A_taxa_de_cambio_de_referencia_Ptax.pdf)
is the reference exchange rate for U.S. Dollar, expressed as the amount of Brazilian Reais per one U.S. Dollar,
published by the [Central Bank of Brazil](https://www.bcb.gov.br/en).

## Features
 - Closing Ptax rates for a requested date
 - Historical Ptax rates for a requested period
 - Intermediary Ptax rates for a requested date

## Installation
```bash
$ pip install pyptax
```

## Quickstart

### Closing Ptax rates for a requested date

**Command line:**

```bash
$ pyptax close --date 2020-01-20
```

**Module:**

```
>>> from pyptax import ptax
>>> bulletin = ptax.close("2020-01-20")
>>> bulletin.as_dict
{
    "datetime": "2020-01-20 13:09:02.871",
    "bid": 4.1823,
    "ask": 4.1829,
    "bulletin_type":
    "close"
}
>>> bulletin.datetime
"2020-01-20 13:09:02.871"
>>> bulletin.bid
4.1823
>>> bulletin.ask
4.1829
```

### Historical Ptax rates for a requested period

**Command line:**

```bash
$ pyptax historical --start_date 2020-01-01 --end_date 2020-01-05
```

**Module:**

```
>>> from pyptax import ptax
>>> historical_bulletin = ptax.historical('2020-01-01', '2020-01-05')
>>> historical_bulletin
HistoricalBulletin(
    start_date="2020-01-01",
    end_date="2020-01-03",
    bulletins=[
        Bulletin("2020-01-02 13:11:10.762", 4.0207, 4.0213, "close"),
        Bulletin("2020-01-03 13:06:22.606", 4.0516, 4.0522, "close"),
    ],
)

>>> historical_bulletin.as_dict
{
    "start_date": "2020-01-01",
    "end_date": "2020-01-03",
    "bulletins": [
        {
            "datetime": "2020-01-02 13:11:10.762",
            "bid": 4.0207,
            "ask": 4.0213,
            "bulletin_type": "close"
        },
        {
            "datetime": "2020-01-03 13:06:22.606",
            "bid": 4.0516,
            "ask": 4.0522,
            "bulletin_type": "close"
        },
    ],
}
```

> :warning: Enter all dates in the format **_YYYY-MM-DD_**

## Documentation

The full documentation is available on https://pyptax.readthedocs.io/.

## Contributing

Please see the [contributing page](https://github.com/brunobcardoso/pyptax/blob/master/CONTRIBUTING.rst)
for guidance on setting up a development environment and how to contribute.
