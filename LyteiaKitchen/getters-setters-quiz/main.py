'''
Lyteia Kitchen
Getters and Setters Quiz
May 21,2014
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Counter() #instance of the counter class

        if self.request.GET:

            counter += 1#should add 1 each time its clicked
        else:
            counter = 0

        p.count = counter

        self.response.write(p.update())


#Logs is saying ERROR IndentationError: expected an indented block for line 13
class Counter(object):
    def __init__(self):
        self.__count = 0
        self.open = """
<!DOCTYPE html>
<html>
    <head>
        <title>Count UP</title>
    </head>
    <body>
        """
        self.content = """

        {self.count}
        """
        '''number should have changed ! didnt populate '''
        self.__button = """
        <a href=?count=button>Count Up</a>
        """
        self.close = """
    </body>
</html>
        """

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, c):
        self.__count = c

    @property
    def button(self):
        return self.__button

    @button.setter
    def button(self, b):
        self.__button = b

    def update(self):
        return self.open + self.content + self.button + self.close


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
