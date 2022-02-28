from machine import ADC 
from machine import Pin

class Button():
    def __init__(self, pin):
        self.switchpin = Pin(pin, Pin.IN)


    def state(self):
        return self.switchpin.value()