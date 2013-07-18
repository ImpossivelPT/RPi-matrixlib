import requests
#import BeautifulSoup

r = requests.get('http://internos.metacriacoes.com/testes/ledmatrix/json/matrix.json')
json = r.json()
print json["matrix"]