from bs4 import BeautifulSoup
from .retrieve import *

class Process:
    def __init__(self, page_content, strategy):
        self.page_content = page_content
        self._strategy = strategy

    def get_all(self):
        '''
            Retorna uma lista com as notícias contidas em 'page_content' como objetos do tipo 'Article'
        '''
        return self._strategy.get(self.page_content)
