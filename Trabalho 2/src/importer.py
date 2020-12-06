import requests 
from bs4 import BeautifulSoup

class Fetch:
    def site_content(self, URL):
        page = requests.get(URL)
        return BeautifulSoup(page.content, 'html.parser')
