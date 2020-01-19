from machine import ADC
#模拟口
adc = ADC(0)	#模拟口A0
print('receive ADC0...')
vin = adc.read()