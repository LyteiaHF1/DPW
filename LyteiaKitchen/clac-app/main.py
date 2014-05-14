
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
        gfruit.img ="http://upload.wikimedia.org/wikipedia/commons/2/28/US_Navy_010924-N-0063S-501_USS_Bataan_%28LHD_5%29.jpg"

        #Protein Powder Instance

        proteinp = List()
        proteinp.name = 'Protein Powder'
        proteinp.price = 220 #$
        proteinp.need = 1 #pairs
        proteinp.img = "http://upload.wikimedia.org/wikipedia/commons/2/28/US_Navy_010924-N-0063S-501_USS_Bataan_%28LHD_5%29.jpg"

        #Whole Wheat Bread Instance

        wwb = List()
        wwb.name = 'Whole Wheat Bread'
        wwb.price = 220 #$
        wwb.need = 1 #pairs
        wwb.img ="http://upload.wikimedia.org/wikipedia/commons/2/28/US_Navy_010924-N-0063S-501_USS_Bataan_%28LHD_5%29.jpg"

        






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
