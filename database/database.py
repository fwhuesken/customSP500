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
        name TEXT NOT NULL
    )
""")

#cursor.execute("""
  #  CREATE TABLE IF NOT EXISTS sp500 (
   #   symbol TEXT NOT NULL UNIQUE,
   #   name TEXT NOT NULL,
   #   sector TEXT
    #)
#""")

connection.commit()