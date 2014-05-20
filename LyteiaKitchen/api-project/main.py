'''
Lyteia
Api Project
May 19,2013
'''
import webapp2
from page import *
import urllib2
from xml.dom import minidom
class MainHandler(webapp2.RequestHandler):
    def get(self):
        #setting up basic page
        view = FormPage()
        view.form_header = ""
        self.response.write(view.print_out())

        if self.request.GET:
           code = self.request.GET['code']
           url = 'http://production.shippingapis.com/ShippingAPITest.dll?API=TrackV2&XML=' + code
           req = urllib2.Request(url)
           opener = urllib2.build_opener()
           data = opener.open(req)

           #Parse xml
           xmldoc = minidom.parse(data)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
