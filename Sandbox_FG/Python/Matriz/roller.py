# original: http://dangerousprototypes.com/2012/10/04/driving-4-8x8-led-matrices-via-the-ht1632c-and-an-arduino/

#bibliotecas
import RPi.GPIO as GPIO
from time import sleep
import requests

delay = 0

def dataON():
    GPIO.output(DISPLAY_WR, False)
    sleep(delay)
    GPIO.output(DISPLAY_DATA, True)
    print 1
    sleep(delay)
    GPIO.output(DISPLAY_WR, True)
    sleep(delay)
    
def dataOFF():
    GPIO.output(DISPLAY_WR, False)
    sleep(delay)
    GPIO.output(DISPLAY_DATA, False)
    print 0
    sleep(delay)
    GPIO.output(DISPLAY_WR, True)
    sleep(delay)
    
def writeMatrix(array,nMatrix):
    if nMatrix == 1:
        GPIO.output(DISPLAY_CS1, False)
    elif nMatrix == 2:
        GPIO.output(DISPLAY_CS2, False)

    for index in range(len(array)):
        if array[index] == 1:
            dataON()
        else:
            dataOFF()
            
    if nMatrix == 1:
        GPIO.output(DISPLAY_CS1, True)
    elif nMatrix == 2:
        GPIO.output(DISPLAY_CS2, True)

# dont stop    
def writeMatrixDS(array,nMatrix):
    if nMatrix == 1:
        GPIO.output(DISPLAY_CS1, False)
    elif nMatrix == 2:
        GPIO.output(DISPLAY_CS2, False)

    for index in range(len(array)):
        if array[index] == 1:
            dataON()
        else:
            dataOFF()
            
def injectoToMatrix(array):
    for index in range(len(array)):
        if array[index] == 1:
            dataON()
        else:
            dataOFF()
        
def matrixWriteMode(nMatrix):
    led = [1,0,1,0,0,0,0,0,0,0]
    writeMatrixDS(led,nMatrix)
    
    
def startMatrix(nMatrix):
    led = [1,0,0,0,0,0,0,0,0,0,1,0,0] # SYS EN
    writeMatrix(led,nMatrix)
    sleep(delay)
    led = [1,0,0,0,0,0,0,0,0,1,1,0,0] # LED ON
    writeMatrix(led,nMatrix)
    
    #led = [1,0,0,0,0,0,0,1,0,0,1,0,0] # BLINK ON
    #writeMatrix(led,nMatrix)
    
    #led = [1,0,0,0,0,0,0,1,0,0,0,0,0] # BLINK OFF
    #writeMatrix(led,nMatrix)
    
    #led = [1,0,0,1,0,1,0,1,1,1,1,0,0] # PWM 16/16
    #writeMatrix(led,nMatrix)

def drawString(string):
    clearMatrix(2)
    string = list(string)
    finalString = ''
    
    for index in range(len(string)):
        finalString += Letras[string[index]] + ',' + space
        #finalString += ''.join(Letras[string[index]])
        #print type(Letras[string[index]])
        
    #apaga o ultimo char
    finalstring = finalString[:-1]
    
    finalArray = eval(finalString)
    
    if(len(finalArray) >= 256):
    
        finalArray1 = finalArray[:256]
        finalArray2 = finalArray[256:512]
        
        startWrite = [1,0,1,0,0,0,0,0,0,0]
        writeMatrixDS(startWrite,1)
        writeMatrix(finalArray1,1)
        
        startWrite = [1,0,1,0,0,0,0,0,0,0]
        writeMatrixDS(startWrite,2)
        writeMatrix(finalArray2,2)
    else:
        finalArray = finalArray
        
        startWrite = [1,0,1,0,0,0,0,0,0,0]
        writeMatrixDS(startWrite,1)
        
        writeMatrix(finalArray,1)

