from flask import Flask, render_template, request, jsonify, url_for, redirect
import sqlite3

site = Flask(__name__)

@site.route('/', methods=['GET', 'POST'])
def index():
  con = sqlite3.connect('app.db')
  con.row_factory = sqlite3.Row
  cur = con.cursor()
  cur.execute("""
          SELECT symbol, name, sector, weight
          FROM sp500
          ORDER BY name
              """)
  rows = cur.fetchall(); 
  return render_template('index.html',rows = rows)

@site.route('/data', methods=['POST']) 
def parse_request(): 
    data = request.get_json()
    print(data)
    return jsonify(success=True)

site.run(host='0.0.0.0', port=8080)

