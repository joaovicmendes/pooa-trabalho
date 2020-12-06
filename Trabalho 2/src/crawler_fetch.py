import requests 
from bs4 import BeautifulSoup

class Fetch:
    def site_content(self, URL):
        ''' 
            Retorna objeto do tipo BeautifulSoup() contendo o código HTML do site indicado por 'URL'
        '''
        page = requests.get(URL)
        return BeautifulSoup(page.content, 'html.parser')
