import sqlite3
import alpaca_trade_api as tradeapi
import config

# Sets up connection to database
connection = sqlite3.connect('app.db')

# row_factory method turns standard python tuple (which needs to be accessed by row[index number]) into a more useful object
connection.row_factory = sqlite3.Row

# Function to use connection
cursor = connection.cursor()
cursor.execute("""
    SELECT symbol, name FROM stock
""")

rows = cursor.fetchall()
symbols = [row['symbol'] for row in rows]
#The above is called list comprehension and equal to
#symbols = []
#for row in rows:
#    symbols.append(row['symbol'])

api = tradeapi.REST(config.API_KEY, config.SECRET_KEY, base_url=config.API_URL) # or use ENV Vars shown below
assets = api.list_assets()

for asset in assets:
    #print(asset.name)
       #"INSERT INTO" specifies columns of stock to be populated"
       #VALUES (?, ?)" are placeholders.
       #"(asset.symbol, asset.name)" specifies columns of list_assets
    try:
        if asset.status == 'active' and asset.fractionable and asset.tradable and asset.symbol not in symbols:
            print(f"New symbol {asset.symbol} {asset.name}")
            cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES (?, ?, ?)", (asset.symbol, asset.name, asset.exchange))
    except Exception as e:
        print(asset.symbol)
        print(e)
    connection.commit()


connection.commit()