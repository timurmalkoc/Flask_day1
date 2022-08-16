from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favorite')
def favorite():
    fav = ['art','soccer','travel','cooking','reading']
    return render_template('favorite.html', fav=fav)
