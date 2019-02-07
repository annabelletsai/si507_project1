from flask import Flask
from lab3_code import * #imports all of lab3_code to pull the classes and other functions from there

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is the homepage.'

@app.route('/bank/<name>')
def bank_name(name):
    new_bank = Bank(name, Dollar, 1)
    return 'Welcome to {}!'.format(new_bank.name)

@app.route('/dollar/<amt>')
def dollar_amt(amt):
    dollar_amts = Dollar(int(amt))
    return "{}".format(dollar_amts)


@app.route('/yuan/<amt>')
def yuan_amt(amt):
    yuan_amt = Yuan(int(amt))
    return "{}".format(yuan_amt)

@app.route('/pound/<amt>')
def pound_amt(amt):
    pound_amt = Pound(int(amt))
    return "{}".format(pound_amt)

@app.route('/bank/<name>/<currency>/<value>')
def total_information(name,currency,value):
    if currency == "Dollar":
        c = Dollar(int(value))
    elif currency == "Yuan":
        c = Yuan(int(value))
    else:
        c = Pound(int(value))

    bank = Bank(name,c,int(value))
    return "Welcome to the {} bank! {}".format(bank.name, bank)

if __name__== "__main__":
    app.run()
