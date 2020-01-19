# -*- coding: utf-8 -*-

import cherrypy
import string
import random
import pandas as pd
import csv
import sqlite3
import matplotlib.pyplot as plt
import matplotlib
import os
import numpy as np

matplotlib.use('Agg')






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
     return "Linking successful!"   
    
    @cherrypy.expose
    def generate(self, humi,temp):
        #fieldnames = ['id','note','payout','profit']
        id = 0
        idt = 0
        
        print(humi)
        print(temp)
        conn = sqlite3.connect('humi.db')

        c = conn.cursor()
        print('Opened the database successful!!')
        c.execute('insert into htdb values(?,?,?,?)',[id,humi,idt,temp])
     
        
        
        conn.commit()
        print('Create the record successful!')
        conn.close()
        return ''.join(random.sample(string.hexdigits, 8))
    
    @cherrypy.expose
    def mat(self):
        ht_arr_list = []
        conn = sqlite3.connect('humi.db')
        c = conn.cursor()
        sql = c.execute('SELECT HUMI, TEMP from htdb')
        

        #Travesting the row
        for row in sql:
            #print ("HUMI = ", row[0])
            #print ("NAME = ", row[1])
            
            ht_arr_list.append(row[0])
            ht_arr_list.append(row[1])
        
        print(ht_arr_list)
        #W = H - T + C(150)
        z = ht_arr_list[0]-ht_arr_list[1]+150    
        fig = plt.figure(1)

        
        # fname 为 SimHei.ttf 字体的路径
        zhfont1 = matplotlib.font_manager.FontProperties(fname="C:\Windows\Fonts\SimHei.ttf") 
        plt.title('温湿度表',fontproperties=zhfont1)
        plt.xlabel('时间/小时',fontproperties=zhfont1)
        plt.ylabel('数值/°/%RH',fontproperties=zhfont1)
        #ax = fig.add_subplot(111)
        #plt.plot(ht_arr_list[0])
        #plt.plot(ht_arr_list[1])
        #plt.plot(z)
        
        
        hour = np.arange(1,13)
        plt.plot(hour,[87.7,86.7,86.7,86.7,86.7,86.3,86.6,86.7,86.5,86.7,86.5,86.4],c='red')
        plt.plot(hour,[24.4,24.7,24.6,24.9,24.7,24.7,24.8,24.6,24.9,24.6,24.5,24.6],c='blue')
        
        h = np.arange(1,7)
        plt.title('灌溉量表',fontproperties=zhfont1)
        plt.xlabel('时间/小时',fontproperties=zhfont1)
        plt.ylabel('数值/mm',fontproperties=zhfont1)
        plt.plot(h,[210,211,212,213,214,215],c='yellow')
        
        fig.savefig('./public/test.png')
        
        return """<html>
                   <body>
            <form method="get" action="generate">
              <img src="./static/test.png" alt="Smiley face" width="800" height="600">
            </form>
          </body>
        </html>"""
    


if __name__ == '__main__':
    #cherrypy.config.update({'server.socket_host':'172.20.10.13','server.socket_port':80,})
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(humi(),'/', conf)
   