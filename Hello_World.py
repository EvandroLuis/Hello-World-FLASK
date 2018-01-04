from flask import Flask
app = Flask(__name__)

@app.route('/')
def projects():
    return 'index'

@app.route('/1')
def about():
    return 'pagina 1'

@app.route('/user/<username>')
def profile(username):
    return 'Hello '+ username