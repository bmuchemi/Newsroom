from app import app
import urllib.request,json
from .models import sources

Sources = sources.Sources


# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_data():
    '''
    Function that gets the json response to our url request
    '''
    get_data_url = 'https://newsapi.org/v2/sources?language=en&apiKey={}'.format(api_key)

    with urllib.request.urlopen(get_data_url) as url:
        get_data_data = url.read()
        get_data_response = json.loads(get_data_data)

        data_results = None

        if get_data_response['sources']:
            data_results_list = get_data_response['sources']
            data_results = process_results(data_results_list)

    return data_results


def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

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

        if name:
            news_object = Sources(id,name,description)
            data_results.append(news_object)


    return data_results

def get_movie(id):
    get_news_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            name = news_details_response.get('name')
            description = news_details_response.get('description')
        
            news_object = Sources(id,name,description)

    return news_object