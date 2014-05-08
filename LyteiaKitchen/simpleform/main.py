'''
Lyteia Kitchen
5/7/2014
Simple Form
Lab 2
'''

import webapp2
from page import Page

class MainHandler(webapp2.RequestHandler):

    def get(self):
        '''
        if form has been entered try the urgent_info form field, if it has been entered, change the value to a string
        if it does not exist, create a different string
         create a concatenated string to pass into a new Form instance print method
         otherwise call the default print method of the Form class for default results
        '''
        if self.request.GET:

            try:
                urgent_updates = self.request.GET["urgent_info"]
                if urgent_updates:
                    urgent_updates = "- You will also receive updates."
            except StandardError:
                urgent_updates = "- You <em>will not</em> receive any updates."

            form_fields = ("<div id='confirm'><p>" +self.request.GET["first_name"] + " " + self.request.GET["last_name"] + "<br>"
                + self.request.GET["address"] + "<br>"
                + self.request.GET["city"] + ", " + self.request.GET["state"] + " " + self.request.GET["zipcode"] + "</p><p>"
                + "<a href='mailto:" + self.request.GET["email"] + "'>" + self.request.GET["email"] + "</a><br>"
                + urgent_updates + "</p></div>")
            page = Page(self)
            self.response.write(page.print_form_results(form_fields))

        else:
            page = Page(self)
            base = page.print_form_results()
            self.response.write(base)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

