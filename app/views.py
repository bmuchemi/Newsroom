from .models import sources
from flask import render_template
from app import app
from .request import get_data,get_news

# Views
@app.route('/')
def index():
    '''
    View movie page function that returns the news details page and its data
    '''
    popular_articles = get_news()
    print(popular_articles)

    return render_template('index.html',articles= popular_articles)

    
   
@app.route('/news/id')
def news():

    '''
    View root page function that returns the index page and its data
    '''

    popular_news = get_data()
    print(popular_news)
    title = 'NEWSROOM'
    return render_template('index.html', title = title,popular=popular_news)
