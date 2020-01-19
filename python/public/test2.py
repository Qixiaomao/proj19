#coding:utf-8

import cherrypy
import string
import random
import pandas as pd
import csv
import sqlite3
import matplotlib.pyplot as plt
import matplotlib
import os

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
     return "hhhhh"   
    
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
    
    @cherrypy.expose
    def mat(self):
        

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot([1,2,3])
        fig.savefig('./public/test.png')
        
        return """<html>
                   <body>
            <form method="get" action="generate">
              <img src="./static/test.png" alt="Smiley face" width="600" height="720">
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
   