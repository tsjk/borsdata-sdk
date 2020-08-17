# Borsdata python SDK

> unofficial

python SDK for the [Börsdata API](https://github.com/Borsdata-Sweden/API), [detailed docs](https://apidoc.borsdata.se/swagger/index.html).

## Install

`( git pull https://github.com/tsjk/borsdata-sdk && cd borsdata-sdk && pip install . )`

## Usage

A simple example can be found [here](demo/stock-list-ex.ipynb).

```python
from borsdata_sdk import BorsdataAPI

borsdata = BorsdataAPI('<api_key>')

# Meta
markets = borsdata.get_markets()
branches = borsdata.get_branches()
countries = borsdata.get_countries()
sectors = borsdata.get_sectors()

# All stocks
instruments = borsdata.get_instruments()

# Entries for stock with insId == 3
entries = borsdata.get_instrument_stock_price(3)
entries_from_to = borsdata.get_instrument_stock_price(3, '2009-04-22', '2009-04-25')

# Updated instruments
updated_instruments = borsdata.get_instruments_updated()

# Last entries of updated instruments
list_of_updated_instruments = borsdata.get_instrument_stock_price_last()

# Entries for all instruments at a certain date
list_20090423 = borsdata.get_instrument_stock_price_date('2009-04-23')

# Reports
yearly_reports = borsdata.get_instrument_reports(3, 'year')
r12s = borsdata.get_instrument_reports(3, 'r12')
quarters = borsdata.get_instrument_reports(3, 'quarter')
```
