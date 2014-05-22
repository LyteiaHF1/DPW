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
class MainHandler(webapp2.RequestHandler):
    def get(self):
        #setting up basic page
        view = FormPage()
        view.form_header = ""
        apiKey = 'dvx8Y0CHtVVGzv48v4qI3q8776KPFsYo'
        self.response.write(view.print_out())

        if self.request.GET:
           code = self.request.GET['code']

           url = "http://api.bigoven.com/recipes?pg=1&rpp=25&title_kw="+ code + "&api_key=" +apiKey

           req = urllib2.Request(url)
           opener = urllib2.build_opener()
           data = opener.open(req)

           #Parse xml
           jsondoc = json.load(data)
		   content = jsondoc['title']['']
           view.page_content = " Temp is in Kelvins: " +str(content)
           view.page_content += "<br/>Temp In Farenheit: " + str(1.8*(content-273)+32)



           self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
