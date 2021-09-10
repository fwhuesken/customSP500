import config
import json
import alpaca_trade_api as tradeapi
import selection
from flask import Flask, render_template, request, jsonify, url_for, redirect
import json

site = Flask(__name__)

@site.route('/')
def index():
    return render_template('index.html')

site.run(host='0.0.0.0', port=8080)

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
#print(portfolio)

#Making sure that I can convert csv to json
data_file = 'meta_etf.csv'
selection = selection.get_json(data_file)
#print(selection_json)


#JSON: Check if the chosen stocks are actually fractionable
def final_selection():
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

etf = final_selection()
#print(etf)

#Check buying power
account = api.get_account()
cash = round(float(account.buying_power), 2)
#print(f"My buying power is {cash}")

def buy():
  if cash < len(etf):
    print(f"There are {len(etf)} positions in your ETF. With your current cash balance of ${cash} (not including open orders) you fail to reach the minimum order of $1 per position")
  else:
    for key in etf.keys():
      weight = float(etf[key]['weight'])
      notional = round(cash * weight,2)
      stock = etf[key]['symbol']
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
buy()
