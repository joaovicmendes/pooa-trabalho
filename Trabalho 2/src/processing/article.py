class Article:
    def __init__(self, title, url):
        self._title = title
        self._url = url

    def title(self):
        return self._title

    def url(self):
        return self._url
