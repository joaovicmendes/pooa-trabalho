class Metadata:
    '''
        Classe que representa a abstração dos metadados de um determinado site de notícias
    '''
    def __init__(self, URL, parameters):
        self.URL = URL
        self.parameters = parameters

class MetadataRetrieve:
    def __init__(self, base_dir='./metadata/', extension='.txt'):
        self.base_dir = base_dir
        self.extension = extension

    def get(self, website_name):
        '''
            Retorna um objeto do tipo Metadata() do site informado em 'website_name'
        '''
        # Caminho até o arquivo
        file_name = self.base_dir + website_name + self.extension

        try:
            fp = open(file_name, 'r')
        except OSError:
            print("Erro ao abrir arquivo")
            exit()

        # Recuperando a URL do site
        URL = fp.readline()[:-1]
        
        # Recuperando quais as tags HTML/CSS devem ser utilizadas no site em questão
        line = fp.readline()[:-1]
        parameters = []
        while line:
            strategy, arguments = line.split(' ', 1)
            parameters.append([strategy, arguments])
            line = fp.readline()[:-1]

        fp.close()

        return Metadata(URL, parameters)
