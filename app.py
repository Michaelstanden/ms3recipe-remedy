import os 
from flask import Flask, render_template, redirect, request, url_for, flash, \
      redirect, request, session
from flask_pymongo import PyMongo
import math
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from os import path
if path.exists("env.py"):
    import env


SECRET_KEY = os.environ.get('MONGO_URI')
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Recipe'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Create index for recipe titles in recipe collection

mongo.db.recipe.create_index([('recipe_name', 'text')])

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')



@app.route('/recipe')
def recipe():
    recipes = mongo.db.recipe.find().sort("_id", -1)
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


#edit recipe in edit form, this will change the recipe in the database and on screen
@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    if request.method == 'POST':
        recipe = mongo.db.recipe
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


#deletes a recipe from the datbase and the screen
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipe.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('recipe'))


#log in render
@app.route('/log_in')
def log_in():
    return render_template('login.html')


@app.route('/log_out')
def log_out():
    return render_template('logout.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/register', methods=["GET", "POST"])
def register():
     if request.method == "POST":
        # Check username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
            # makes username in lowercase to identify easier in system

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        new_user = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(new_user)

        # Put user into a session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful! You can now share your own recipes!")
        return redirect(url_for("index", username=session["user"]))
    
     return render_template("register.html")         



#function to show recipes in full
@app.route('/full_recipe/<recipe_id>')
def full_recipe(recipe_id):
    the_recipe = mongo.db.recipe.find_one({'_id': ObjectId(recipe_id)})
    return render_template('full_recipe.html', recipe=the_recipe)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)