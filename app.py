from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def hell_world():
  return 'Vulnerable web application'

"""
Vulnerability occurs because a user controlled input is rendered back without any escaping (sanitization).

Looks like flask doesn't escape variable URLs by default.
https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
No need to escape  int, float, path, uuid?
"""

@app.route('/xss/<value>')
def xss(value):
  return f'value is: {value}'

"""
Can be prevented by escaping value using escape function in markupsafe module
"""

@app.route('/noxss/<value>')
def noXss(value):
  return f'value is {escape(value)}'
