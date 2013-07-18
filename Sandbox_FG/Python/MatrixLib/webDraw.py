#bibliotecas
import requests
from time import sleep
import matrixLib
import RPi.GPIO as GPIO

while True:  # This constructs an infinite loop
    
    # JSON 
    r = requests.get('http://spendyfox.com/sandbox/meta/ledmatrix/json/matrix.json')
    json = r.json()
    print json["matrix1"]
    # - fim JSON
    led1 = json["matrix1"]
    matrixLib.writeMatrix(led1,1)
    led2 = json["matrix2"]
    matrixLib.writeMatrix(led2,2)
    sleep(10)
    
    """
    string = 'META'
    string = list(string)
    finalString = ''
    
    for index in range(len(string)):
        finalString += Letras[string[index]] + ',' + space
        #finalString += ''.join(Letras[string[index]])
        #print type(Letras[string[index]])

    startWrite = [1,0,1,0,0,0,0,0,0,0]
    writeMatrixDS(startWrite,1)
    
    #apaga o ultimo char
    finalstring = finalString[:-1]
    
    finalArray = eval(finalString)
    injectoToMatrix(finalArray)
    """
   
    
    sleep(10)
    
    
    
    
    

# reset pins
GPIO.cleanup()

# fim do programa
print "Fim"