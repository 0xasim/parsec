from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/')
def hell_world():
  return 'Vulnerable web application'

@app.route('/xss/<value>')
def xss(value):
  return f'value is: {value}'

@app.route('/noxss/<value>')
def noXss(value):
  return f'value is {escape(value)}'
