from machine import Pin
import time
import dht

#数字口

def run():
   print('dht module demo')
   gpio_dht = Pin(16)  #D2口
   d = dht.DHT21(gpio_dht)
   led = Pin(2, Pin.OUT)
   while 1:
      led.value(1)
      d.measure()
      temperature = d.temperature()
      humidity = d.humidity()
      print('Temperature: ' + str(temperature) + ' Celsius')
      print('Humidity: ' + str(humidity) + ' % RH')
      led.value(0)
      time.sleep(2)

