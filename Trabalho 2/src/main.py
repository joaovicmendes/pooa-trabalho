import sys
from importer import Fetch

f = Fetch()
documento = f.site_content('http://g1.globo.com')
print(documento.prettify())