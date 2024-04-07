# recipemanager/routes.py
import os
from flask import Flask, render_template, request, session, redirect, url_for, flash
from recipemanager import app, db
from recipemanager.models import User, Recipe, Rating, Comment
from datetime import datetime
from werkzeug.routing import UUIDConverter
from sqlalchemy import or_, func, cast, Text , desc


app.secret_key = 'saba'

@app.context_processor
def inject_categories():
    categories = ['Around the World', 'Quick & Easy', 'Healthy Food', 'Sweet Treats']
    return dict(categories=categories)



@app.route('/')
def home():
    recipes = Recipe.query.all()  
    top_rated_recipes = db.session.query(
        Recipe,
        func.avg(Rating.rating).label('avg_rating')
    ).join(Rating).group_by(Recipe.id).order_by(desc('avg_rating')).limit(3).all()
    return render_template('home.html', top_rated_recipes=top_rated_recipes)



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
            flash('Username already exists', 'danger')
        elif existing_email:
            flash('Email already exists', 'danger')
        else:
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            
            session['username'] = username
            session['user_id'] = new_user.id
            
            flash('Registration successful! Welcome, ' + username, 'success')
            return redirect(url_for('user_dashboard', user_id=new_user.id))
    
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

        return redirect(url_for('view_recipes', user_id=user_id))

    
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
        average_rating = Rating.query.filter_by(recipe_id=recipe.id).with_entities(func.avg(Rating.rating)).scalar()
        recipe.average_rating = average_rating

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
        flash('You must be logged in to edit a recipe', 'danger')
        return redirect(url_for('login')) 

    user_id = session.get('user_id')
    recipe = Recipe.query.filter_by(id=recipe_id, user_id=user_id).first()

    if not recipe:
        flash('Recipe not found or you do not have permission to edit it', 'danger')
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
        
        flash('Recipe updated successfully', 'success')
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
        flash('You must be logged in to delete recipes.', 'danger')
        return redirect(url_for('login')) 
    
    user_id = session.get('user_id')
    
    recipe = Recipe.query.filter_by(id=recipe_id, user_id=user_id).first()
    
    if not recipe:
        flash('Recipe not found or you are not authorized to delete it.', 'danger')
        return redirect(url_for('manage_recipes'))
    
    try:
        
        Comment.query.filter_by(recipe_id=recipe_id).delete()
        Rating.query.filter_by(recipe_id=recipe_id).delete()
        
        db.session.commit()
        db.session.delete(recipe)
        db.session.commit()
        
        flash('Recipe deleted successfully.', 'success')

    except Exception as e:
        flash('An error occurred while deleting the recipe.', 'danger')
        db.session.rollback()

    return redirect(url_for('manage_recipes'))



app.url_map.converters['uuid'] = UUIDConverter

@app.route('/recipe/<uuid:unique_identifier>', methods=['GET', 'POST'])
def recipe_details(unique_identifier):
    recipe = Recipe.query.filter_by(unique_identifier=unique_identifier).first()
    average_rating = Rating.query.filter_by(recipe_id=recipe.id).with_entities(func.avg(Rating.rating)).scalar()

    if not recipe:
        flash('Recipe not found!', 'danger')
        return redirect(url_for('home')) 
    
    comments = Comment.query.filter_by(recipe_id=recipe.id).all()
    authenticated = 'user_id' in session
    
    if request.method == 'POST':
        if authenticated:
            user_id = session.get('user_id')
            content = request.form.get('comment_content')
            if content:
                new_comment = Comment(content=content, user_id=user_id, recipe_id=recipe.id)
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
                new_comment = Comment(content=content, name=name, email=email, recipe_id=recipe.id)
                db.session.add(new_comment)
                db.session.commit()
                flash('Comment added successfully!', 'success')
            else:
                flash('Name, email, and comment content are required!', 'danger')

    return render_template('recipe_details.html', recipe=recipe, comments=comments, authenticated=authenticated, average_rating=average_rating)


@app.route('/share_recipe/<unique_identifier>', methods=['GET'])
def share_recipe(unique_identifier):
    print("Share Recipe Route Accessed")
    recipe = Recipe.query.filter_by(unique_identifier=unique_identifier).first()

    if recipe:
        return render_template('shareable_link.html', unique_identifier=unique_identifier)
    else:
        flash('Recipe not found!', 'danger')
        return redirect(url_for('home')) 


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
    username = session.get('username')
    categories = [
        {'id': 1, 'name': 'Around the World'},
        {'id': 2, 'name': 'Quick & Easy'},
        {'id': 3, 'name': 'Healthy Food'},
        {'id': 4, 'name': 'Sweet Treats'}
    ]
    return render_template('search.html', username=username, categories=categories)



@app.route('/search_results', methods=['GET'])
def search_results():
    username = session.get('username')
    query = request.args.get('query')
    category = request.args.get('category')
    ingredients = request.args.get('ingredients')
    cooking_time = request.args.get('cooking_time')
    
    query_filters = []

    if query:
        query_filters.append(Recipe.title.ilike(f'%{query}%'))
    if category:
        query_filters.append(Recipe.category_name.ilike(f'%{category}%'))
    if ingredients:
        query_filters.append(cast(Recipe.ingredients, Text).ilike(f'%{ingredients}%'))
    if cooking_time:
       
        try:
            cooking_time = int(cooking_time)
        except ValueError:
            flash('Invalid cooking time format', 'error')
            return redirect(url_for('search'))  
    
        query_filters.append(Recipe.cook_time <= cooking_time)

    search_results = Recipe.query.filter(or_(*query_filters)).all()

    return render_template('search_results.html', search_results=search_results, query=query, username=username)


