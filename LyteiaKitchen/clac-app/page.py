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
            </header>
            <div id="main">
        '''

        self.__form = '''
            <form action="" method="GET" name="list" id="buttons">
                <p><a href="/?shop=1" name="shop" id="">/a></p>
                <p><a href="/?shop=2" name="shop" id=""></a></p>
                <p><a href="/?shop=3" name="shop" id=""></a></p>
                <p><a href="/?shop=4" name="shop" id=""></a></p>
                <p><a href="/?shop=5" name="shop" id=""></a></p>
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