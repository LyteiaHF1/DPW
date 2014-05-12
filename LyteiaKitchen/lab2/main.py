'''
Lyteia Kitchen
5/7/2014
Simple Form
Lab 2
'''
import webapp2
from page import Form

class MainHandler(webapp2.RequestHandler):
	def get(self):
		if self.request.GET:


app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)