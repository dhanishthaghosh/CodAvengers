from flask import render_template, url_for
from web import app, db
from web.models import Hotel


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html', title='Index Page')

@app.route('/hotels')
def hotels():
    hotels = Hotel.query.all()
    return render_template('hotels.html', title='Hotels', hotels=hotels)



