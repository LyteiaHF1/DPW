'''
Lyteia Kitchen
5/7/2014
Simple Form
Lab 2
'''
import webapp2
from page import Form
# aritcles i read to help with this assignment
#http://dev.fyicenter.com/Interview-Questions/Python/How_to_make_Forms_in_python_.html
#http://learnpythonthehardway.org/book/ex51.html
    '''
        this one was very helpful
    '''
class MainHandler(webapp2.RequestHandler):
	def get(self):
		if self.request.GET:
			#Sting variable to populate form values on page
			relationship = ''
			#Try prevent checkbox errors
			try:
                # If the person did check the 'relationship1' checkbox
				relationship_type = self.request.GET['relationship1']
				if relationship_type:
					relationship = relationship + relationship_type + ' '
			except StandardError:
				pass
			#Try prevent checkbox errors
			try:
                # Set relationship equal to itself checkbox if checked
				# If checkbox is checked
				if relationship_type2:
					relationship = relationship + relationship_type2
			#If they check neither box no error will happen
			except StandardError:
				pass
			info_results = self.request.GET['first_name'] + ' ' + self.request.GET['last_name'] + ' ' + self.request.GET['phone_type'] + ' ' + self.request.GET['phone_number'] + ' ' + relationship

			#Creates Form Object
			form = Form(self)
			#Puts user info on new form Page
			self.response.write(form.print_contents(info_results))
		else:
			#Creates Form Object
			form = Form(self)
			#fillsthe form for the user to input it's information
			self.response.write(form.print_contents())


app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)