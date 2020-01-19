
import urequests
import urequests as req
import time
import network
import gc




SSID="zte_331"
PASSWORD="123456789"
wlan=None
s=None



def connectWifi(SSID,PASSWORD):
  global wlan
  wlan=network.WLAN(network.STA_IF)
  print('connectWifi……')
  wlan.active(True)
  wlan.disconnect()
  wlan.connect(SSID,PASSWORD)
  while(wlan.ifconfig()[0]=='0.0.0.0'):
    time.sleep(1)
  return True



 

 
 
  
  
if __name__ == '__main__':
 
   connectWifi(SSID,PASSWORD)
   #i = 100
   temp = '22'
   humi = '33'
   
   '''
   apiURL='{url}?humi={value1}&temp={value2}'.format(
     url = 'http://192.168.0.102:80/generate',
     value1 = humi,
     value2 = temp
      )
   '''
   i = 0
   
   #gc.collect()
   
   while (i<4):
    i += 1    
    r = req.get('http://jsonplaceholder.typicode.com/albums/1') 
    print(type(r))    
    gc.collect()
    
   r = req.get('http://jsonplaceholder.typicode.com/albums/1')  
   gc.collect()
    
     #r.close()
