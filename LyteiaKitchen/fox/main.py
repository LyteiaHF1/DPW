'''
Lyteia Kitchen
Lab 4
5/14/14
'''
import webapp2
from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
