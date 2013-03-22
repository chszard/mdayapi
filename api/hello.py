#-*- coding UTF-8 -*-
#
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world!"

@app.route('/add/<value>')
def get_index(value):
    return value

def set_user():
    pass

def set_date():

def get_user():
    pass

def get_date():
    pass

def get_feamil_user(value):
    return value
 
if __name__ == '__main__':
    app.run(host='192.168.11.2')
