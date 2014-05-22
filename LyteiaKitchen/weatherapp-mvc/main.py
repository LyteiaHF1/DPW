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
           wm = WeatherModel(code) #send code to the model
           wm.send() #tells model to send the info and get the data

           wv = WeatherView() #creates the view
           wv.do = wm.do #pass data from the model to the view
           self.response.write(wv.content)

class WeatherModel(object):
    '''
    This model handles fetching,parsing and sorting data from the weather api
    '''
    def __init__(self, code):
        #assembles the request, formatted very specifically

        self.__url = 'http://xml.weather.yahoo.com/forecastrss?p=' #where the API is
        self.__req = urllib2.Request(self.__url + code) #assemble the url request
        self.__opener = urllib2.build_opener() #use the urllib2 to create an object to get url


    def send(self):
        self.__result = self.__opener.open(self.__req) #use url to get a result - request info from the API
        self.sort() #call the method that sorts the xmldoc

    def sort(self):
        print "Sort function has ran"
        #parse the result

        self.__xmldoc = minidom.parse(self.__result)
        self.__do = WeatherData()
        self.__do.title = self.__xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue
        list = self.__xmldoc.getElementsByTagName('yweather:forecast')
        for l in list:
            # print l.attributes['day'].value
            self.__do.code = l.attributes['code'].value
            self.__do.day = l.attributes['day'].value
            self.__do.high = l.attributes['high'].value
            self.__do.low = l.attributes['low'].value
            self.__do.condition = l.attributes['text'].value
            self.__do.img = l.attributes['code'].value

    @property
    def do(self):
        return self.__do # returns data object with all of our delicious data

class WeatherData(object):
    '''
    This data object holds the data fetched by the model and shown by the view
    '''
    def __init__(self):
        self.title = ''
        self.day = ''
        self.high = ''
        self.low = ''
        self.code = ''
        self.condition = ''
        self.img = ''

class WeatherView(object):
    '''
    This class handles how the data is shown to the user
    '''
    def __init__(self):
        self.__do = WeatherData()

    def update(self): #updates the appearance of the view
        self.__content = '<h3>' + self.__do.title + '</h3>'

        self.__content += self.__do.day + ' : '
        self.__content += 'High: ' + self.__do.high
        self.__content += ' - Low: ' + self.__do.low
        self.__content += '  Condition: ' + self.__do.condition
        self.__content += ' <img src="images/' + self.__do.img + '.png" width="50"/>'
        #print self.__content

    @property
    def do(self):
        return self.__do

    @do.setter
    def do(self, new_do):
        self.__do = new_do
        #print "SETTER RUNS"
        #print self.do.title
        self.update()

    @property
    def content(self):
        return self.__content

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
