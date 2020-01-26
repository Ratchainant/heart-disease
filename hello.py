# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 16:58:52 2020

@author: Ratchainant
"""

import flask

app = flask.Flask(__name__)

@app.route("/")
def hello_world():
   return """
          <body>
          <h2> Hello World <h2>
          </body>"""
   
@app.route("/greet/<name>")
def greet(name):
    return "Hello, {}!".format(name)

if __name__ == "__main__":
    app.run()
   