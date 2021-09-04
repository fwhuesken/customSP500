import config
import csv
import alpaca_trade_api as tradeapi
from operator import itemgetter
import math
import selection
import selection_json

#Set up connection to Alpaca
api = tradeapi.REST(config.API_KEY, config.SECRET_KEY, base_url=config.API_URL)

#If insufficient cash error is thrown, check if there are any open orders left
open_orders = api.list_orders(
  status='open'
)
#print(open_orders)

#Cancel all existing orders to avoid insufficient cash error
api.cancel_all_orders()

#If needed: Current positions
portfolio = api.list_positions()

#Not sure why I keep selection.py separate from main.py
data_file = 'meta_etf.csv'
selection = selection.get_index(data_file)

#Making sure that I can convert csv to json
data_file_json = 'meta_etf_json.csv'
selection_json = selection_json.get_json(data_file_json)
print(selection_json)

#Check if the chosen stocks are actually fractionable
def final_selection():
  etf = []
  for stock in selection:
    fractional_asset = api.get_asset(stock)
    if fractional_asset.fractionable:
      etf.append(stock)
      #print(f"We can trade {stock}")
    else:
      print(f"{stock} is not available for fractional trading")
  print(f"My ETF contains the following {len(etf)} stocks: {etf}")
  return etf

etf = final_selection()

#Check buying power
account = api.get_account()
cash = round(float(account.buying_power), 2)
#print(f"My buying power is {cash}")

#Buy stocks if $1 minimum order can be achieved for every stock (ignoring market cap/custom weightings for now)
def buy():
  if cash < len(etf):
    print(f"There are {len(etf)} positions in your ETF. With your current cash balance of ${cash} (not including open orders) you fail to reach the minimum order of $1 per position")
  else:
    notional = round(cash / len(etf),2)
    for stock in etf:
      api.submit_order(
        symbol=stock,
        notional=notional,
        side='buy',
        type='market',
        time_in_force='day')
      print((f"Submitted order for {stock} for ${notional}"))
  return

#Execute it
buy()

