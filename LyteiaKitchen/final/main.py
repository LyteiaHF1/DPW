'''
Lyteia Kitchen
Final
May 30,2014
'''
import webapp2
import urllib2
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        view = Page()
        #self.response.write(view.)


class ApiModel(object):
 ''' This class is where i get the api info setup '''
    def __init__(self):
            self.__url = "http://rebeccacarroll.com/api/got/got.xml"
            self.__request = urllib2.Request(self.__url)
            self.opener = urllib2.buildopener()
            self.__xmldoc.getElementsByTagName()[].firstChild.nodeValue



class ApiData(object):
 ''' This class is to hold the data switihched between modee and view  '''
    def __init__(self):
    #empty array for data
        self.house = []

class ApiView(object):
 ''' This class is what the user sees '''
    def __init__(self):
    #to hold content
        self.__content = '''

        '''


class Page(object):
    def __init__(self):
        self._open = '''
<!DOCTYPE>
    <html>
        <head>
         <title>Final | DPW May2014</title>
        </head>
        <body>
            '''
        self._body = "<h2>Filler Content</h2>"


        self._footer = '''
    </body>
 </html>
        '''
     def return_page(self):
        return self._open + self._body + self._footer


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
