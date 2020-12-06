from abc import ABC, abstractmethod

class SaveTo(ABC):
    @abstractmethod
    def execute(self, articles):
        pass

class SaveToStdOut(SaveTo):
    def execute(self, articles):
        for article in articles:
            print(article.title(), ': ', article.url())
