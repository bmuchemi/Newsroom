import unittest
from app.models import Sources

class SourcesTest(unittest.TestCase):
    '''
    '''
    def setUp(self):
        '''
        '''
        self.new_source = Sources('bbc-news','BBC News')

    def test_source(self):
        '''
        test for creation of a new instance
        '''
        self.assertTrue(isinstance(self.new_source, Sources))

    def test_init(self):
        '''
        '''
        self.new_source.id = 'bbc-news'
        self.new_source.name='BBC News'
