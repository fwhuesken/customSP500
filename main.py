from flask import Flask, render_template, request, jsonify, url_for, redirect
import sqlite3
import config
import alpaca_trade_api as tradeapi


site = Flask(__name__)

@site.route('/', methods=['GET', 'POST'])
def index():
  con = sqlite3.connect('app.db')
  con.row_factory = sqlite3.Row
  cur = con.cursor()
  cur.execute("""
          SELECT symbol, name, sector, industry, weight
          FROM sp500
          ORDER BY name
              """)
  rows = cur.fetchall(); 
  return render_template('index.html',rows = rows)



#Set up connection to Alpaca
api = tradeapi.REST(config.API_KEY, config.SECRET_KEY, base_url=config.API_URL)

#If insufficient cash error is thrown, check if there are any open orders left
open_orders = api.list_orders(
  status='open'
)
print(open_orders)

#Cancel all existing orders to avoid insufficient cash error
api.cancel_all_orders()

#If needed: Current positions
portfolio = api.list_positions()
print(portfolio)


#print(etf)

#Check buying power
account = api.get_account()
cash = round(float(account.buying_power), 2)
print(f"My buying power is {cash}")

def buy(data):
    for row in data:
      minimuminvestment = row['minimuminvestment']
      #remove $ sign, then turn string to float
      minString = minimuminvestment[1:]
      notional = float(minString)
      symbol = row['symbol']

      api.submit_order(
        symbol=symbol,
        notional=notional,
        side='buy',
        type='market',
        time_in_force='day')
      print((f"Submitted order for {symbol} for ${notional}"))
    return


#Let's treat this as the buy function - what would it look like?
@site.route('/data', methods=['POST']) 
def parse_request(): 
    data = request.get_json()
    print(data)
    buy(data)
    return jsonify(success=True)

site.run(host='0.0.0.0', port=8080)
