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
        if self.request.GET:
            #model is created
            model = ApiModel()
            model.counter = int(self.request.GET["n"])
            view = ApiView(model.house_data)

            self.response.write(page.return_page())
        self.response.write(view.content)#writes content


''' This class is where the api makes its calls to url, handles parsing data etc'''
class ApiModel(object):
    def __init__(self):
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
        for i in houses:
            house_dict = dict()
            name = i.getElementsByTagName('name')[0].firstChild.nodeValue
            sigil = i.getElementsByTagName('sigil')[0].firstChild.nodeValue
            motto = i.getElementsByTagName('motto')[0].firstChild.nodeValue
            color1 = i.getElementsByTagName('color1')[0].firstChild.nodeValue
            color2 = i.getElementsByTagName('color2')[0].firstChild.nodeValue
            head = i.getElementsByTagName('head')[0].firstChild.nodeValue
            image = i.getElementsByTagName('image')[0].firstChild.nodeValue

            house_dict =[name,sigil,motto,color1,color2,head,image]
            self.__house_data.house.append(house_dict)
    @property
    def house_data(self):
        return self.__house_data


''' This class is for handling the data between model and view'''
class ApiData(object):
    def __init__(self):
    #empty array for data
        self.house = []


''' This class is for the view'''
class ApiView(object):
    def __init__(self, house_data):
    #to hold content

        self.__content = ''
        #loop here gets data from dictionary
        for i in house_data.house:
            self.__content +='<p> Name: ' +i[0]+ '</p>'
			#self.__content += "<a href='?house='>"+i[1]+"</a>"
            self.__content +='<p> Sigil: ' +i[1]+ '</p>'
            self.__content +='<p> Motto: ' +i[2]+ '</p>'
            self.__content +='<p> Color1: ' +i[3]+ '</p>'
            self.__content +='<p> Color2: ' +i[4]+ '</p>'
            self.__content +='<p> Head: ' +i[5]+ '</p>'
            self.__content +='<img src='"+i[6]+ "'>"'
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
        <a href="?n=0">Lannister</a>
        <a href="?n=1">Stark</a>
        <a href="?n=2">Baratheon</a>
        <a href="?n=3">Greyjoy</a>
        <a href="?n=4">Targaryen</a>
        <a href="?n=5">Tully</a>
            '''
        self._body ='<h2>Game of Thrones</h2>'



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
