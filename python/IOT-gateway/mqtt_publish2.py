#Hardware Platform: FireBeetle-ESP32
#Result: input MQTTlibrary and remote controls LED by mqtt communication.

from umqtt.simple import MQTTClient
from machine import Pin
import network
import time
#import dht
from machine import Pin
#d = dht.DHT11(Pin(16))
#d.measure()

SSID="7-1004（2）"
PASSWORD="HJ898516"

#----------Pin out ----------
led = Pin(2,Pin.OUT)
#----------------------------
SERVER = "mq.tlink.io"
#SERVER = "47.106.19.238"
CLIENT_ID = "20289C362YL3OV93"
TOPIC = b"20289C362YL3OV93"
username='MQTT'
password='MQTTPW'
#up_temp1 ="{\"sens9VQ34XM6W266U811orDatas\":[{\"sensorsId\":200169992,\"value\":80}]}"
#up_temp1 = "{\"sensorDatas\":[{\"sensorsId\":200281021,\"value\":" + str(d.temperature()) +  "}]}"up_humi = "{"sensorDatas":[{"sensorsId":200281021,"flag":"1","value":10.0}]}"
#d.humidity()
print(up_temp1)
print(type(up_temp1))

def connectWifi(ssid,passwd):
  global wlan
  wlan=network.WLAN(network.STA_IF)         #create a wlan object
  wlan.active(True)                         #Activate the network interface
  wlan.disconnect()                         #Disconnect the last connected WiFi
  wlan.connect(ssid,passwd)                 #connect wifi
  while(wlan.ifconfig()[0]=='0.0.0.0'):
    time.sleep(2)

    
#Catch exceptions,stop program if interrupted accidentally in the 'try'
try:
  connectWifi(SSID,PASSWORD)
  server=SERVER
  c = MQTTClient(CLIENT_ID,server,1883,username,password)    #create a mqtt client
  c.connect()                               #connect mqtt
  print("Before MQTT Publish......")
  c.publish(TOPIC,up_temp2,retain=True)            #client publish to a topic
  print("MQTT Published......")
finally:
  print('11111')  if(c is not None):
    c.disconnect()
  wlan.disconnect()
  wlan.active(False)




