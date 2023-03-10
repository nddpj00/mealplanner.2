from datetime import time, timedelta
import random
from flask import render_template, request, redirect, url_for, flash
from mealplanner import app, db, models
from mealplanner.models import Category, Recipe, Cuisine
from sqlalchemy.sql import func




@app.route("/")    
def home():
    random_vegmeal = random.choice(Recipe.query.filter_by(category_id=1).all())
    wmeat_recipe = list(Recipe.query.filter_by(category_id=2).all())
    rmeat_recipe = list(Recipe.query.filter_by(category_id=3).all())
    ofish_recipe = list(Recipe.query.filter_by(category_id=4).all())
    wfish_recipe = list(Recipe.query.filter_by(category_id=5).all())
    return render_template("categories.html", random_vegmeal=random_vegmeal, wmeat_recipe=wmeat_recipe, 
    rmeat_recipe=rmeat_recipe, ofish_recipe=ofish_recipe, wfish_recipe=wfish_recipe)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    categories = list(Category.query.order_by(Category.food_category).all())
    cuisines = list(Cuisine.query.order_by(Cuisine.recipe_cuisine).all())
    d=timedelta()
    if request.method == "POST":
        recipe = Recipe(
            recipe_name=request.form.get("recipe_name").title(),
            recipe_notes=request.form.get("recipe_notes"),
            cook_time=request.form.get("cook_time"),
            recipe_location=request.form.get("recipe_location"),
            family_friendly=bool(True if request.form.get("family_friendly") else False),
            recipe_healthy=bool(True if request.form.get("recipe_healthy") else False),
            date_added=func.now(),
            category_id=request.form.get("category_id"),
            cuisine_id=request.form.get("cuisine_id")
        )
        db.session.add(recipe)
        db.session.commit()
        flash('Recipe successfully added')
    return render_template("add_recipe.html", categories=categories, cuisines=cuisines)

@app.route("/edit_recipe/<int:recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    categories = list(Category.query.order_by(Category.food_category).all())
    cuisines = list(Cuisine.query.order_by(Cuisine.recipe_cuisine).all())
    if request.method == "POST":
        recipe.recipe_name = request.form.get("recipe_name").title()
        recipe.recipe_notes = request.form.get("recipe_notes")
        recipe.cook_time = request.form.get("cook_time")
        recipe.recipe_location = request.form.get("recipe_location")
        recipe.family_friendly = bool(True if request.form.get("family_friendly") else False)
        recipe.recipe_healthy = bool(True if request.form.get("recipe_healthy") else False)
        recipe.date_added = func.now()
        recipe.category_id = request.form.get("category_id")
        recipe.cuisine_id = request.form.get("cuisine_id")
        db.session.commit()
        flash('Recipe successfully updated')
    return render_template("edit_recipe.html", recipe=recipe, categories=categories, cuisines=cuisines)

@app.route("/delete_recipe/<int:recipe_id>")
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    flash('Recipe successfully deleted')
    return redirect(request.referrer)

@app.route("/red_meat", methods=["GET"])
def red_meat():
    rmeat_recipe = list(Recipe.query.filter_by(category_id=3).all())
    return render_template("red_meat.html", rmeat_recipe=rmeat_recipe)

@app.route("/vegetarian", methods=["GET"])
def vegetarian():
    veg_recipe = list(Recipe.query.filter_by(category_id=1).all())
    return render_template("vegetarian.html", veg_recipe=veg_recipe)


@app.route("/white_meat", methods=["GET"])
def white_meat():
    wmeat_recipe = list(Recipe.query.filter_by(category_id=2).all())
    return render_template("white_meat.html", wmeat_recipe=wmeat_recipe)


@app.route("/oily-fish", methods=["GET"])
def oily_fish():
    ofish_recipe = list(Recipe.query.filter_by(category_id=4).all())
    return render_template("oily_fish.html", ofish_recipe=ofish_recipe)


@app.route("/white-fish", methods=["GET"])
def white_fish():
    wfish_recipe = list(Recipe.query.filter_by(category_id=5).all())
    return render_template("white_fish.html", wfish_recipe=wfish_recipe)



