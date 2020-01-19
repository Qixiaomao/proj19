
import dht
import machine
import urequests
import urequests as req
import network
import time
from machine import Pin



#setting the inite
d = dht.DHT22(machine.Pin(4))

#PASSWORD="15151616"
SSID="zte_331"
PASSWORD="123456789"
wlan=None
s=None


#----------Pin out ----------
led = Pin(2,Pin.OUT)
#----------------------------

def connectWifi(SSID,PASSWORD):
  global wlan
  wlan=network.WLAN(network.STA_IF)
  print('connectWifi¡­¡­')
  wlan.active(True)
  wlan.disconnect()
  wlan.connect(SSID,PASSWORD)
  while(wlan.ifconfig()[0]=='0.0.0.0'):
    time.sleep(1)
  return True


def humi():
  while 1:
   d.measure()
   temperature = d.temperature()
   humidity = d.humidity()
   print('humidity:'+str(humidity)+' %RH')
   print('temperature:'+str(temperature)+'¡æ')
   time.sleep(2)  
 
''' 
def addSocket():
  #d.measure()
  #time.sleep(2)
  #temperature = d.temperature()
  #humidity = d.humidity()
  temp = '22'
  humi = '33'
#set the data 
  apiURL='{url}?humi={value1}&temp={value2}'.format(
  url = 'http://localhost:8080/generate',
  value1 = humi,
    value2 = temp
    )
  
  r = req.get(apiURL)
  #obj = ujson.loads(r.text)
'''
 
 
  
  
  
if __name__ == '__main__':
 
   connectWifi(SSID,PASSWORD)

   temp = '22'
   humi = '33'
   
   '''
   apiURL='{url}?humi={value1}&temp={value2}'.format(
     url = 'http://http://192.168.1.150:80/generate',
     value1 = humi,
     value2 = temp
      )
    '''
   apiURL='{url}?humi={value1}&temp={value2}'.format(
    url = 'http://192.168.1.150:80',
    value1 = humi,
    value2 = temp
   )  
    
   while True:
       time.sleep(5)
       r = req.get('http://192.168.1.150:80/generate?humi=22&temp=33')
