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
        #writes page
        page = Page()
        self.response.write(page.return_page())
        #instanuates model
        model = ApiModel()
        view = ApiView(view.house_data)#calls view
        self.response.write(view.content)#writes content



class ApiModel(object):
    def __init__(self):
    #def __init__(self):
        self.__url = "http://rebeccacarroll.com/api/got/got.xml"
        self.__request = urllib2.Request(self.__url)
        self.__opener = urllib2.build_opener()
        self.send()#call send function

    def send(self):
        self.__result = self.__opener.open(self.__request)#setting up result
        self.sort()#call sort function

    def sort(self):
    #pasre xml and store in variable
        self.__xmldoc = minidom.parse(self.__result)
        self.__house_data = ApiData()
        houses = self.__xmldoc.getElementsByTagName('house')
        for i in house:
            house_dict = dict()
            name = i.getElementsByTagName('name')[0].firstChild.nodeValue
            sigil = i.getElementsByTagName('sigil')[0].firstChild.nodeValue
            motto = i.getElementsByTagName('motto')[0].firstChild.nodeValue
            color1 = i.getElementsByTagName('color1')[0].firstChild.nodeValue
            color2 = i.getElementsByTagName('color2')[0].firstChild.nodeValue
            head = i.getElementsByTagName('head')[0].firstChild.nodeValue
            image = i.getElementsByTagName('image')[0].firstChild.nodeValue

            house_dict =[name,sigil,motto,color1,color2,head,image]
            self.__house_data_house.append(house_dict)
    @property
    def house_data(self):
        return self.__house_data



class ApiData(object):
    def __init__(self):
    #def __init__(self):
    #empty array for data
        self.house = []

class ApiView(object):
    def __init__(self, house_data):

    #def __init__(self, house_data):
    #to hold content
        self.__content = ''
        #loop here gets data from dictionary
        for i in house_data.house:
            self.__content +='<p> Name: ' +i[0]+ '</p>'
            self.__content +='<p> Sigil: ' +i[1]+ '</p>'
            self.__content +='<p> Motto: ' +i[2]+ '</p>'
            self.__content +='<p> Color1: ' +i[3]+ '</p>'
            self.__content +='<p> Color2: ' +i[4]+ '</p>'
            self.__content +='<p> Head: ' +i[5]+ '</p>'
            self.__content +='<p> image: ' +i[6]+ '</p>'

            #print i[0]
    @property
    def content(self):
        return self.__content

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
     #def return_page(self):
        return self._open + self._body + self._footer


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
