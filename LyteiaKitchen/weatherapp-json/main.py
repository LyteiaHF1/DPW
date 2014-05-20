'''
Lyte
5/19/13
Lecture 5
'''
import webapp2
from page import *
import urllib2
import json
class MainHandler(webapp2.RequestHandler):
    def get(self):
        #setting up basic page
        view = FormPage()
        view.form_header = "Weather App"
        self.response.write(view.print_out())

        if self.request.GET:
           code = self.request.GET['code']
           url = 'http://api.openweathermap.org/data/2.5/weather?q=' + code
           req = urllib2.Request(url)
           opener = urllib2.build_opener()
           data = opener.open(req)

           #Parse
           jsondoc = json.load(data)
           content = jsondoc['main']['tempt']
           view.page_content = " Temp is in Kelvins: " +str(content)
           view.page_content += "<br/>Temp In Farenheit: " + str(1.8*(content-273)+32)



           self.response.write(content)






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
