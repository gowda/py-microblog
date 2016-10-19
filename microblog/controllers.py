from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return 'Home Page'


# function name 'help' conflicts with builtin function
@app.route('/help')
def help_page():
    return 'Help Page'
