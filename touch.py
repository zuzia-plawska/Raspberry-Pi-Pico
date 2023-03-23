from machine import Pin
import time

touch_pad = Pin(18, Pin.IN, Pin.PULL_DOWN)

led = Pin('LED', Pin.OUT)

while True:
    if touch_pad.value():
        print('Touched')
        led.toggle()
        time.sleep(0.5)