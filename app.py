# File: app.py
# Author: Teodora Stokic
# Date: 26.06.2026
# Version: 1.2
# Description:
# Main Flask application file.
# Defines database models, routes, and CRUD operations for managing recipes, ingredients, categories, and preparation steps.

from flask import Flask, render_template, request, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename

recipe_app  = Flask(__name__)
recipe_app.config['SECRET_KEY'] = 'change_this_secret_key'
recipe_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rezepte.db'
# Allowed image file extensions for recipe uploads
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    # Returns True if the file extension is in the allowed list
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
db = SQLAlchemy(recipe_app)

# --- Database Models ---
class Category(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)

class Recipe(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  description = db.Column(db.String(500), nullable=False)
  image = db.Column(db.String(200))
  preparation_time = db.Column(db.Integer, nullable=False)
  portions = db.Column(db.Integer, nullable=False)
  difficulty = db.Column(db.String(50), nullable=False)
  category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
  category = db.relationship('Category', backref='recipes')
  is_default = db.Column(db.Boolean, default=False, nullable=False)

class Ingredient(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  quantity = db.Column(db.Float)
  measurement_unit = db.Column(db.String(50))
  recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))

class Preparation(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  step_number = db.Column(db.Integer, nullable=False)
  description = db.Column(db.String(500), nullable=False)
  recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))

# --- Routes ---
@recipe_app.route('/')
def welcome():
  return render_template('welcome.html')

@recipe_app.route('/recipes')
def home():
  # Filter recipes by category and/or search term (recipe name or ingredient name)
  category_id = request.args.get('category_id', type=int)
  search = request.args.get('search', '').strip()

  query = Recipe.query
  if category_id:
      query = query.filter_by(category_id=category_id)
  if search:
      query = query.join(Ingredient).filter(
          db.or_(
              Recipe.name.ilike(f'%{search}%'),
              Ingredient.name.ilike(f'%{search}%')
          )
      ).distinct()

  recipes = query.all()
  categories = Category.query.all()
  return render_template('index.html', recipes=recipes, categories=categories, selected_category=category_id, search=search)

@recipe_app.route('/recipe/<int:id>')
def recipe_detail(id):
  recipe = Recipe.query.get_or_404(id)
  ingredients = Ingredient.query.filter_by(recipe_id=id).all()
  steps = Preparation.query.filter_by(recipe_id=id).all()
  return render_template('detail.html', recipe=recipe, ingredients=ingredients, steps=steps)

@recipe_app.route('/recipe/create', methods=['GET', 'POST'])
def create_recipe():
  if request.method == 'POST':
      # Validate and save the uploaded image
      image = request.files['image']
      if not allowed_file(image.filename):
         return "Invalid file type", 400
      image_filename = secure_filename(image.filename)
      image.save(os.path.join('static/images/recipes', image_filename))
      # Create the recipe
      recipe = Recipe(
          name=request.form['name'],
          preparation_time=request.form['preparation_time'],
          description=request.form['description'],
          portions=request.form['portions'],
          difficulty=request.form['difficulty'],
          category_id=request.form['category_id'],
          image=image_filename
      )
      db.session.add(recipe)
      db.session.commit()
      # Save ingredients (quantity and unit are optional)
      names = request.form.getlist('ingredient_name[]')
      quantities = request.form.getlist('ingredient_quantity[]')
      units = request.form.getlist('ingredient_unit[]')
      for i in range(len(names)):
          if names[i]:
              ingredient = Ingredient(
                  name=names[i],
                  quantity=quantities[i] if quantities[i] else None,
                  measurement_unit=units[i] if units[i] else None,
                  recipe_id=recipe.id
              )
              db.session.add(ingredient)
      # Save preparation steps
      descriptions = request.form.getlist('step_description[]')
      step_number = 1
      for desc in descriptions:
          if desc:
              step = Preparation(
                  step_number=step_number,
                  description=desc,
                  recipe_id=recipe.id
              )
              db.session.add(step)
              step_number += 1

      db.session.commit()
      return redirect(url_for('home'))

  categories = Category.query.all()
  return render_template('create.html', categories=categories)

@recipe_app.route('/recipe/<int:id>/edit', methods=['GET', 'POST'])
def edit_recipe(id):
  recipe = Recipe.query.get_or_404(id)
  ingredients = Ingredient.query.filter_by(recipe_id=id).all()
  steps = Preparation.query.filter_by(recipe_id=id).all()

  if request.method == 'POST':

      recipe.name = request.form['name']
      recipe.description = request.form['description']
      # Only update image if a new file was uploaded
      image = request.files.get('image')
      if image and image.filename:
        if not allowed_file(image.filename):
           return "Invalid file type", 400
        image_filename = secure_filename(image.filename)
        image.save(os.path.join('static/images/recipes', image_filename))
        recipe.image = image_filename
      recipe.preparation_time = int(request.form['preparation_time'])
      recipe.portions = int(request.form['portions'])
      recipe.difficulty = request.form['difficulty']
      recipe.category_id = request.form['category_id']
      # Update ingredients, quantity and unit are set to None if left empty
      for ingredient in ingredients:
        ingredient.name = request.form.get(f'ingredient_name_{ingredient.id}', ingredient.name)

        ingredient_quantity_value = request.form.get(f'ingredient_quantity_{ingredient.id}', '')
        ingredient.quantity = float(ingredient_quantity_value) if ingredient_quantity_value and ingredient_quantity_value.strip() else None

        ingredient_unit_value = request.form.get(f'ingredient_unit_{ingredient.id}', '')
        ingredient.measurement_unit = ingredient_unit_value if ingredient_unit_value and ingredient_unit_value.strip() else None
      # Update preparation steps
      for step in steps:
        step.description = request.form.get(f'step_description_{step.id}', step.description)

      db.session.commit()
      return redirect(url_for('home'))
  categories = Category.query.all()
  return render_template('edit.html', recipe=recipe, ingredients=ingredients, steps=steps, categories=categories)

@recipe_app.route('/recipe/<int:id>/delete', methods=['POST'])
def delete_recipe(id):
  # Delete ingredients and steps before deleting the recipe
  recipe = Recipe.query.get_or_404(id)
  Ingredient.query.filter_by(recipe_id=id).delete()
  Preparation.query.filter_by(recipe_id=id).delete()
  db.session.delete(recipe)
  db.session.commit()
  return redirect(url_for('home'))

if __name__ == '__main__':
  with recipe_app.app_context():
      db.create_all()
  recipe_app.run(debug=False)
