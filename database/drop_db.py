import sqlite3
connection = sqlite3.connect('app.db')
    
cursor = connection.cursor()
#cursor.execute("""
 #   DROP TABLE stock
#""")

cursor.execute("""
    DROP TABLE sp500
""")

#cursor.execute("""
#    DROP TABLE nasdaq100
#""")

connection.commit()