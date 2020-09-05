from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def hell_world():
  return 'Vulnerable web application'

"""
WHY:
  Vulnerability occurs because a user controlled input is rendered back without any escaping (sanitization).

COMMENTS:
  Looks like flask doesn't escape variable URLs by default.
  https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
  No need to escape  int, float, path, uuid?
  Browser didn't help at all. Frontend framework could've helped. Flask didn't help

Exploitation:
  http://127.0.0.1:5000/xss/%3Cimg%20src=x%20onerror=%22alert(document.domain)%22%3E
  translates to
  http://127.0.0.1:5000/xss/<img src=x onerror='alert(document.domain)'>
"""

@app.route('/xss/<value>')
def xss(value):
  return f'value is: {value}'

"""
Can be prevented by simply escaping value using escape function in markupsafe module
"""

@app.route('/noxss/<value>')
def noXss(value):
  return f'value is {escape(value)}'
