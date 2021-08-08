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
    get_data_url = base_url.format(api_key)

    with urllib.request.urlopen(get_data_url) as url:
        get_data_data = url.read()
        get_data_response = json.loads(get_data_data)

        data_results = None

        if get_data_response['results']:
            data_results_list = get_data_response['results']
            data_results = process_results(data_results_list)


    return data_results