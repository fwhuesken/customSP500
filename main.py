import config
import json
import alpaca_trade_api as tradeapi
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
print(portfolio)
#Not sure why I keep selection.py separate from main.py
data_file = 'meta_etf.csv'
selection = selection.get_index(data_file)

#Making sure that I can convert csv to json
data_file_json = 'meta_etf_json.csv'
selection_json = selection_json.get_json(data_file_json)
#print(selection_json)

#CSV: Check if the chosen stocks are actually fractionable
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

#JSON: Check if the chosen stocks are actually fractionable
def final_selection_json():
  with open('index.json') as f:    
    data = json.load(f)
    for key in list(data.keys()):
      fractional_asset = api.get_asset(key)
      if not fractional_asset.fractionable:
        del data[key]
    return data 
     #Parsing weight 
    #for key in data.keys():
      #print(data[key]['weight'])

etf_json = final_selection_json()
print(etf_json)

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

def buy_json():
  if cash < len(etf_json):
    print(f"There are {len(etf_json)} positions in your ETF. With your current cash balance of ${cash} (not including open orders) you fail to reach the minimum order of $1 per position")
  else:
    for key in etf_json.keys():
      weight = float(etf_json[key]['weight'])
      notional = round(cash * weight,2)
      stock = etf_json[key]['symbol']
      if notional < 1:
        print(f"Order for {stock} not possible, weight too low to reach minimum order size of $1 per position")
      else:
        api.submit_order(
        symbol=stock,
        notional=notional,
        side='buy',
        type='market',
        time_in_force='day')
      print((f"Submitted order for {stock} for ${notional}"))
  return

#Execute it
#buy()
#final_selection_json()
buy_json()
