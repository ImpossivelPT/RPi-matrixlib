import matrixLib
import requests
from time import sleep
import json


while True:  # This constructs an infinite loop
    session = requests.session()
    req = session.get('http://graph.facebook.com/metacriacoes')
    
    jsonFacebook = json.loads(req.content)
    
    print jsonFacebook['likes']
    
    matrixLib.drawString('Likes: ' + str(jsonFacebook['likes']))

    sleep(1)
    
    
    
    
    

# reset pins
GPIO.cleanup()

# fim do programa
print "Fim"





