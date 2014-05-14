'''
Lyteia Kitchen
Lab 4
5/14/13
'''


class Page(object):
    def __init__(self):
        self.header = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Animal Info</title>
        <link rel='stylesheet' type='text/css' href='css/main.css'/>
    </head>
    <body> <div class='container'>
    '''
        self.body = '''
        <form method='GET' name='animals' id='links'>
            <a href='/?animal=1' name = 'animal' class ='link' id=''></a>
            <a href='/?animal=2' name = 'animal' class ='link' id=''></a>
            <a href='/?animal=3' name = 'animal' class ='link' id=''></a>
        </form>
        '''
        self.footer = '''
    </div>
    </body>
</html>'''


