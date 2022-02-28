
from machine import PWM, Pin
import time 

#设置对应红、绿、蓝的三个GPIO管脚
led_red = PWM(Pin(5), freq = 1000)  
led_green = PWM(Pin(4), freq = 1000)
led_blue = PWM(Pin(0), freq = 1000)

#继电器的GPIO管脚
relaypin = Pin(16, Pin.OUT)#

#通过PWM的占空比设置颜色
def rgb_light(red, green, blue, brightness):
    pwm_red = led_red.duty(int(red/255*brightness*1023))
    pwm_green = led_green.duty(int(green/255*brightness*1023))
    pwm_blue = led_blue.duty(int(blue/255*brightness*1023))

rgb_light(255, 255, 0, 1.0)

#周期点亮、熄灭
while True:
    # relaypin.on()  # value: 1 but light is off
    relaypin.value(0)
    print('on: value: ' + str(relaypin.value()))
    time.sleep(2)
    relaypin.value(1)
    # relaypin.off() value: 0 but light is on
    print('off value: ' + str(relaypin.value()))
    time.sleep(2)