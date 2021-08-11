from app import app
import urllib.request,json
from .models import sources,articles

Sources = sources.Sources
Articles = articles.Articles

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_data():
    '''
    Function that gets the json response to our url request
    '''
    get_data_url = f'https://newsapi.org/v2/sources?language=en&apiKey={api_key}'

    with urllib.request.urlopen(get_data_url) as url:
        get_data_data = url.read()
        get_data_response = json.loads(get_data_data)

        data_results = None

        if get_data_response.get('sources'):
            data_results_list = get_data_response.get('sources')
            data_results = process_results(data_results_list)

    return data_results
    
def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        data_results: A list of  objects
    '''
    data_results = []

    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')

        if name:
            news_object = Sources(id,name,description,url)
            data_results.append(news_object)


    return data_results

def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results

def process_articles(articles_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        data_results: A list of  objects
    '''
    news_results = []

    for articles_item in articles_list:
        id = articles_item.get('id')
        name = articles_item.get('name')
        description = articles_item.get('description')
        url = articles_item.get('url')
        title = articles_item.get('title')
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')
        content = articles_item.get('content')



        if id:
            articles_object = Sources(id,name,description,url,title,urlToImage,publishedAt,content)
            news_results.append(articles_object)


    return news_results
