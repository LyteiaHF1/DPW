class Page(object):
    def __init__(self):
        self._open = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Food App</title>
        <link rel='stylesheet' type='text/css' href='css/base.css'/>
        <link rel='stylesheet' type='text/css' href='css/layout.css'/>
        <link rel='stylesheet' type='text/css' href='css/skeleton.css'/>
        <link rel="stylesheet" type="text/css" href= 'css/main.css'  />
    </head>
    <body> '''
        self._content = ''
        self._close = '''
    </body>
</html>'''

    def print_out(self):
        self.update()
        return self.all

    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())


class FormPage(Page):
    def __init__(self):
        super(FormPage, self).__init__()
        self.__form_open = '<form method = "GET" action="">'

        self.__inputs = '''
    <img src = images/logo1.png>
    <h4>Hungry</h4>
    <p>Got an ingredient? Don't know what to have? Need ideas? Tell Us What You Want</p>
    <input type ="text" class="search" name="prep"  placeholder="Food" required>
    <input type ="submit" name ="submit">
        '''
        self.__form_close = '</form>'
        self.__small_form = '''
        
        '''

        self.form_header = ">>Form Header<<"
        self._content = self.form_header + self.__form_open + self.__inputs+ self.__form_close

    def update(self):
        self.all = self._open + self.form_header + self.__form_open + self.__inputs+ self.__form_close+ self._close
        self.all = self.all.format(**locals())
