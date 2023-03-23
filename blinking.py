from machine import Pin
import utime 

leds = [Pin(i, Pin.OUT) for i in [2,3,6]]

if __name__ == '__main__':
    while True:
        for n in range(0,3):
            leds[n].value(1)
            utime.sleep_ms(50)
        for n in range(0,3):
            leds[n].value(0)
            utime.sleep_ms(50)