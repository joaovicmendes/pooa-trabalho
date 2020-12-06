from bs4 import BeautifulSoup

class Process:
    def __init__(self, page_content, tags):
        self.page_content = page_content
        self.tags = tags
    
    def filter(self):
        result = []
        for tag in self.tags:
            result += self.page_content.select(tag)
        return result
