'''
Lyteia K
Lecture day 3 Review Classes
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
        yoda = Character()
        yoda.name = "Yoda"
        yoda.age = -5
        yoda.gender = "Male"
        yoda.occupation = "Jedi Master"
        yoda.print_info()
        #instance.attribute
        #instance.method()
        #instance.property

        luke = Character()
        luke.name = "Luke Skywalker"
        luke.age = 24
        luke.gender = "Male"
        luke.occupation = "Jedi Knight"
        luke.print_info()

        leia = Character()
        leia.name = "Leia Organa"
        leia.gender = "Female"
        leia.occupation = "Princess"
        leia.age = luke.age
        leia.squad_no = "Pink 5"
        print leia.squad_no



class Character(object):
    def __init__(self):#construtor function
        self.name = ""
        self.age = 0
        self.occupation = ""
        self.gender = ""
        self.__rouge_squadron_no = "DEFAULT"

    def print_info(self):
        print self.name+ " is a(n)" +self.occupation

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,new_age):
        if new_age <0 or new_age > 1000:
            print "Error"
        else:
            self.__age = new_age

    #PROVIDES READ ACCESS
    @property
    def squad_no(self):
        return self.__rouge_squadron_no

    @squad_no.setter
    def squad_no(self, new_no):
    #Validation
         if new_no == "Pink 5":
          new_no = "Red 5"
          #showing info - more code at once!
          print new_no
          self.__rouge_squadron_no = new_no




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
