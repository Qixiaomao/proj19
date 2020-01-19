#Hardware Platform: FireBeetle-ESP32
#Result: input MQTTlibrary and remote controls LED by mqtt communication.

from umqtt.simple import MQTTClient
from machine import Pin
import network
import time
import ujson

SSID="Huawei"
PASSWORD="12345678"

led=Pin(2, Pin.OUT, value=0)

SERVER = "47.106.19.238"
CLIENT_ID = "2O78E783Q8I9NU1H"
TOPIC = b"2O78E783Q8I9NU1H"
username='MQTT'
password='MQTTPW'
state = 0
c=None
def sub_cb(topic, msg):
  global state
  print((topic, msg))
    
def connectWifi(ssid,passwd): #(1)连接WIFI热点
  global wlan
  wlan=network.WLAN(network.STA_IF)         #create a wlan object
  wlan.active(True)                         #Activate the network interface
  wlan.disconnect()                         #Disconnect the last connected WiFi
  wlan.connect(ssid,passwd)                 #connect wifi
  while(wlan.ifconfig()[0]=='0.0.0.0'):
    time.sleep(1)

    
#Catch exceptions,stop program if interrupted accidentally in the 'try'
try:
  connectWifi(SSID,PASSWORD)
  server=SERVER
  c = MQTTClient(CLIENT_ID, server,1883,username,password)     #create a mqtt client（2）建立MQTTClient客户端对象
  c.set_callback(sub_cb)                    #set callback  （3）设定接收MQTT信息的回调函数
  c.connect()                               #connect mqtt  （4）连接MQTT服务器
  c.subscribe(TOPIC)                        #client subscribes to a topic （5）订阅主题
  print("Connected to %s, subscribed to %s topic" % (server, TOPIC))

  while True:
    c.wait_msg()                            #wait message （6）检查MQTT消息
finally:
  if(c is not None):
    c.disconnect()
  wlan.disconnect()
  wlan.active(False)
