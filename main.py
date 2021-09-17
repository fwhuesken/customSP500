from flask import Flask, render_template, request, jsonify, url_for, redirect
from bs4 import BeautifulSoup
import sqlite3

site = Flask(__name__)


ticker='AAPL'

def get_price(ticker):
    page = request.get("https://finance.yahoo.com/quote/" + ticker)
    soup = BeautifulSoup(page.text, "html5lib")
    print('Hello World')
    price = soup.find('span', {'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text

    # remove thousands separator
    price = price.replace(",", "")
    
    return price

@site.route('/', methods=['GET', 'POST'])
def index():
  index = request.form.get('index', False)
  con = sqlite3.connect('app.db')
  con.row_factory = sqlite3.Row
   
  cur = con.cursor()
  if index == 'sp500':
        cur.execute("""
                SELECT symbol, name, sector
                FROM sp500
                ORDER BY name
                    """)
  elif index == 'nasdaq100':
        cur.execute("""
                SELECT
                  nasdaq100.symbol,
                  nasdaq100.name,
                  sector.sector
                FROM
                  nasdaq100 
                LEFT JOIN sector ON
                  sector.symbol = nasdaq100.symbol
                ORDER BY
                  nasdaq100.name
                """)
  elif index == 'fractionable':
        cur.execute("""
                SELECT
                  stock.symbol,
                  stock.name,
                  sector.sector
                FROM
                  stock 
                LEFT JOIN  sector ON
                  sector.symbol = stock.symbol
                ORDER BY
                  stock.name
                """)
  
  
  rows = cur.fetchall(); 
  return render_template('index.html',rows = rows)
    

site.run(host='0.0.0.0', port=8080)

get_price()
print(price)

