'''
Lyteia Kitchen
Getters and Setters Quiz
May 21,2014
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):



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
        self.__button = """
        <a href=?count=button>Count Up</a>
        """
        self.close = """
    </body>
</html>
        """

     


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
