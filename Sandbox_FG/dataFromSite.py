import requests
#import BeautifulSoup

session = requests.session()
req = session.get('http://internos.metacriacoes.com/testes/ledmatrix/json/matrix.json')

#doc = BeautifulSoup.BeautifulSoup(req.content)

print req.content