from flask import Flask
app = Flask(__name__)

@app.route('/')
def hell_world():
  return 'Hello, World!'

@app.route('/xss/<value>')
def xss(value):
  return value
