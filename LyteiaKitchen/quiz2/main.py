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

        self.__type = 'Denim Wings'
        self._debut = '2011'
        self.__style = 'winged'
        self.condition = 'Deadstock'
