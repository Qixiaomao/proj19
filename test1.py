import random
import string

import cherrypy


class StringHumi(object):
    @cherrypy.expose
    def index(self):
        return "hello cccccccc"
    
    @cherrypy.expose
    def humi(self, length = 8):
        return ''.join(random.sample(string.hexdigits,int(length)))
    
    @cherrypy.expose
    def temp(self, length = 8):
        return ''.join(random.sample(string.hexdigits,int(length)))
    
if __name__ == '__main__':
        cherrypy.quickstart(StringHumi())    