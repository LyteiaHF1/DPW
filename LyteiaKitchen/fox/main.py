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
        #Instantiate's Lion subclass
		lion = Lion()

		#Assign Info to attributes from Lion's superclass Animal
		lion.name = 'Lion'
		lion.phylum = 'Chordata'
		lion.animal_class = 'Mammalia'
		lion.order = 'Carnivora'
		lion.family = 'Felidea'
		lion.genus = 'Panthera'
		lion.image = ''
		lion.lifespan = '15 Years'
		lion.habitat = 'Tropical'
		lion.geolocation = 'Sub-Saharan Africa'
		lion.sound = 'Rawr'

		#Instantiate's Tiger subclass
		tiger = Tiger()
		tiger.name = 'Tiger'
		tiger.phylum = 'Chordata'
		tiger.animal_class = 'Mammalia'
		tiger.order = 'Carnivora'
		tiger.family = 'Felidae'
		tiger.genus = 'Panthera'
		tiger.image = ''
		tiger.lifespan = '20 – 26 Years (In captivity)'
		tiger.habitat = 'Trees, Bushes, and Clumps of Tall Grass.'
		tiger.geolocation = 'Southeast Asia, China, Korea and Russia'
		tiger.sound = 'Chuff'

		#Instantiate's Giant Panda subclass
		panda = Giantpanda()
		panda.name = ''
		panda.phylum = ''
		panda.animal_class = ''
		panda.order = ''
		panda.family = ''
		panda.genus = ''
		panda.image = ''
		panda.lifespan = ''
		panda.habitat = ''
		panda.geolocation = ''
		panda.sound = ''


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

class Lion(Animal):
	def __init__(self):
		super(Lion,self).__init__()

class Tiger(Animal):
	def __init__(self):
		super(Tiger,self).__init__()

class Giantpanda(Animal):
	def __init__(self):
		super(Giantpanda,self).__init__()
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