@app.route('/search_results_home', methods=['GET'])
def search_results_home():
    username = session.get('username')
    query = request.args.get('query')
    search_results = Recipe.query.filter(Recipe.title.ilike(f'%{query}%')).all()

    return render_template('search_results_home.html', search_results=search_results, query=query, username=username)


@app.route('/profile')
def view_profile():
    username = session.get('username')
    if username:
        user = User.query.filter_by(username=username).first()
        if user:
            user_profile = {
                'username': user.username,
                'email': user.email,
                'created_at': user.created_at, 
            }
            return render_template('profile.html', profile=user_profile, username=username)
   
    return redirect(url_for('login'))  


@app.route('/update_profile', methods=['POST'])
def update_profile():
    if 'username' in session:
        username = session['username']
        new_username = request.form['username']
        new_email = request.form['email']
        
        user = User.query.filter_by(username=username).first()
        if user:
            user.username = new_username
            user.email = new_email
            db.session.commit()
            session.clear()
            return redirect(url_for('login'))
    
    return redirect(url_for('error_page'))



@app.route('/recipe/<unique_identifier>/rate', methods=['POST'])
def submit_rating(unique_identifier):
    if 'user_id' in session:  
        user_id = session['user_id']
    else:
        user_id = None  

    rating_value = request.form.get('rating')

    if rating_value is None or rating_value.strip() == '':
        flash('Please provide a rating.', 'error')
        return redirect(url_for('recipe_details', unique_identifier=unique_identifier))

    try:
        rating_value = int(rating_value)
    except ValueError:
        flash('Invalid rating value.', 'error')
        return redirect(url_for('recipe_details', unique_identifier=unique_identifier))

    recipe = Recipe.query.filter_by(unique_identifier=unique_identifier).first()

    if recipe:
        rating = Rating(rating=rating_value, user_id=user_id, recipe_id=recipe.id)
        db.session.add(rating)
        db.session.commit()
        flash('Thank you for rating this recipe!', 'success')
    else:
        flash('Recipe not found!', 'error')

    return redirect(url_for('recipe_details', unique_identifier=unique_identifier))


@app.route('/recipes/<category>', methods=['GET'])
def recipes_by_category(category):
    recipes = Recipe.query.filter_by(category_name=category).all()
    return render_template('recipes_by_category.html', recipes=recipes, category=category)



def get_user_dashboard_stats(user_id):
    user = User.query.get(user_id)
    if not user:
        return None

    total_recipes = len(user.recipes)

    total_comments = Comment.query.filter_by(user_id=user_id).count()

    most_popular_category_query = db.session.query(Recipe.category_name, func.count(Recipe.id).label('count')) \
        .filter_by(user_id=user_id) \
        .group_by(Recipe.category_name) \
        .order_by(func.count(Recipe.id).desc()) \
        .first()

    most_popular_category = most_popular_category_query[0] if most_popular_category_query else None

    total_ratings = 0
    total_recipe_ratings = 0
    for recipe in user.recipes:
        recipe_ratings = Rating.query.filter_by(recipe_id=recipe.id).all()
        total_recipe_ratings += len(recipe_ratings)
        for rating in recipe_ratings:
            total_ratings += rating.rating
    average_rating = total_ratings / total_recipe_ratings if total_recipe_ratings > 0 else 0

    total_ratings_given = Rating.query.filter_by(user_id=user_id).count()

    recipe_most_comments = max(user.recipes, key=lambda x: len(x.comments)).title if user.recipes else None

    recipe_highest_rating_query = db.session.query(Recipe.title, func.avg(Rating.rating).label('avg_rating')) \
        .join(Rating, Recipe.id == Rating.recipe_id) \
        .filter(Recipe.user_id == user_id) \
        .group_by(Recipe.id) \
        .order_by(func.avg(Rating.rating).desc()) \
        .first()

    recipe_highest_rating = recipe_highest_rating_query[0] if recipe_highest_rating_query else None

    return {
        'total_recipes': total_recipes,
        'total_comments': total_comments,
        'most_popular_category': most_popular_category,
        'average_rating': average_rating,
        'total_ratings_given': total_ratings_given,
        'recipe_most_comments': recipe_most_comments,
        'recipe_highest_rating': recipe_highest_rating
    }


@app.route('/dashboard/<int:user_id>')
def user_dashboard(user_id):
    user = User.query.get(user_id)
    if not user:
        return "User not found", 404

    username = user.username  

    stats = get_user_dashboard_stats(user_id)
    return render_template('user_dashboard.html', user=user, stats=stats, username=username)



@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    username = session.get('username')
    
    if request.method == 'POST':
        if not username:
            flash('You must be logged in to change your password', 'danger')
            return redirect(url_for('login'))
        
        old_password = request.form['old_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']
        
        user = User.query.filter_by(username=username).first()  
        
        if user and user.password == old_password:
            if new_password == confirm_password:
                user.password = new_password  
                db.session.commit()
                flash('Password updated successfully', 'success')
                return redirect(url_for('user_dashboard', user_id=user.id))

            else:
                flash('New passwords do not match', 'danger')
        else:
            flash('Invalid old password', 'danger')
    
    return render_template('change_password.html', username=username)


@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')

    flash('You have successfully subscribed to our mailing list!', 'subscription_success')
    return redirect(url_for('home'))



@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email')

        flash('A password reset link has been sent to your email.', 'success')
        return redirect(url_for('login')) 
    return render_template('forgot_password.html')

if __name__ == "__main__":
    app.run(debug=True)






