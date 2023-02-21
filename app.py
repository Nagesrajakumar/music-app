# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, redirect, url_for, request, render_template
 
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello():
    return 'Hello World'

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name
 
 
@app.route('/login', methods=['GET'])
def login():
    return render_template("home.html")
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()