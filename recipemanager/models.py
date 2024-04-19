# recipemanager/models.py
from recipemanager import db
from datetime import datetime
from sqlalchemy.orm import relationship
import json
import uuid

class User(db.Model):
    """User model for storing user information."""

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    
    # Relationship with Recipe model
    recipes = relationship('Recipe', backref='author', lazy=True)


class Recipe(db.Model):
    """Recipe model for storing recipe information."""

    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    instructions = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) 
    category_name = db.Column(db.String(50)) 
    image_url = db.Column(db.String(255))
    preparation_time = db.Column(db.Integer)
    cook_time = db.Column(db.Integer)
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    ingredients = db.Column(db.JSON)  # Storing ingredients as JSON
    unique_identifier = db.Column(db.String(36), unique=True, nullable=False, default=uuid.uuid4)

    def add_ingredient(self, name, quantity):
        """Method to add an ingredient to the recipe."""
        if not self.ingredients:
            self.ingredients = []
        self.ingredients.append({"name": name, "quantity": quantity})
    
    def get_ingredients(self):
        """Method to get the ingredients of the recipe."""
        return self.ingredients if self.ingredients else []


class Rating(db.Model):
    """Rating model for storing recipe ratings."""

    __tablename__ = 'ratings'
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'))
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)


class Comment(db.Model):
    """Comment model for storing comments on recipes."""

    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id')) 
    name = db.Column(db.String(100))  
    email = db.Column(db.String(255))  

    # Relationship with User and Recipe models
    user = db.relationship('User', backref='comments')
    recipe = db.relationship('Recipe', backref='comments')
