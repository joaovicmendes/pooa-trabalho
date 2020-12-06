import sys
from crawler_fetch import Fetch
from crawler_processing import Process

fetcher = Fetch()
documento = fetcher.site_content('http://g1.globo.com')

processor = Process(documento, ['a.feed-post-link'])
noticias = processor.filter()
for noticia in noticias:
    print(noticia.string)