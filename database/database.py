import sqlite3

#Would be used if I didn't have sp500.py which creates a table straight from the csv

#Connecting to a newly created (if not already existing) sql database
connection = sqlite3.connect('app.db')

#Cursor object contains execute function to  execute sql queries
cursor = connection.cursor()
# """contains sql queries"""
# IF NOT EXISTS prevents duplicated tables


cursor.execute("""
    CREATE TABLE IF NOT EXISTS sp500 (
     symbol TEXT NOT NULL UNIQUE,
     name TEXT NOT NULL,
     sector TEXT,
     weight REAL
  )
""")

connection.commit()