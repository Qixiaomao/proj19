from machine import Pin
import time

def run():
   led = Pin(2, Pin.OUT)
   button = Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
   button.value()
   while 1:
      led.value(1)
      time.sleep(2)
      led.value(0)
      time.sleep(2)