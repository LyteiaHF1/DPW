'''
Lyteia Kitchen
Inheritance Quiz
May 19,2013
'''

#Abstract Class Sneaker
class Sneaker(object):
    def __init__(self):
        self._type = 'Balenciga'
        self.__debut = '2014'
        self.__color = 'White'

#Sub Class
class JeremyS(Sneaker):
    def __init__(self):
        super(JeremyS, self).__init__()

        self._type = 'JS Denim Wings'
        self.__debut = '2011'
        self.__style = 'winged'
        self.condition = 'Deadstock'


#Sub Class 2
class Jordan(Sneaker):
    def __init__(self):
        super(Jordan,self).__init__()

        self._type = "Air Jordan Banned Retro 1 "
        self.__debut = "1998"
        self.__style = "Retro 1 "
        self.condition = "Beaters"
