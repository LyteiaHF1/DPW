'''
Lyteia Kitchen
5/14/13
Lab 3
'''
class Page():
    def __init__(self):
        self.__header = '''
<!DOCTYPE>
<html>
    <head>
        <title>Shopping List</title>
        <link rel="stylesheet" href="css/main.css">
    </head>
    <body>
        <div id="wrapper">
            <header>
                <h1>Shopping List For BCT Weight Loss</h1>
                <p>Cut Weight Before Basic Training; These 5 Items are Cheap and Help You Cut Weight FAST</p>
            </header>
            <div id="main">
        '''

        self.__form = '''
            <form action="" method="GET" name="glist" id="buttons">
                <p><a href="/?shop=1" name="shop" id="gfruit">Grape Fruit</a></p>
                <p><a href="/?shop=2" name="shop" id="proteinp">Protein Powder</a></p>
                <p><a href="/?shop=3" name="shop" id="wwb">Whole Wheat Bread</a></p>
                <p><a href="/?shop=4" name="shop" id="eggs">Eggs</a></p>
                <p><a href="/?shop=5" name="shop" id="water">Water</a></p>
            </div>
        '''

        self.__footer = '''
            </div>
        </div>
    </body>
</html>
        '''


    def header(self):
        return self.__header

    def form(self):
        return self.__form

    def footer(self):
        return self.__footer