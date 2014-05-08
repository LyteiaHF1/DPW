'''
Lyteia Kitchen
5/7/2014
Simple Form
Lab 2
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
