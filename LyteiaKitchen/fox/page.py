'''
Lyteia Kitchen
Lab 4
5/14/14
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
            <a href='/?animal=1' name = 'animal' class ='link' id='lion'>Lion</a>
            <a href='/?animal=2' name = 'animal' class ='link' id='tiger'>Tiger</a>
            <a href='/?animal=3' name = 'animal' class ='link' id='panda'>Giant Panda</a>
        </form>
        '''
        self.footer = '''
    </div>
    </body>
</html>'''



