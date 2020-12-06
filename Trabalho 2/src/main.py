import sys

# Módulos locais
from fetch.fetch import Fetch
from processing.article import Article
from processing.processing import Process
from processing.retrieve import *

supported_websites = {
    'g1':  ( 'https://g1.globo.com', RetrieveG1() ),
    'uol': ( 'https://noticias.uol.com.br/',   RetrieveUol() ),
}

supported_export_methods = {
    # 'stdout': ExportStdOut(),
}

def main():
    url, retrieve_strategy, export_strategy = eval_arguments(sys.argv)

    # Recuperando página principal do website
    website_content = Fetch.site_content(url)

    # Extraindo notícias da página obtida
    process = Process(website_content, retrieve_strategy)
    articles = process.get_all()

    for article in articles:
        print(article.title())

def eval_arguments(argv):
    # Filtrando arugmentos
    if len(sys.argv) < 2:
        print("Argumentos insuficientes. Tente:")
        print(" python main.py <site> [método de exportação]")
        exit()
    elif len(sys.argv) == 2:
        website_name = sys.argv[1]
        export_name = 'stdout'
    else:
        website_name = sys.argv[1]
        export_name = sys.argv[2]

    try:
        url, retrieve_strategy = supported_websites[website_name]
    except KeyError:
        print("Website '%s' não suportado." % website_name)
        print("Disponíveis:")
        for key in supported_websites:
            print(key)
        exit()

    # try:
    #     export_strategy = supported_export_methods[export_name]
    # except KeyError:
    #     print("Método de exportação '%s' não suportado." % export_strategy)
    #     print("Disponíveis:")
    #     for key in super:
    #         print(key)
    #     exit()
    export_strategy = None

    return url, retrieve_strategy, export_strategy

if __name__ == "__main__":
    main()
