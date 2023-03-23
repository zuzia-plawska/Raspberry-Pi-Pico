from machine import Pin
import time 

led = Pin('LED', Pin.OUT) #create LED object from Pin13, set Pin13 to output

#while True:
led.toggle()      
   # time.sleep(0.5)
   