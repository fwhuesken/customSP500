import sqlite3
import pandas as pd

# load data
df = pd.read_csv('etf/sp500.csv')

# strip whitespace from headers
df.columns = df.columns.str.strip()

con = sqlite3.connect("app.db")

# drop data into database
df.to_sql('sp500', con)

con.commit()