# -*- coding: utf-8 -*-

import requests as req


apiURL='{url}?humi={value1}&temp={value2}'.format(
url = 'http://192.168.0.102:80',
value1 = '22',
value2 = '33'
)

r = req.get(apiURL)


