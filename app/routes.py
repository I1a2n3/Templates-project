from app import app
from flask import render_template
@app.route('/')
@app.route('/Shop')
def Shop():
    """Index URL"""
    return render_template('index.html', title='Home')

@app.route('/register')
def register():
    """Register URL"""
    return render_template('register.html' , title='Register')

@app.route('/login')
def login():
    """Login URL"""
    return render_template('login.html' , title='Login')

