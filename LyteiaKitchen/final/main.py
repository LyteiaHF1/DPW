'''
Lyteia Kitchen
Final
May 30,2014
'''
import webapp2
import urllib2
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        view = Page()


class ApiModel(object):
 ''' This class is where i get the api info setup '''
    def __init__(self):
        self.__url = "http://rebeccacarroll.com/api/got/got.xml"
        self.__request = urllib2.Request(self.__url)
        self.opener = urllib2.buildopener()
        


class ApiData(object):
    def __init__(self):
        pass

class ApiView(object):
    def __init__(self):
        pass


class Page(object):
    def __init__(self):
        self._open = '''
<!DOCTYPE>
    <html>
        <head>
         <title>Final | DPW May2014</title>
        </head>
        <body>
            '''
        self._body = "<h2>Filler Content</h2>"


        self._footer = '''
    </body>
 </html>
        '''


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
