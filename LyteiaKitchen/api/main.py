

import webapp2
from htm import *
import urllib2
import json #library for working with xml

class MainHandler(webapp2.RequestHandler):
	def get(self):
		page = Page()

		self.response.write(page.head)
		if self.request.GET:
			self.response.write(page.nav)
			model = Model(self.request.GET['zip'])
			do = model.do
			page.tmp(do)
			self.response.write(page.ul)
		else:
			self.response.write(page.cta)
		self.response.write(page.foot)

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
