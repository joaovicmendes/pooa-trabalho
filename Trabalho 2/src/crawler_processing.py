from bs4 import BeautifulSoup

class Process:
    def __init__(self, page_content, parameters):
        self.page_content = page_content
        self.parameters = parameters
        self.strategy = Retrieve()

    def get_all(self):
        '''
            Retorna todas as notícias contidas em 'page_content' utilizando as estratégias e seletores contidos em 'parameters'
        '''
        ret = []
        for strategy, arguments in self.parameters:
            if strategy == "SelectCSS":
                self.strategy = RetrieveSelectCSS()

            data = self.strategy.get(self.page_content, arguments)
            ret += data
        return ret

# Classe Abstrata para usar padrão Strategy
class Retrieve:
    def get(self, page_content, arguments):
        pass

# Estratégia de busca chamada 'SelectCSS'
class RetrieveSelectCSS(Retrieve):
    def get(self, page_content, arguments):
        '''
            Retorna as notícias em 'page_content' utilizando select css.\n
            Ex: a.minha_classe
        '''
        selector = arguments
        return page_content.select(selector)
