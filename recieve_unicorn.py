from microbit import *
import radio

pin0.set_analog_period(20)
pin0.set_analog_period(20)

def backward(N):
    pin0.write_analog(10)
    pin1.write_analog(100)
    sleep(N)
    
def forward(N):
    pin0.write_analog(100)
    pin1.write_analog(10)
    sleep(N)

def turnRight(N):
    pin0.write_analog(100)
    pin1.write_analog(100)
    sleep(N)

def turnLeft(N):
    pin0.write_analog(10)
    pin1.write_analog(10)
    sleep(N)
    
def stopIt(N):
    pin0.write_analog(0)
    pin1.write_analog(0)
    sleep(N)

radio.on()

while True:
    incoming = radio.receive()
    if incoming == 'fwd': 
        forward(100)
    if incoming == 'bwd': 
        backward(100)
    if incoming == 'tl': 
        turnLeft(100)
    if incoming == 'tr': 
        turnRight(100)
    if incoming == 'stp': 
        stopIt(1000)