def clearMatrix(nMatrix):
    clearArray = [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for index in range(1,nMatrix+1):
        writeMatrix(clearArray,index)
    
    """
    startWrite = [1,0,1,0,0,0,0,0,0,0]
    writeMatrixDS(startWrite,1)
    
    
    injectoToMatrix(finalArray)
    """

# define pins
DISPLAY_CS1     = 17
DISPLAY_CS2     = 4
DISPLAY_WR      = 27
DISPLAY_DATA    = 22

# pins BCM nao BOARD
GPIO.setmode(GPIO.BCM)


# pins
GPIO.setup(DISPLAY_CS1, GPIO.OUT)
GPIO.setup(DISPLAY_CS2, GPIO.OUT)
GPIO.setup(DISPLAY_WR, GPIO.OUT)
GPIO.setup(DISPLAY_DATA, GPIO.OUT)

#tudo a zero
GPIO.output(DISPLAY_WR, False)
GPIO.output(DISPLAY_DATA, False)
GPIO.output(DISPLAY_CS1, True)
GPIO.output(DISPLAY_CS2, True)



startMatrix(1)
startMatrix(2)










sleep(delay)
Letras = {}
Letras['A'] = '0,0,1,1,1,1,1,1,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,1,1,1,1,1'
Letras['B'] = '0,1,1,1,1,1,1,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,1,0,1,1,1,0'
Letras['C'] = '0,0,1,1,1,1,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0'
Letras['D'] = '0,1,1,1,1,1,1,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,1,1,1,1,0'
Letras['E'] = '0,1,1,1,1,1,1,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1'
Letras['F'] = '0,1,1,1,1,1,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0'
Letras['G'] = '0,0,1,1,1,1,1,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,1,1,1,0'
Letras['H'] = '0,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1'
Letras['I'] = '0,1,0,0,0,0,0,1,0,1,1,1,1,1,1,1,0,1,0,0,0,0,0,1'
Letras['J'] = '0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,0'
Letras['K'] = '0,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,1'
Letras['L'] = '0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1'
Letras['M'] = '0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1'
Letras['N'] = '0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,1'
Letras['O'] = '0,0,1,1,1,1,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,1,1,1,1,0'
Letras['P'] = '0,1,1,1,1,1,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0'
Letras['Q'] = '0,0,1,1,1,1,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,1,1,0,1'
Letras['R'] = '0,1,1,1,1,1,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,1,1,1,1'
Letras['S'] = '0,0,1,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,1,1,1,0'
Letras['T'] = '0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0'
Letras['U'] = '0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,0'
Letras['V'] = '0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,1,1,1,1,0,0,0'
Letras['W'] = '0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1'
Letras['X'] = '0,1,0,0,0,1,1,1,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,1'
Letras['Y'] = '0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0'
Letras['Z'] = '0,1,0,0,0,0,1,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,0,0,0,1,0,1,1,0,0,0,0,1'

Letras['a'] = '0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,0,1,1,1,1'
Letras['b'] = '0,1,1,1,1,1,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,1,1,0'
Letras['c'] = '0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1,0'
Letras['d'] = '0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,1,1,1,1,1,1,1'
Letras['e'] = '0,0,0,0,1,1,1,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,0,1,1,0,1'
Letras['f'] = '0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0'
Letras['g'] = '0,0,0,1,1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,1,1,1,1,0'
Letras['h'] = '0,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1'
Letras['i'] = '0,1,0,1,1,1,1,1'
Letras['j'] = '0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,1,1,1,0'
Letras['k'] = '0,1,1,1,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1'
Letras['l'] = '0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1'
Letras['m'] = '0,0,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1'
Letras['n'] = '0,0,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1'
Letras['o'] = '0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,1,1,0'
Letras['p'] = '0,0,1,1,1,1,1,1,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,1,0,0,0'
Letras['q'] = '0,0,0,1,1,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,1,1,1,1,1,1'
Letras['r'] = '0,0,0,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0'
Letras['s'] = '0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,1,0'
Letras['t'] = '0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1'
Letras['u'] = '0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1'
Letras['v'] = '0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,1,1,0,0'
Letras['w'] = '0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1'
Letras['x'] = '0,0,0,1,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1'
Letras['y'] = '0,0,1,1,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,1,1,1,1,1,0'
Letras['z'] = '0,0,0,1,0,0,0,1,0,0,0,1,0,0,1,1,0,0,0,1,0,1,0,1,0,0,0,1,1,0,0,1,0,0,0,1,0,0,0,1'

Letras['1'] = '0,0,1,0,0,0,0,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1'
Letras['2'] = '0,0,1,0,0,0,1,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,1,1,0,0,1,1'
Letras['3'] = '0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,1,1,0,1,1,0'
Letras['4'] = '0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,1,1,1'
Letras['5'] = '0,1,1,1,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,1,1,1,0'
Letras['6'] = '0,0,0,1,1,1,1,0,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,0,0,0,1,1,0'
Letras['7'] = '0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,0,0,0,0,1,1,1,0,0,0,0'
Letras['8'] = '0,0,1,1,0,1,1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,1,1,0,1,1,0'
Letras['9'] = '0,0,1,1,0,0,0,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0,0,1,1,1,1,0,0'
Letras['0'] = '0,0,1,1,1,1,1,0,0,1,0,0,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,0,0,0,1,0,0,1,1,1,1,1,0'


Letras[':'] = '0,0,0,1,0,0,1,0'
Letras[';'] = '0,0,0,1,0,0,1,1'
Letras['.'] = '0,0,0,0,0,0,0,1'
Letras[','] = '0,0,0,0,0,0,1,1'
Letras['-'] = '0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0'
Letras['/'] = '0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0'

Letras[' '] = '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'


space = '0,0,0,0,0,0,0,0,0'



while True:  # This constructs an infinite loop
    """
    # JSON 
    r = requests.get('http://spendyfox.com/sandbox/meta/ledmatrix/json/matrix.json')
    json = r.json()
    print json["matrix1"]
    # - fim JSON
    led1 = json["matrix1"]
    writeMatrix(led1,1)
    led2 = json["matrix2"]
    writeMatrix(led2,2)
    sleep(10)
    """
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
    
    drawString('Likes: ' + '749')
    
    
    sleep(500)
    
    
    
    
    

# reset pins
GPIO.cleanup()

# fim do programa
print "Fim"


