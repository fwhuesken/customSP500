from flask import Flask, render_template, request, jsonify, url_for, redirect
import trade
import sqlite3

site = Flask(__name__)

@site.route('/')

def index():
   con = sqlite3.connect('app.db')
   con.row_factory = sqlite3.Row
   
   cur = con.cursor()
   cur.execute("SELECT symbol, name FROM stock ORDER BY symbol")
   
   rows = cur.fetchall(); 
   return render_template('index.html',rows = rows)
    

site.run(host='0.0.0.0', port=8080)



