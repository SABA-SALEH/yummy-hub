# recipemanager/routes.py
import os
from flask import Flask, render_template, request, session, redirect, url_for, flash
from recipemanager import app, db
from recipemanager.models import User, Recipe, Rating, Comment
from datetime import datetime

app.secret_key = 'saba'

@app.context_processor
def inject_categories():
    categories = ['Around the World', 'Quick & Easy', 'Healthy Food', 'Sweet Treats']
    return dict(categories=categories)

@app.route('/')
def home():
    recipes = Recipe.query.all()  
    return render_template('home.html', recipes=recipes)

@app.route('/category/<category>')
def category(category):
    return render_template('categories.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        existing_user = User.query.filter_by(username=username).first()
        existing_email = User.query.filter_by(email=email).first()
        
        if existing_user:
            return render_template('register.html', error='Username already exists')
        elif existing_email:
            return render_template('register.html', error='Email already exists')
        else:
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            
            session['username'] = username
            return redirect(url_for('user'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('user'))  
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.password == password:
            session['username'] = username  
            session['user_id'] = user.id  
            return redirect(url_for('user'))  
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

@app.route('/user')
def user():
    if 'username' not in session:
        return redirect(url_for('login')) 
    
    username = session['username']
    
    return render_template('user.html', username=username)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():

    if 'username' not in session:
        return redirect(url_for('login')) 

    username = session['username']
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        instructions = request.form['instructions']
        category_name = request.form['category']  
        preparation_time = request.form['preparation_time']
        cook_time = request.form['cook_time']
        image_url = request.form['image_url']  
        
        user_id = session.get('user_id')
        
        new_recipe = Recipe(
            title=title,
            description=description,
            instructions=instructions,
            user_id=user_id,
            category_name=category_name, 
            image_url=image_url,
            preparation_time=preparation_time,
            cook_time=cook_time
        )
        
        db.session.add(new_recipe)
        db.session.commit()
        
        return redirect(url_for('user'))  
    
    categories = [
        {'id': 1, 'name': 'Around the World'},
        {'id': 2, 'name': 'Quick & Easy'},
        {'id': 3, 'name': 'Healthy Food'},
        {'id': 4, 'name': 'Sweet Treats'}
    ]
    
    return render_template('add_recipe.html', categories=categories, username=username)

@app.route('/view_recipes')
def view_recipes():
    if 'username' not in session:
        return redirect(url_for('login'))  

    username = session['username']
    user_id = session.get('user_id')
    user_recipes = Recipe.query.filter_by(user_id=user_id).all()
    
    return render_template('view_recipes.html', username=username, recipes=user_recipes)

@app.route('/manage_recipes')
def manage_recipes():
    if 'username' not in session:
        return redirect(url_for('login')) 

    username = session['username']
    user_id = session.get('user_id')
    
    user_recipes = Recipe.query.filter_by(user_id=user_id).all()
    
    return render_template('manage_recipes.html', username=username, recipes=user_recipes)


@app.route('/edit_recipe/<int:recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    if 'username' not in session:
        return redirect(url_for('login')) 
    username = session['username']
    user_id = session.get('user_id')
    
    recipe = Recipe.query.filter_by(id=recipe_id, user_id=user_id).first()
    
    if not recipe:
        flash('Recipe not found or you do not have permission to edit this recipe.', 'danger')
        return redirect(url_for('manage_recipes'))
    
    if request.method == 'POST':
        recipe.title = request.form['title']
        recipe.description = request.form['description']
        recipe.instructions = request.form['instructions']
        recipe.category_name = request.form['category']
        recipe.preparation_time = request.form['preparation_time']
        recipe.cook_time = request.form['cook_time']
        recipe.image_url = request.form['image_url'] 

        db.session.commit()
        
        flash('Recipe updated successfully!', 'success')
        return redirect(url_for('manage_recipes'))
    
    categories = [
        {'id': 1, 'name': 'Around the World'},
        {'id': 2, 'name': 'Quick & Easy'},
        {'id': 3, 'name': 'Healthy Food'},
        {'id': 4, 'name': 'Sweet Treats'}
    ]
    
    return render_template('edit_recipe.html', username=username, recipe=recipe, categories=categories)

@app.route('/delete_recipe/<int:recipe_id>', methods=['POST'])
def delete_recipe(recipe_id):
    if 'username' not in session:
        return redirect(url_for('login')) 
    
    user_id = session.get('user_id')
    
    recipe = Recipe.query.filter_by(id=recipe_id, user_id=user_id).first()
    
    if not recipe:
        flash('Recipe not found or you do not have permission to delete this recipe.', 'danger')
        return redirect(url_for('manage_recipes'))
    
    db.session.delete(recipe)
    db.session.commit()
    
    flash('Recipe deleted successfully!', 'success')
    return redirect(url_for('manage_recipes'))


if __name__ == "__main__":
    app.run(debug=True)
