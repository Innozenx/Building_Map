"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Building_Map import app

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index1.html',
        title='1st Floor',
        year=datetime.now().year,
    )

@app.route('/index2.cshtml')
def index2():
    return render_template(
        'index2.html',
        title='2nd Floor',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

