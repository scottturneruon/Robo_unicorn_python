from microbit import *
import radio

radio.on()

while True:
    radio.send("fwd")
    display.scroll("forward")
    radio.send("bwd")
    display.scroll("backward")
    radio.send("tl")
    display.scroll("Left")
    radio.send("tr")
    display.scroll("right")  
    radio.send("stp")
    display.scroll("stop")


