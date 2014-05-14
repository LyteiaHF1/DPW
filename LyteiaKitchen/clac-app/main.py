
import webapp2
#gets page.py
from page import Page


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #import page
        page = Page()
        #Grape Fruit Instance

        gfruit = List()
        gfruit.name = 'Grape Fruit'
        gfruit.price = 180 #$
        gfruit.need = 2 #pairs
        gfruit.img ="http://upload.wikimedia.org/wikipedia/en/3/37/Jumpman_logo.svg"

        




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
