'''
Lyteia Kitchen
Final
May 30,2014
'''
import webapp2
import urllib2
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')



class Page(object):
    def __init__(self):
        self._open = '''
<!DOCTYPE>
    <html>
        <title>Final | DPW May2014</title>
       

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
