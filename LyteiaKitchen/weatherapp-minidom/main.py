'''
Lyte
5/19/13
Lecture 5
'''
import webapp2
from page import *
import urllib2
from xml.dom import minidom
class MainHandler(webapp2.RequestHandler):
    def get(self):
        #setting up basic page
        view = FormPage()
        view.form_header = "Weather App"
        self.response.write(view.print_out())

        if self.request.GET:
           code = self.request.GET['code']
           url = 'http://xml.weather.yahoo.com/forecastrss?p=' + code
           req = urllib2.Request(url)
           opener = urllib2.build_opener()
           data = opener.open(req)

           #Parse xml
           xmldoc = minidom.parse(data)
           self.response.write(xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue)

           content = '<br/>'
           list = xmldoc.getElementsByTagName('yweather:forecast')
           for l in list:
               content += l.attributes['day'].value
               content += " HIGH: " + l.attributes['high'].value
               content += " LOW: " + l.attributes['low'].value
               content += " CONDITION: " + l.attributes['text'].value
               content += ' <img src="images/' + l.attributes['code'].value + '.png" width="50"/>'
               content += '<br/>'

           self.response.write(content)






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
