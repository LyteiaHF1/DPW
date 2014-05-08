class Page():
    #methods
        #behaviors - actions STORE CODE
    def __init__(self, main_self):
        #initializing function - CONSTRUCTOR
            #attributes
            #traits - STORE DATA
            #no underscores is public
            #one underscore is protected access
            #two underscores is mostly private, but not completely
        self.title = "Welcome to the Page"
        self.head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
        <link rel="stylesheet" type="text/css" href="style.css" />
    </head>
    <body>
        '''
        self.body = ""
        self.form = '''
    <form method="GET" action="">
        <input type="text" name="firstname" />
        <input type="text" name="lastname" />
        <input type="submit" value="go" />
    </form>
    '''
        self.ender = '''
    </body>
</html>'''
        main_self.response.write("")


    def print_contents(self, i=""):
        if i=="":
            return self.head + self.body + self.form + self.ender
        else:
            return self.head + i + self.ender


class Button():
    def __init__(self):
        #initializing function - CONSTRUCTOR
        self.label = "Contact Me"
        self.size = 100