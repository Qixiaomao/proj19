#Hardware Platform: FireBeetle-ESP32
#Result: input MQTTlibrary and remote controls LED by mqtt communication.

from umqtt.simple import MQTTClient
from machine import Pin
import network
import time

SSID="FAST_B0F8"
PASSWORD="ly13977025398"

led=Pin(2, Pin.OUT, value=0)

SERVER = "mq.tlink.io"
#SERVER = "47.106.19.238"
CLIENT_ID = "20289C362YL3OV93"
TOPIC = b"20289C362YL3OV93"
username='MQTT'
password='MQTTPW'
up_temp1 ="{"sensorDatas":[{"sensorsId":200281021,"flag":"1","value":10.0}]}"

#----------Pin out ----------
led = Pin(2,Pin.OUT)
#----------------------------

def connectWifi(ssid,passwd):	#(1)连接WIFI热点
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
  c = MQTTClient(CLIENT_ID,server,1883,username,password)    #create a mqtt client（2）建立MQTTCLinet客户端对象
  c.connect()                               #connect mqtt (3)连接MQTT服务器
  print("Before MQTT Publish......")
  c.publish(TOPIC,up_temp1,retain=True)            #client publish to a topic  (4)发布主题消息
  print("MQTT Published......")
finally:
  if(c is not None):
    c.disconnect()
  wlan.disconnect()
  wlan.active(False)

