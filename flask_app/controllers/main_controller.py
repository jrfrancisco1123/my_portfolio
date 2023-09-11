from flask_app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/myportfolio/aboutme')
def about_me():
    return render_template('aboutme.html')