# -*- coding: utf-8 -*-

import requests as req
import json

apiURL='{url}?q={city}&APPID={key}'.format(
url = 'http://api.openweathermap.org/data/2.5/weather',
city = 'Babu,CN',
key = 'bf1b626f3ed6c480088d28d9a053e358'
)

r = req.get(apiURL)
obj = json.loads(r.text)


city = obj['name']
icon = obj['weather'][0]['icon']
humid = obj['main']['humidity']

del r