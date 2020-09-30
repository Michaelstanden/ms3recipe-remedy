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
app.config["MONGO_DBNAME"] = 'Recipes'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

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


@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        recipe = mongo.db.recipe
        recipe.insert_one(request.form.to_dict())
        return redirect(url_for('recipe.html'))
    return render_template('add_recipe.html',
                           categories=mongo.db.categories.find())


@app.route('/edit_recipe')
def edit_recipe():
    return render_template('edit_recipe.html')


@app.route('/contact_us')
def contact_us():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)