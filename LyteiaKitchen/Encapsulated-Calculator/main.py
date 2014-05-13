'''
Lyteia Kitchen
4/12/14
Lab 3
'''
import webapp2
#gets page.py
from page import Page
class MainHandler(webapp2.RequestHandler):
    def get(self):
        #this is getting the class page
        page = Page()
        #airJordan Shoe Instance

        airj = Shoe()
        airj.name = 'Air Jordans'
        airj.price = 180 #$
        airj.limit = 2 #pairs
        airj.img ="http://upload.wikimedia.org/wikipedia/en/3/37/Jumpman_logo.svg"

        #nikeFoampositePro Shoe Instance

        nfp = Shoe()
        nfp.name = 'Nike Foamposite Pro'
        nfp.price = 220 #$
        nfp.limit = 1 #pairs
        nfp.img = "http://upload.wikimedia.org/wikipedia/en/3/37/Jumpman_logo.svg"

        #nikeFoampositeOne Shoe Instance

        nfo = Shoe()
        nfo.name = 'Nike Foamposite One'
        nfo.price = 220 #$
        nfo.limit = 1 #pairs
        nfo.img ="http://upload.wikimedia.org/wikipedia/en/3/37/Jumpman_logo.svg"

        #lebron Shoe Instance

        leb = Shoe()
        leb.name = 'LeBrons'
        leb.price = 200 #$
        leb.limit = 1 #pairs
        leb.img ="http://upload.wikimedia.org/wikipedia/en/3/37/Jumpman_logo.svg"


        #kobe Shoe Instance

        kobe = Shoe()
        kobe.name = 'Kobes'
        kobe.price = 120 #$
        kobe.limit = 4 #pairs
        kobe.img ="http://upload.wikimedia.org/wikipedia/en/3/37/Jumpman_logo.svg"

        shoes = [
            airj,nfp,nfo,leb,kobe
        ]

        #HTML
        self.response.write(page.header())
        self.response.write(page.form())
        if self.request.GET:
            heat = (int(self.request.GET['heat']))-1
            print heat
            self.response.write(self.html(shoes[heat]))
        self.response.write(page.footer())

     #function for html
    def html(self, obj):
        #sales tax
        sales_tax = 6.5
        #total = price of object * limit of object + sales_tax
        total = obj.price * obj.limit+sales_tax

        finish = '''
        <div id="finish">
            <h2>{obj.name}</h2>
            <img src="{obj.img}" alt="{obj.name}">
            <ul>
                <li>
                    <h4>Price(For 1)</h4>
                    <p>$ {obj.price} us dollars</p>
                </li>
                <li>
                    <h4>Limit On Pairs</h4>
                    <p>{obj.limit} pairs</p>
                </li>
                <li>
                    <h4>Total(with Limit)</h4>
                    <p> $ {total} </p>
                </li>
            </ul>
        </div>
        '''

        finish = finish.format(**locals())
        return finish


#Objects
class Shoe(object):
    def __init__(self):
        self.name = ''
        self.__price = 0
        self.__limit = 0
        self.img = ''

    #Getter for price
    @property
    def price(self):
        return self.__price


    #Setter for price
    @price.setter
    def price(self, v):
        self.__price = v

    #Getter for limit
    @property
    def limit(self):
        return self.__limit

    #Setter for limit
    @limit.setter
    def limit(self, v):
        self.__limit = v

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
