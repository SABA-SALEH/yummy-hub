# recipemanager/routes.py
from flask import Flask, render_template, request, session, redirect, url_for
from recipemanager import app, db
from recipemanager.models import User, Recipe, Category, Rating, Comment
from datetime import datetime

app.secret_key = 'saba'

@app.context_processor
def inject_categories():
    categories = ['Around the World', 'Quick & Easy', 'Healthy Food', 'Sweet Treats']
    return dict(categories=categories)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/category/<category>')
def category(category):
    return render_template('categories.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('home')) 
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == 'admin' and password == 'password':
            session['username'] = username  
            return redirect(url_for('home'))  
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home')) 
