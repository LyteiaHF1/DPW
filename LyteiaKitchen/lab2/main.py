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
            try:
				# If the person did check the 'relationship1' checkbox
				if relationship_type:

					relationship = relationship + relationship_type + ' '
			# If they check neither box no error will happen
			except StandardError:
				pass


app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)