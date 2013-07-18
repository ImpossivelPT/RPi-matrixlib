import json
import requests

session = requests.session()
req = session.get('http://graph.facebook.com/metacriacoes')

jsonFacebook = json.loads(req.content)

print jsonFacebook['likes']

