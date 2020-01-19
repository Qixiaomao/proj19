

# This file is executed on every boot (including wake-boot from deepsleep)

#import esp

#esp.osdebug(None)

import gc

import os

import network

#import webrepl

#webrepl.start()

gc.collect()

sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
  print('connecting to network...')
  sta_if.active(True)
  #sta_if.connect('Huawei', 'yellow1981')
  #sta_if.connect('nubia', 'yellowlmf1234')
  #sta_if.connect('Tenda_63BEE8','15151616')
  sta_if.connect('iPhone','12345678')
  while not sta_if.isconnected():

    pass
print('network config:', sta_if.ifconfig())



