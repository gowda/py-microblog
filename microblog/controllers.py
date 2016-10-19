from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


# function name 'help' conflicts with builtin function
@app.route('/help')
def help_page():
    return render_template('help.html')


@app.route('/about')
def about():
    return render_template('about.html')
