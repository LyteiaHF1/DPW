'''
Lyteia Kitchen
Lab 4
5/14/14
Adding css links for http://www.getskeleton.com/ to help with
adding style to  the page
'''
class Page(object):
    def __init__(self):
        self.header = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Animal Info</title>
        <link rel='stylesheet' type='text/css' href='css/main.css'/>
        <link rel='stylesheet' type='text/css' href='css/base.css' />
        <link rel='stylesheet' type='text/css' href='css/layout.css' />
        <link rel='stylesheet' type='text/css' href='css/skeleton.css' />
    </head>
    <body> <div class='container'>
    '''
        self.body = '''
        <form method='GET' name='animals' id='links'>
            <a href='/?animal=1' name = 'animal' class ='link' id='lion'>Lion</a>
            <a href='/?animal=2' name = 'animal' class ='link' id='tiger'>Tiger</a>
            <a href='/?animal=3' name = 'animal' class ='link' id='panda'>Giant Panda</a>
        </form>
        '''
        self.footer = '''
    </div>
    </body>
</html>'''

    def header(self):
        return self.header
    def body(self):
        return self.body
    def footer(self):
        return self.footer



