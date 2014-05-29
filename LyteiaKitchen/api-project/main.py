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

        #If Statement for if something is in the url
        if self.request.GET:
			#Get info in url
			prep = self.request.GET['prep']
			#Sends ingredient into model
			model = ApiModel(prep)
			#Tells model to send into and get the data
			model.send()


class ApiModel(object):
	'''  This model handles fetching, parsing and sorting data from the api '''

	def __init__(self, prep):
	    #api url where the ifo is
		self.__url = 'http://www.recipepuppy.com/api/?q='
		#setup for api request
		self.__request = urllib2.Request(self.__url + prep)
		#building the opener
		self.__opener = urllib2.build_opener()
    #send function
	def send(self):
		self.__result = self.__opener.open(self.__request)
		self.sort()


    def sort(self):
        #parse Json
        self.__json_data = json.load(self.__result)
        self.__array = []
        #array to put data in

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
