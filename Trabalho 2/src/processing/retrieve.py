from abc import ABC, abstractmethod
from .article import Article

# Classe Abstrata para usar padrão Strategy
class Retrieve(ABC):
    @abstractmethod
    def get(self, page_content):
        pass

# Estratégia de busca para o site G1
class RetrieveG1(Retrieve):
    def get(self, page_content):
        '''
            Retorna as notícias em 'page_content' do site G1. Retorna uma lista de objetos 'Article'.
        '''
        ret = []
        articles = page_content.select('a.feed-post-link')

        for article in articles:
            title = article.string
            url = article['href']
            ret.append(Article(title, url))

        return ret

# Estratégia de busca para o site UOL
class RetrieveUol(Retrieve):
    def get(self, page_content):
        '''
            Retorna as notícias em 'page_content' do site UOL. Retorna uma lista de objetos 'Article'.
        '''
        ret = []
        articles = page_content.find_all('div', class_='thumbnails-wrapper')
        
        for article in articles:
            title = article.find('h3').string
            url = article.find('a')['href']
            ret.append(Article(title, url))

        return ret

class RetrieveEstadao(Retrieve):
    def get(self, page_content):
        '''
            Retorna as notícias em 'page_content' do site Estadão. Retorna uma lista de objetos 'Article'.
        '''
        ret = []
        articles = page_content.find_all('li', class_='share-more-container')
        
        for article in articles:
            title = article['data-title']
            url = article['data-url']
            ret.append(Article(title, url))

        return ret

class RetrieveFolha(Retrieve):
    def get(self, page_content):
        '''
            Retorna as notícias em 'page_content' do site Folha de S. Paulo. Retorna uma lista de objetos 'Article'.
        '''
        ret = []
        articles = page_content.find_all('div', class_='c-headline__content')
        
        for article in articles:
            title = article.find('h2', class_="c-headline__title")
            if title is not None:
                title = title.string.strip()
            else:
                continue
            url = article.find('a', class_="c-headline__url")
            if url is not None:
                url = url['href']
            else:
                continue
            ret.append(Article(title, url))

        return ret