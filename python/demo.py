# -*- coding: utf-8 -*-

import sys
import socket
import machine
import time
import dht, socket
import urequests as req
from machine import Pin, Timer

d = dht.DHT11(Pin(13))
running = True


def sendDHT11(t):
    global  running
    apiURL='http://192.168.43.63/store?'

    try:
        d.measure()
    except OSError as e:
        print(e)
        return
    
    apiURL+='&temp={temp}&humid={humid}'.format(
        temp = d.temperature(),
        humid = d.humidity()
    )

    r = req.get(apiURL)

    if r.status_code != 200:
        t.deinit()
        print('Bad request error.')
        running = False
    else:
        print('Data saved, id: ', r.text)

tim = Timer(-1)
tim.init(period=5000, mode=Timer.PERIODIC, callback=sendDHT11)

try:
    while running:
        pass
except:
    tim.deinit()
    print('stopped')

