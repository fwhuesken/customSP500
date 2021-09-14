from flask import Flask, render_template, request, jsonify, url_for, redirect

import sqlite3

site = Flask(__name__)

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
                ORDER BY symbol
                    """)
  else:
        cur.execute("""
                SELECT symbol, name
                FROM nasdaq100 
                ORDER BY symbol
                """)

  
  rows = cur.fetchall(); 
  return render_template('index.html',rows = rows)
    

site.run(host='0.0.0.0', port=8080)



