import config
import json
import alpaca_trade_api as tradeapi
import main

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

etf = main.data
#print(etf)

#Check buying power
account = api.get_account()
cash = round(float(account.buying_power), 2)
#print(f"My buying power is {cash}")

def buy():
    for key in etf.keys():
      minimuminvestment = etf[key]['minimuminvestment']
      #remove $ sign, then turn string to float
      minString = minimuminvestment[1:]
      notional = float(minString)
      stock = etf[key]['symbol']

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