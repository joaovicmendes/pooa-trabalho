from abc import ABC, abstractmethod

# Classe abstrata para usar o padrão Strategy
class SaveTo(ABC):
    @abstractmethod
    def execute(self, articles):
        pass

# Implementação para a saída padrão
class SaveToStdOut(SaveTo):
    def execute(self, articles):
        for article in articles:
            print(article.title(), ': ', article.url())

# Implementação para escrever em arquivo CSV usando ';' como separador
class SaveToCSV(SaveTo):
    def execute(self, articles):
        try:
            fp = open('./output.csv', 'w')
        except:
            print("Não conseguiu criar o arquivo output.csv")
            exit()
        
        fp.write('Titulo;URL\n')
        for article in articles:
            fp.write(article.title() + ';' + article.url() + '\n')
        
        fp.close()
