import unittest
from models import sources
Sources = sources.Sources

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('bbc-news','BBC News')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

    def test_init(self):
        '''
        confirms that the object is instantiated correctly
        '''
        self.new_source.id = 'bbc-news'
        self.new_source.name='BBC News'


if __name__ == '__main__':
    unittest.main()
