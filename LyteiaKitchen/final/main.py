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
        self.response.write('Hello world!')




class ApiData(object):
    pass

class ApiView(object):
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


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
