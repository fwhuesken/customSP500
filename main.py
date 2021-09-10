#Import FastAPI class
import sqlite3, config
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
#from flask import Flask, render_template, request, jsonify, url_for, redirect
#import trade

#site = Flask(__name__)

#@site.route('/')
#def index():
   # return render_template('index.html')

#site.run(host='0.0.0.0', port=8080)

#We're creating an API to fetch data from our database, which is populated by the Alpaca API



#Creating an instance of a FastAPI application 
app = FastAPI()
#Configuring a templates directory
templates = Jinja2Templates(directory="templates")

#All requests to this base route ("/") will get routed to the function below (def index():)
#Whatever response this function returns will be returned to the browser
#Styling of the return is provided by index.html in the templates directory
@app.get("/") 
def index(request: Request):
    #Variable to adjust sql query based on filter. False as second parameter is default - when you first come to the page no filter is selected, so filter is false
    stock_filter = request.query_params.get('filter', False)
    
    connection = sqlite3.connect('app.db')
    
    #row_factory method turns standard python tuple (which needs to be accessed by row[index number]) into a more useful object
    connection.row_factory = sqlite3.Row
 
    #Function to use connection
    cursor = connection.cursor()
    
    if stock_filter == 'new_closing_highs':
        cursor.execute("""
                SELECT * FROM (
                    SELECT symbol, name, stock_id, max(close), date
                    FROM stock_price JOIN stock ON stock.id=stock_price.stock_id
                    GROUP BY stock_id
                    ORDER BY symbol
                    ) WHERE date = (SELECT max(date) FROM stock_price)
                    """)
    else:
        cursor.execute("""
                    SELECT id, symbol, name
                    FROM stock 
                    ORDER BY symbol
                    """)

    rows = cursor.fetchall()
    return templates.TemplateResponse("index.html", {"request": request, "stocks": rows})

