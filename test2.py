#coding:utf-8

import cherrypy
import string
import random
import pandas as pd
import csv
import sqlite3






#set the csv
File_name = 'Test.csv'
#number == 1
'''
Humi = {
    "H":"humi",
    "T":"temp",
}
'''


#send to the data of the class
class humi(object):
    @cherrypy.expose
    def index(self):
        return "hhhhhhhhh"
    
    @cherrypy.expose
    def generate(self, humi,temp):
        #fieldnames = ['id','note','payout','profit']
        
        print(humi)
        print(temp)
        conn = sqlite3.connect('humi.db')

        c = conn.cursor()
        print('Opened the database successful!!')
        c.execute('insert into htdb values(?,?)',(humi,temp))
        
        conn.commit()
        print('Create the record successful!')
        conn.close()
        
        return ''.join(random.sample(string.hexdigits, 8))
    



    
    

    

if __name__ == '__main__':
    #cherrypy.config.update({'server.socket_host':'172.20.10.13','server.socket_port':80,})
    cherrypy.quickstart(humi())
   