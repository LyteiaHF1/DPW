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
		lion.image = 'http://upload.wikimedia.org/wikipedia/commons/7/73/Lion_waiting_in_Namibia.jpg'
		lion.lifespan = '15'
		lion.habitat = 'Tropical'
		lion.geolocation = 'Sub-Saharan Africa'
		lion.sound = 'Rawr'

		#Instantiate's Tiger subclass
		tiger = Tiger()
		#Assign Info to attributes from Tiger's superclass Animal
		tiger.name = 'Tiger'
		tiger.phylum = 'Chordata'
		tiger.animal_class = 'Mammalia'
		tiger.order = 'Carnivora'
		tiger.family = 'Felidae'
		tiger.genus = 'Panthera'
		tiger.image = 'http://upload.wikimedia.org/wikipedia/commons/archive/2/2f/20140122104305%21Tigress_at_Jim_Corbett_National_Park_.jpg'
		tiger.lifespan = '20-26 Years (In captivity)'
		tiger.habitat = 'Trees, Bushes, and Clumps of Tall Grass'
		tiger.geolocation = 'Southern Asia,China,Korea and Russia'
		tiger.sound = 'Chuff'

		#Instantiate's Giant Panda subclass
		panda = GiantPanda()
		panda.name = 'Giant Panda'
		panda.phylum = 'Chordata'
		panda.animal_class = 'Mammalia'
		panda.order = 'Carnivora'
		panda.family = 'Ursidae'
		panda.genus = 'Ailuropoda'
		panda.image = 'http://upload.wikimedia.org/wikipedia/commons/8/8a/Bai_yun_giant_panda.jpg'
		panda.lifespan = '20 Y (In Wild)'
		panda.habitat = ''
		panda.geolocation = 'Western China'
		panda.sound = 'Bleat'

		#Array to populate animal info
		animals = [lion, tiger, panda]
		self.response.write(page.header + page.body + page.footer)
		if self.request.GET:
			animal = (int(self.request.GET['animal']))-1
			self.response.write(self.html(animals[animal]))

	def html(self,obj):
	    result = '''
	    <div>
			<div id='img'>
			<img src="{obj.image}" height="350" width="500"/>
			</div>
			<div id ='txt'>
			<h1></h1>
			<ul>
				<li>Phylum: {obj.phylum}</li>
				<li>Class: {obj.animal_class}</li>
				<li>Order: {obj.order}</li>
				<li>Family: {obj.family}</li>
				<li>Genus: {obj.genus}</li>
				<li>Lifespan: {obj.lifespan}</li>
				<li>Habitat: {obj.habitat}</li>
				<li>Geolocation: {obj.geolocation}</li>
			</ul>
			<p>What does the {obj.name} say? <br> {obj.sound}</p>
			</div>
		</div>
		'''
		#Method format for big strings
		result = result.format(**locals())
		#Returns result to be put on screen
		return result


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

		@property
		def sound(self):
			return self.__sound

		@sound.setter
		def sound(self, specific_sound):
			self.__sound = specific_sound

class Lion(Animal):
	def __init__(self):
		super(Lion,self).__init__()

class Tiger(Animal):
	def __init__(self):
		super(Tiger,self).__init__()

class GiantPanda(Animal):
	def __init__(self):
		super(GiantPanda,self).__init__()

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
