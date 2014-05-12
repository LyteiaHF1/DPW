class Page():
    def __init__(self, main_self):
        #define attributes for html
        self.site_name = "SoleSearch"
        self.title = self.site_name + " | Newsletter Sign-Up"
        self.head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>%s</title>
        <link rel="stylesheet" type="text/css" href="style.css" />
    </head>
    <body>
        <div class="container">
            <header>
                <h1><a href="/">%s</a></h1>
            </header>
            <div id="main">
                <section>
                    <p>%s is a community devoted to the art of Collecting Sneakears of all kinds.SoleSearch is a community for Sneakerheads so anything your little sole desire's are included in the newsletters.</p>
                </section>
                <aside>''' %(self.title, self.site_name, self.site_name)
        self.confirmation = '''
                <p>Thanks for subscribing</p>
                <p>Your info:</p>
                '''
        self.form = '''
                    <form method="GET">
                        <fieldset>
                            <legend>Newsletter Sign-Up</legend>
                            <div>
                                <input type="text" name="first_name" placeholder="First Name" required>
                                <input type="text" name="last_name" placeholder="Last Name" required>
                            </div>
                            <div>
                                <input type="text" name="address" placeholder="Street Address" required>
                            </div>
                            <div>
                                <input type="text" name="city" id="city" placeholder="City" required>
                                <select name="state" id="state" required>
                                    <option value="" disabled selected>State</option>
                                    <option value="AL">AL</option>
                                    <option value="AK">AK</option>
                                    <option value="AZ">AZ</option>
                                    <option value="AR">AR</option>
                                    <option value="CA">CA</option>
                                    <option value="CO">CO</option>
                                    <option value="CT">CT</option>
                                    <option value="DE">DE</option>
                                    <option value="DC">DC</option>
                                    <option value="FL">FL</option>
                                    <option value="GA">GA</option>
                                    <option value="HI">HI</option>
                                    <option value="ID">ID</option>
                                    <option value="IL">IL</option>
                                    <option value="IN">IN</option>
                                    <option value="IA">IA</option>
                                    <option value="KS">KS</option>
                                    <option value="KY">KY</option>
                                    <option value="LA">LA</option>
                                    <option value="ME">ME</option>
                                    <option value="MD">MD</option>
                                    <option value="MA">MA</option>
                                    <option value="MI">MI</option>
                                    <option value="MN">MN</option>
                                    <option value="MS">MS</option>
                                    <option value="MO">MO</option>
                                    <option value="MT">MT</option>
                                    <option value="NE">NE</option>
                                    <option value="NV">NV</option>
                                    <option value="NH">NH</option>
                                    <option value="NJ">NJ</option>
                                    <option value="NM">NM</option>
                                    <option value="NY">NY</option>
                                    <option value="NC">NC</option>
                                    <option value="ND">ND</option>
                                    <option value="OH">OH</option>
                                    <option value="OK">OK</option>
                                    <option value="OR">OR</option>
                                    <option value="PA">PA</option>
                                    <option value="RI">RI</option>
                                    <option value="SC">SC</option>
                                    <option value="SD">SD</option>
                                    <option value="TN">TN</option>
                                    <option value="TX">TX</option>
                                    <option value="UT">UT</option>
                                    <option value="VT">VT</option>
                                    <option value="VA">VA</option>
                                    <option value="WA">WA</option>
                                    <option value="WV">WV</option>
                                    <option value="WI">WI</option>
                                    <option value="WY">WY</option>
                                </select>
                                <input type="text" name="zipcode" id="zipcode" placeholder="Zipcode" required>
                            </div>
                        <div>
                            <input type="email" name="email" placeholder="Email Address" required>
                        </div>
                        <div>
                            <input type="checkbox" name="urgent_info" id="urgent_info">
                            <label for="urgent_info">Receive updates</label>
                        </div>
                        <div>
                            <input type="submit" value="Sign-Up">
                        </div>
                        </fieldset>
                    </form>'''
        self.ender = '''
                </aside>
            </div>
            <footer>
                <p>SoleSearch |2014</p>
            </footer>
        </div>
    </body>
</html>'''

    def print_form_results(self, i=""):

        if i=="":
            return self.head + self.form + self.ender
        else:
            return self.head + self.confirmation + i + self.ender