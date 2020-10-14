import os 
import flask_pymongo
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
import math
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env


SECRET_KEY = os.environ.get('MONGO_URI')
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Recipe'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

# Create index for recipe titles in recipe collection

mongo.db.recipe.create_index([('recipe_name', 'text')])

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/breakfast')
def breakfast():
    return render_template('breakfast.html')
    


@app.route('/lunch')
def lunch():
    return render_template('lunch.html')


@app.route('/dessert')
def dessert():
    return render_template('dessert.html')


@app.route('/recipe')
def recipe():
    recipes = mongo.db.recipe.find().sort("_id", 1)
    return render_template('recipe.html', recipes=recipes)



# Post a recipe to Mongo DB
@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        recipe = mongo.db.recipe
        recipe.insert_one(request.form.to_dict())
        return redirect(url_for('add_recipe'))
    return render_template('add_recipe.html',
                           recipe=mongo.db.recipe.find())



@app.route('/recipe_full/<recipe_id>')
def recipe_full(recipe_id):
    the_recipe = mongo.db.recipe.find_one({'_id': ObjectId(recipe_id)})
    return render_template('recipe.html', recipe=the_recipe)



@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    if request.method == 'POST':
        recipe = mongo.db.recipes
        recipe.update({'_id': ObjectId(recipe_id)}, {
            'recipe_name': request.form.get('recipe_name'),
            'cuisine_type': request.form.get('cuisine_type'),
            'recipe_description': request.form.get('recipe_description'),
            'cooking_time': request.form.get('cooking_time'),
            'prep_time': request.form.get('prep_time'),
            'servings': request.form.get('servings'),
            'ingredients': request.form.get('ingredients'),
            'posted_date': request.form.get('posted_date'),
            'method': request.form.get('method'),
            'image_url': request.form.get('image_url'),
            })
        return redirect(url_for('recipe'))
    else:
        the_recipe = mongo.db.recipe.find_one({'_id': ObjectId(recipe_id)})
        all_recipes = mongo.db.recipe.find()
        return render_template('edit_recipe.html', recipe=the_recipe,
                           recipes=all_recipes)

@app.route('/contact_us')
def contact_us():
    return render_template('contact.html')




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)