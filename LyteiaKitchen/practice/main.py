import webapp2
import urllib2
from xml.dom import minidom


class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = FormPage()
        page.inputs = {'search':'text', 'Submit': 'submit'}
        page.create_inputs()
        self.response.write(page.print_out("Enter First and Last Name"))

        if self.request.GET:#if there is info in the url
            search = self.request.GET['search']
            url = "https://api.fullcontact.com/v2/name.xml" #where the API is
            #step 1 assemble request
            request = urllib2.Request(url + search)#assembles request

            #2 use url lib2 to create an object to get the url
            opener = urllib2.build_opener()
            #3 use url to get result-request info from API

            result = opener.open(request)
            #print result
            #4 parse the result
            xmldoc = minidom.parse(result)
            self.response.write(xmldoc.getElementsByTagName('nameDetails')[2].firstChild.nodeValue)
            content = '<br/>'
            list = xmldoc.getElementsByTagName('givenName')
            for l in list:
                content += l.attributes['familyName'].value
                #content += "  Name: " + l.attributes['fullName'].value
                #content += "  Nickname: " + l.attributes['givenName'].value
                #content += "  CONDITION: " + l.attributes['text'].value
                #content += '  <img src="images/' + l.attributes['code'].value + '.png" width="50" />'
                #content += '  <img src="http://l.yimg.com/a/i/us/we/52/' + l.attributes['code'].value + '.gif" />'
                content += '<br />'
            self.response.write(content)




class Page(object):
      def __init__(self):
        self._head ='''
<!DOCTYPE>
<html>
    <head>
        <title></title>
    </head>
  <body>
        '''
        self._body = ''
        self._close = '''
    </body>
</html>'''

class FormPage(Page):
     def __init__(self):
        #run the init function
        #super for this class run its init function
        super(FormPage, self).__init__()

        self.__form_open = '<form method="GET">'
        self.__form_close = '</form>'
        self.__inputs = dict()
        self.__input_string = ""

     def create_inputs(self):
         for key, value in self.__inputs.iteritems():
            #print self.__inputs[i]
            #self input string for input type
            self.__input_string += '<input type="' + value+ '" name="' +key+ '" placeholder="' +key+'"/>'

     def print_out(self, msg):
        return self._head + msg + self.__form_open + self.__input_string + self.__form_close + self._close

     @property
     def inputs(self):
        pass

     @inputs.setter
     def inputs(self, dict):
        self.__inputs = dict




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
