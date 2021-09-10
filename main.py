from flask import Flask, render_template, request, jsonify, url_for, redirect
import trade

site = Flask(__name__)

@site.route('/')
def index():
    return render_template('index.html')

site.run(host='0.0.0.0', port=8080)



