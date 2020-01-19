# -*- coding: utf-8 -*-

import urequests as req
import ujson

apiurl = 'http://api.openweathermap.org/data/2.5/weather',
url= 'Babu',
key = 'bf1b626f3ed6c480088d28d9a053e358'


#http://api.openweathermap.org/data/2.5/weather?q=Babu&APPID=bf1b626f3ed6c480088d28d9a053e358

r = req.get(apiURL)
obj = ujson.loads(r.text)

city = obj['name']
icon = obj['weather'][0]['icon']
temp = int(obj['main']['temp'] - 273.15)
humid = obj['main']['humidity']
    

'''
{
	"coord": {
		"lon": 104.89,
		"lat": 23.23
	},
	"weather": [{
		"id": 803,
		"main": "Clouds",
		"description": "broken clouds",
		"icon": "04n"
	}],
	"base": "stations",
	"main": {
		"temp": 298.78,
		"pressure": 869.52,
		"humidity": 73,
		"temp_min": 298.78,
		"temp_max": 298.78,
		"sea_level": 1010.32,
		"grnd_level": 869.52
	},
	"wind": {
		"speed": 1.12,
		"deg": 174.505
	},
	"clouds": {
		"all": 76
	},
	"dt": 1530794146,
	"sys": {
		"message": 0.0061,
		"country": "CN",
		"sunrise": 1530742771,
		"sunset": 1530791431
	},
	"id": 1801374,
	"name": "Babu",
	"cod": 200
}
'''