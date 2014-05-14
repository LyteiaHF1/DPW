
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
        gfruit.price =  1.26#$
        gfruit.need = 1 #bag
        gfruit.img ="http://upload.wikimedia.org/wikipedia/commons/2/28/US_Navy_010924-N-0063S-501_USS_Bataan_%28LHD_5%29.jpg"

        #Protein Powder Instance

        proteinp = List()
        proteinp.name = 'Protein Powder'
        proteinp.price = 15 #$
        proteinp.need = 1 #Container
        proteinp.img = "http://upload.wikimedia.org/wikipedia/commons/2/28/US_Navy_010924-N-0063S-501_USS_Bataan_%28LHD_5%29.jpg"

        #Whole Wheat Bread Instance

        wwb = List()
        wwb.name = 'Whole Wheat Bread'
        wwb.price = 1.50 #$
        wwb.need = 2 #loaf
        wwb.img ="http://upload.wikimedia.org/wikipedia/commons/2/28/US_Navy_010924-N-0063S-501_USS_Bataan_%28LHD_5%29.jpg"

        #Eggs Instance

        eggs = List()
        eggs.name = 'Eggs'
        eggs.price = 1 #$
        eggs.need = 1 #carton
        eggs.img ="http://upload.wikimedia.org/wikipedia/commons/2/28/US_Navy_010924-N-0063S-501_USS_Bataan_%28LHD_5%29.jpg"

         #Water Instance

        water = List()
        water.name = 'Water'
        water.price =  5 #$
        water.need = 1 #cases 24 pack
        water.img ="http://upload.wikimedia.org/wikipedia/commons/2/28/US_Navy_010924-N-0063S-501_USS_Bataan_%28LHD_5%29.jpg"

       
#Objects
class List(object):
    def __init__(self):
        self.name = ''
        self.__price = 0
        self.__need = 0
        self.img = ''

    #Getter for price
    @property
    def price(self):
        return self.__price


    #Setter for price
    @price.setter
    def price(self, v):
        self.__price = v

    #Getter for need
    @property
    def need(self):
        return self.__need

    #Setter for need
    @need.setter
    def need(self, v):
        self.__need = v












app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
