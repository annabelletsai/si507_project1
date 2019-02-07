# Welcome to my banking app! #

This program will allow you to go to the routes at specific paths that will use the Bank and Currency classes. The following are paths that you can visit:

## Home ##
When visiting "/", you will receive the message "This is the home page."

## Bank ##
When visiting "/bank/<name>", the program will create a new Bank object with the <name> parameter you provide. The Bank class is being pulled from lab3_code.py. It will then return the message "Welcome to <bank name>!".

## Dollar ##
When visiting "/dollar/<amt>", the program will create a new Dollar object with the <amt> parameter you provide. The Dollar class is being pulled from lab3_code.py. It will then return the message of the amount you provided.

## Yuan ##
When visiting "/yuan/<amt>", the program will create a new Yuan object with the <amt> parameter you provide. The Yuan class is being pulled from lab3_code.py. It will then return the message of the amount you provided.

## Pound ##
When visiting "/pound/<amt>", the program will create a Pound object with the <amt> parameter you provide. The Pound class is being pulled from lab3_code.py. It will then return the message of the amount you provided.

## Total Information ##
When visiting "/bank/<name>/<currency>/<value>", the program will create a new Currency object, depending on the input value for the parameter <currency>. It will then take the <name>, the new Currency object, and the <value> to create a new Bank object.


A little about *lab3_code.py*
lab3_code.py has 2 parent classes: Currency and Bank. There are then subclasses for Currency: Dollar, Yuan, Pound.

The Currency class has a method that converts an input into a different currency. Each Currency subclass stores the rate and the currency name. The Bank class stores the name of the bank, the currency, and the value. There is also a method to deposit into the bank. 
