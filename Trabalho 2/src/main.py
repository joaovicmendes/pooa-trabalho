import sys

# Módulos locais
from fetch.fetch import Fetch
from processing.article import Article
from processing.processing import Process
from processing.retrieve import *
from export.export import Export
from export.save_to import *

supported_websites = {
    'g1': ('https://g1.globo.com', RetrieveG1()),
    'uol': ('https://noticias.uol.com.br/', RetrieveUol()),
    'estadao': ('https://estadao.com.br', RetrieveEstadao()),
    'folha': ('https://folha.uol.com.br', RetrieveFolha()),
}

supported_export_methods = {
    'stdout': SaveToStdOut(), 
    'csv': SaveToCSV()
}

def main():
    url, retrieve_strategy, export_strategy = eval_arguments(sys.argv)

    # Recuperando página principal do website
    website_content = Fetch.site_content(url)

    # Extraindo notícias da página obtida
    process = Process(website_content, retrieve_strategy)
    articles = process.get_all()

    export = Export(export_strategy)
    export.execute(articles)

def eval_arguments(argv):
    error_message = ""
    list_to_print = []

    # Filtrando arugmentos
    if len(sys.argv) < 2:
        erro_message = "Argumentos insuficientes. Tente:\n python main.py <site> [método de exportação]"
        error_exit(erro_message)
    elif len(sys.argv) == 2:
        website_name = sys.argv[1]
        export_name = 'stdout'
    else:
        website_name = sys.argv[1]
        export_name = sys.argv[2]

    # Recuperando a URL e estratégia adequada segundo argumento passado
    try:
        url, retrieve_strategy = supported_websites[website_name]
    except KeyError:
        error_message = ("Website '%s' não suportado.\n" % website_name) + "Disponíveis:"
        list_to_print = list(supported_websites.keys())
        error_exit(error_message, list_to_print)

    # Recuperando a estratégia de exportação adequada segundo argumento passado
    try:
        export_strategy = supported_export_methods[export_name]
    except KeyError:
        error_message += ("Método de exportação '%s' não suportado.\n" % export_name) + "Disponíveis:"
        list_to_print = list(supported_export_methods.keys())
        error_exit(error_message, list_to_print)

    return url, retrieve_strategy, export_strategy

def error_exit(message, list=[]):
    print(message)
    for value in list:
        print(" ", value)
    exit()

if __name__ == "__main__":
    main()
