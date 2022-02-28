
from machine import ADC
from machine import Pin, Signal

class Relay():

    def __init__(self, pin):
        self.relaypin = Pin(pin, Pin.OUT)
        self.relayled = Signal(self.relaypin, invert=True) # 将信号置反, 实现开与关和输入信号对应
        #self.last_status = 1

    def set_state(self, state):
        self.relayled.value(state)
        #self.relaypin.value(state)
        #self.last_status = state

    def set_on(self):
        #self.relaypin.on() value: 1 but light is off
        self.relayled.value(1)
        print('Relay on value: ' + str(self.relayled.value()))
    
    def set_off(self):
        # self.relaypin.off() value: 0 but light is on
        self.relayled.value(0)
        print('Relay off value: ' + str(self.relayled.value()))
    
    def state(self):
        return self.relayled.value()