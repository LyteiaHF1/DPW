'''
Lyteia Kitchen
4/12/14
Lab 3
'''
import webapp2
#gets page.py
from page import Page
class MainHandler(webapp2.RequestHandler):
    def get(self):
        #this is getting the class page
        page = Page()

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
