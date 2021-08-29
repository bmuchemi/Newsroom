import unittest
from app.models import Headlines

class SourcesTest(unittest.TestCase):
    '''
    '''
    def setUp(self):
        '''
        '''
        self.top_article = Headlines('bbc-news','https://www.google.com/img','https://www.google.com')

    def test_source(self):
        '''
        test for creation of a new instance
        '''
        self.assertTrue(isinstance(self.top_article, Headlines))

    def test_init(self):
        '''
        '''
        self.top_article.title = 'bbc-news'
        self.top_article.url_to_image='https://www.google.com/img'
        self.top_article.url='https://www.google.com'
