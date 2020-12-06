import requests 
from bs4 import BeautifulSoup

class Fetch:
    @staticmethod
    def site_content(url):
        ''' 
            Retorna objeto do tipo BeautifulSoup() contendo o código HTML do site indicado por 'url'
        '''
        page = requests.get(url)
        return BeautifulSoup(page.content, 'html.parser')
