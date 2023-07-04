from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome!'

@app.route('/greet/<username>')
def greet(username):
    return f'Hello, {username}!'

@app.route('/farewell/<username>')
def farewell(username):
    return f'Goodbye, {username}!'

@app.route('/*')
def NotFound():
    return f'Not Valid !'


app.run(debug=True,port=5050)