from flask import render_template, request, redirect, url_for
from mealplanner import app, db
from mealplanner.models import Category, Recipe, Cuisine
from sqlalchemy.sql import func


@app.route("/")
def home():
    return render_template("categories.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    categories = list(Category.query.order_by(Category.food_category).all())
    cuisines = list(Cuisine.query.order_by(Cuisine.recipe_cuisine).all())
    if request.method == "POST":
        recipe = Recipe(
            recipe_name=request.form.get("recipe_name"),
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
        return redirect(url_for("home"))
    return render_template("add_recipe.html", categories=categories, cuisines=cuisines)


@app.route("/vegetarian", methods=["GET"])
def vegetarian():
    veg_recipe = list(Recipe.query.filter_by(category_id=1).all())
    return render_template("vegetarian.html", veg_recipe=veg_recipe)


@app.route("/white_meat", methods=["GET"])
def white_meat():
    wmeat_recipe = list(Recipe.query.filter_by(category_id=2).all())
    return render_template("white_meat.html", wmeat_recipe=wmeat_recipe)


@app.route("/red_meat", methods=["GET"])
def red_meat():
    rmeat_recipe = list(Recipe.query.filter_by(category_id=3).all())
    return render_template("red_meat.html", rmeat_recipe=rmeat_recipe)


@app.route("/oily-fish", methods=["GET"])
def oily_fish():
    ofish_recipe = list(Recipe.query.filter_by(category_id=4).all())
    return render_template("oily_fish.html", ofish_recipe=ofish_recipe)


@app.route("/white-fish", methods=["GET"])
def white_fish():
    wfish_recipe = list(Recipe.query.filter_by(category_id=5).all())
    return render_template("white_fish.html", wfish_recipe=wfish_recipe)
