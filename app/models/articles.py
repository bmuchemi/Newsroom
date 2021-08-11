class Articles:
    '''
    Articles class to define articles Objects
    '''

    def __init__(self,id,name,author,title,description,url,urlToImage,publishedAt,content):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.title = title
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
        self.author = author
       