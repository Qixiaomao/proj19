import sys
import socket
import machine
from machine import ADC
import time
import network
from machine import Pin



adc = ADC(0)
SSID='KAI'
PASSWORD='LCK12345678'
wlan=None
s=None



#----------Pin out ----------
led = Pin(2,Pin.OUT)
#----------------------------

def connectWifi(SSID,PASSWORD):
  global wlan
  wlan=network.WLAN(network,STA_IF)
  wlan.active(True)
  wlan.disconnect()
  wlan.connect(SSID,PASSWORD)
  while(wlan.ifconfig()[0]=='0.0.0.0'):
    time.sleep(1)
  return True

#捕抓异常，若有异常就停止运行
try:
  connectWifi(SSID,PASSWORD)
  ip=wlan.ifconfig()[0]
  s = socket.socket()
  s.setcockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
  s.connect((host,port))
  s.send('kkkkkkkkkkkkkkkkkkkkkkk')
  while True:
    data = s.recv(1024)
    if(len(data) == 0):
      print('close socket')
      s.close()
      break
    print(data)
    ret = s.send(data)
except:
  if(s):
    s.close()
  wlan.disconnect()
  wlan.active(False)

def adcSocket():
  # 创建一个TCP的socket对象
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  #host = "tcp.tlink.io" # IP-address of the TCP server of NodeMCU
  host = "tcp.tlink.io"	#（2）指定UDP服务器地址和端口号
  port = 8647
 # s.connect((host, port)) 
  s = socket.socket()
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#（3）设置TCP连接的默认参数 
  
  '''
  socket.SOL_SOCKET表示正在使用socket选项
 当socket关闭后，本地端用于该socket的端口号立刻就可以被重用。通常来说，
 只有经过系统定义一段时间后，才能被重用。
 1表示表示将SO_REUSEADDR标记为TRUE，操作系统会在服务器socket被关闭或
 服务器进程终止后马上释放该服务器的端口，否则操作系统会保留几分钟该端口。
 
 学习地址，socket网络服务器
 https://www.jb51.net/article/50858.htm
 '''
				
  s.connect((host,port)) #(4)通过ip地址和端口进行连接 TCP 服务器
  s.send("4K3JO39UUO142322") #第一次连接后，需要发送序列号，仅一次即可
  time.sleep(2)  #延时2S

  i=10 #发送十次
  while(i>0):
    print(i)
    i-=1
    lux = adc.read()
    print(lux)    
    lux="#"+str(lux)+"#" #组合出上送的数据标签
    s.send(lux)
    print(lux)
    time.sleep(2) #延时10S 
    '''
    while True:
      data = s.recv(1024)
      if(len(data) == 0):
        print("close socket")
        s.close()
        break
      print(data)
      ret = s.send(data)
    '''  



