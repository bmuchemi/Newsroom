from flask import render_template
from app import app
from .request import get_data

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    popular_news = get_data()
    print(popular_news)
    title = 'Home - Welcome to The best News API'
    return render_template('index.html', title = title,popular=popular_news)