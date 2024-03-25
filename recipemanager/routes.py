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
        return redirect(url_for('home'))  
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.password == password:
            session['username'] = username  
            session['user_id'] = user.id  
            return redirect(url_for('home'))  
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
    session.pop('user_id', None)  
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
        
        ingredients = []
        for i in range(1, 11):  
            ingredient_name = request.form.get(f'ingredient_name_{i}')
            ingredient_quantity = request.form.get(f'ingredient_quantity_{i}')
            if ingredient_name and ingredient_quantity:
                ingredients.append({"name": ingredient_name, "quantity": ingredient_quantity})
        
        for ingredient in ingredients:
            new_recipe.add_ingredient(ingredient['name'], ingredient['quantity'])
        
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
   
    for recipe in user_recipes:
        if recipe.ingredients is None:
            recipe.ingredients = []  
    
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

    user_id = session.get('user_id')
    recipe = Recipe.query.filter_by(id=recipe_id, user_id=user_id).first()

    if not recipe:
        return redirect(url_for('manage_recipes'))

    if request.method == 'POST':
        recipe.title = request.form['title']
        recipe.description = request.form['description']
        recipe.instructions = request.form['instructions']
        recipe.category_name = request.form['category']
        recipe.preparation_time = request.form['preparation_time']
        recipe.cook_time = request.form['cook_time']
        recipe.image_url = request.form['image_url'] 

        recipe.ingredients = []
        index = 0
        while True:
            ingredient_name = request.form.get(f'ingredient_name_{index}')
            ingredient_quantity = request.form.get(f'ingredient_quantity_{index}')
            if ingredient_name is not None and ingredient_quantity is not None:
                recipe.ingredients.append({"name": ingredient_name, "quantity": ingredient_quantity})
                index += 1
            else:
                break

        new_ingredient_names = request.form.getlist('new_ingredient_name')
        new_ingredient_quantities = request.form.getlist('new_ingredient_quantity')
        for name, quantity in zip(new_ingredient_names, new_ingredient_quantities):
            if name.strip() and quantity.strip():
                recipe.ingredients.append({"name": name, "quantity": quantity})

        db.session.commit()
        
        return redirect(url_for('manage_recipes'))
    
    categories = [
        {'id': 1, 'name': 'Around the World'},
        {'id': 2, 'name': 'Quick & Easy'},
        {'id': 3, 'name': 'Healthy Food'},
        {'id': 4, 'name': 'Sweet Treats'}
    ]
    
    return render_template('edit_recipe.html', username=session['username'], recipe=recipe, categories=categories, ingredientCounter=len(recipe.ingredients))



@app.route('/delete_recipe/<int:recipe_id>', methods=['POST'])
def delete_recipe(recipe_id):
    if 'username' not in session:
        return redirect(url_for('login')) 
    
    user_id = session.get('user_id')
    recipe = Recipe.query.filter_by(id=recipe_id, user_id=user_id).first()
    
    if not recipe:
        return redirect(url_for('manage_recipes'))
    
    try:
        comment_ids = [comment.id for comment in recipe.comments]
        comments_deleted = Comment.query.filter_by(recipe_id=recipe_id).delete()
       
        db.session.commit()

        db.session.delete(recipe)
        db.session.commit()

    except Exception as e:
        db.session.rollback()

    return redirect(url_for('manage_recipes'))

@app.route('/recipe/<int:recipe_id>', methods=['GET', 'POST'])
def recipe_details(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    comments = Comment.query.filter_by(recipe_id=recipe_id).all()
    
    if request.method == 'POST':
        if 'user_id' in session:  
            user_id = session.get('user_id')
            content = request.form.get('comment_content')
            if content:
                new_comment = Comment(content=content, user_id=user_id, recipe_id=recipe_id)
                db.session.add(new_comment)
                db.session.commit()
                flash('Comment added successfully!', 'success')
            else:
                flash('Comment cannot be empty!', 'warning')
        else:
           
            name = request.form.get('name')
            email = request.form.get('email')
            content = request.form.get('comment_content')
            if name and email and content:
            
                new_comment = Comment(content=content, name=name, email=email, recipe_id=recipe_id)
                db.session.add(new_comment)
                db.session.commit()
                flash('Comment added successfully!', 'success')
            else:
                flash('Name, email, and comment content are required!', 'danger')
    
    return render_template('recipe_details.html', recipe=recipe, comments=comments)


@app.route('/manage_comments')
def manage_comments():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    username = session.get('username')  
    
    user_comments = Comment.query.filter_by(user_id=user_id).all()
    recipe_comments = Comment.query.join(Recipe).filter(Recipe.user_id == user_id).all()

    return render_template('manage_comments.html', user_comments=user_comments, recipe_comments=recipe_comments, username=username)

@app.route('/delete_comment/<int:comment_id>', methods=['POST'])
def delete_comment(comment_id):

    comment = Comment.query.get(comment_id)
    if comment:
        db.session.delete(comment)
        db.session.commit()
        flash('Comment deleted successfully!', 'success')
    else:
        flash('Comment not found.', 'danger')

    return redirect(url_for('manage_comments')) 

@app.route('/edit_comment/<int:comment_id>', methods=['GET', 'POST'])
def edit_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if not comment:
        flash('Comment not found.', 'danger')
        return redirect(url_for('manage_comments'))

    comment_content = comment.content

    return render_template('edit_comment.html', comment_id=comment_id, comment_content=comment_content)



@app.route('/update_comment/<int:comment_id>', methods=['POST'])
def update_comment(comment_id):
    if request.method == 'POST':
       
        updated_content = request.form.get('content')
        comment = Comment.query.get(comment_id)
        if comment:
            comment.content = updated_content
            db.session.commit()
            flash('Comment updated successfully!', 'success')
        else:
            flash('Comment not found.', 'danger')

    return redirect(url_for('manage_comments'))


@app.route('/search', methods=['GET'])
def search():
    return render_template('search.html')


@app.route('/search_results', methods=['GET'])
def search_results():
    query = request.args.get('query')
    search_results = Recipe.query.filter(Recipe.title.ilike(f'%{query}%')).all()

    return render_template('search_results.html', search_results=search_results, query=query)

if __name__ == "__main__":
    app.run(debug=True)






