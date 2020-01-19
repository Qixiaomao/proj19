# -*- coding: utf-8 -*-

import sys
import socket
import machine
import time
import dht, socket
import urequests as req
from machine import Pin, Timer

d = dht.DHT22(Pin(13))
running = True


def sendDHT22(t):
    global  running
    #apiURL='http://192.168.1.109/store?'
    #apiURL='http://192.168.1.150/generate?'
    apiURL = 'http://192.168.0.101/generate?'

    try:
        d.measure()
    except OSError as e:
        print(e)
        return
    
    apiURL+='temp={temp}&humi={humi}'.format(
        temp = d.temperature(),
        humi = d.humidity()
    )
    print(apiURL)
    r = req.get(apiURL)


    if r.status_code != 200:
        t.deinit()
        print('Bad request error.')
        running = False
    else:
        print('Data saved, id: ', r.text)

tim = Timer(-1)
tim.init(period=5000, mode=Timer.PERIODIC, callback=sendDHT22)

try:
    print('start**********************')
    while running:
        pass
except:
    tim.deinit()
    print('stopped')



