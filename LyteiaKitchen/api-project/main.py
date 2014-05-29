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
			##Sends ingredient into model
			model = ApiModel(prep)
			#Tells model to send into and get the data
			model.send()
			#Creates View
			view = ApiView()
			#Passes data collected from model to view
			view.array = model.array
			#Puts info from array results on screen
			self.response.write(view.content)
			
			

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
		#parse json
		self.__json_data = json.load(self.__result)
		self.__array = []
		 #array to put data in
         #Loop the results
		for i in self.__json_data['results']:
			 #makes ApiData Class
			do = ApiData()
			do.title =  i['title']
			do.meats =  i['ingredients']
			do.href =  i['href']
			self.__array.append(do)

	@property
	def array(self):
		#Returns the data object __array which now contains all the data pulled
		return self.__array

class ApiData(object):
	'''  This holds the data gotten by the model and shown in the view '''
	def __init__(self):
		self.title = ''
		self.meats = ''
		self.href = ''

class ApiView(object):
	'''  This class handles what the user sees '''
	def __init__(self):
		#Sets array equal to the ApiData class
		self.__array = ApiData()

	#upadets
	def update(self, recipes):
		self.__content = ''
		for i in recipes:
			self.__array = i
			self.__content += "<div class ='container' class='container sixteen columns results'>"
			self.__content += '<h4>' + i.title + '</h4>'
			self.__content +=  '<li>ingredients: ' + i.meats + '</li>'
			self.__content += "<a href=" + i.href + ">Recipe</a>"
			self.__content += '</div>'

	@property
	def array(self):
		return self.__array

	@array.setter
	def array(self, new_array):
		self.update(new_array)
app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
