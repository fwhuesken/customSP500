import sqlite3
import pandas as pd

# load data
df = pd.read_csv('etf/nasdaq100.csv')

# strip whitespace from headers
df.columns = df.columns.str.strip()

con = sqlite3.connect("app.db")

# drop data into database
name = 'nasdaq100'
df.to_sql(name, con)

con.commit()

# to remove the characters .csv from a string:
#newString = oldString.replace(".csv", "")