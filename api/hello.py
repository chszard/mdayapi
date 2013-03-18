from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world!"

@app.route('/add/<value>')
def get_index(value):
    return value

 
if __name__ == '__main__':
    app.run(host='192.168.11.2')
