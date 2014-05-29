'''
Lyteia
Api Project
May 19,2013
'''
import webapp2
from page import *
import urllib2
import json
#from xml.dom import minidom
'''  API Using http://www.recipepuppy.com/ Easiest api to use '''
class MainHandler(webapp2.RequestHandler):
    def get(self):
        #setting up basic page
        view = FormPage()
        view.form_header = ""
        self.response.write(view.print_out())

    

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
