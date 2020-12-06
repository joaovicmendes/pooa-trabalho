import sys
from crawler_fetch import Fetch
from crawler_processing import Process
from crawler_metadata import Metadata, MetadataRetrieve

# Objetos auxiliares
mdata_retrieve = MetadataRetrieve()
fetch = Fetch()

# Recuperando argumentos para o programa
website_name = sys.argv[1]
# export_method = sys.argv[2]

# Recuperando metadados do site desejado
metadata = mdata_retrieve.get(website_name)

# Buscando página principal
website_content = fetch.site_content(metadata.URL)

# Processando os dados para extrair notícias
process = Process(website_content, metadata.parameters)
list = process.get_all()

for item in list:
    print(item.string)
