import pyfirmata
import time
port = 'COM3'
board = pyfirmata.Arduino(port)
led = board.get_pin('d:3:o')
tSensor = board.get_pin('a:0:i')

it = pyfirmata.util.Iterator(board)
it.start()

while (True) :
    temprature = tSensor.read()
    print(temprature)

#while True :
#    board.digital[3].write(1)
#    time.sleep(1)
#    board.digital[3].write(0)
#    time.sleep(1)
