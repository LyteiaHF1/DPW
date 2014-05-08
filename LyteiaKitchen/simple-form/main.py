'''
Lyteia Kitchen
5/7/2014
Lecture Day 2
'''
import webapp2 #importing additional code handles going to a browser
from page import Page

#Master Class (Where it begins)
class MainHandler(webapp2.RequestHandler):

#unique to framework
#this function runs 1st catalyst

    def get(self):
    #start writing code here, the next line is a placeholder
        if self.request.GET:

            info = self.request.GET["firstname"] + " " + self.request.GET["lastname"]
            page = Page(self) #creates a Page Object
            self.response.write(page.print_contents(info))
            # self.response.write(head+info+ender)
        else:
            page = Page(self) #creates a Page Object
            x = page.print_contents()
            self.response.write(x)
            # self.response.write(head+body+form+ender)

#associates class with framework
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
