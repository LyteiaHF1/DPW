'''
Lyteia Kitchen
Lab 4
5/14/14
'''
import webapp2
from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #Instantiate Page class, this contains the html.
        page = Page()

class Animal(object):
	def __init__(self):
		self.name = ""
		self.phylum = ""
		self.animal_class = ""
		self.order = ""
		self.family = ""
		self.genus = ""
		self.image = ""
		self.lifespan = ""
		self.habitat = ""
		self.geolocation = ""
		self.__sound = ""


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
