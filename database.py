import sqlite3

#Connecting to a newly created (if not already existing) sql database
connection = sqlite3.connect('app.db')

#Cursor object contains execute function to  execute sql queries
cursor = connection.cursor()
# """contains sql queries"""
# IF NOT EXISTS prevents duplicated tables
cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock (
        id INTEGER PRIMARY KEY, 
        symbol TEXT NOT NULL UNIQUE, 
        name TEXT NOT NULL,
        exchange TEXT NOT NULL
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock_price (
        id INTEGER PRIMARY KEY, 
        stock_id INTEGER,
        date NOT NULL,
        open NOT NULL, 
        high NOT NULL, 
        low NOT NULL, 
        close NOT NULL, 
        volume NOT NULL,
        FOREIGN KEY (stock_id) REFERENCES stock (id)
    )
""")
cursor.execute("""
        CREATE TABLE IF NOT EXISTS stock_price_minute (
        id INTEGER PRIMARY KEY,
        stock_id INTEGER,
        datetime NOT NULL,
        open NOT NULL,
        high NOT NULL,
        low NOT NULL,
        close NOT NULL,
        volume NOT NULL,
        FOREIGN KEY (stock_id) REFERENCES stock (id)
        )
    """)


#Create table containing all strategies
cursor.execute("""
    CREATE TABLE IF NOT EXISTS strategy (
    id INTEGER PRIMARY KEY,
    name NOT NULL
    )
    """)

#Create table containing stock_strategy
cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock_strategy(
    stock_id INTEGER NOT NULL,
    strategy_ID INTEGER NOT NULL,
    FOREIGN KEY (stock_id) REFERENCES stock (id),
    FOREIGN KEY (strategy_id) REFERENCES strategy (id)
    )
    """)

#Creating records of strategies
strategies = ['opening_range_breakout', 'opening_range_breakdown']

for strategy in strategies:
    cursor.execute("""
    INSERT INTO strategy (name) values (?)
    """, (strategy,))

connection.commit()