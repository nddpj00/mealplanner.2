from flask import render_template, request, redirect, url_for
from mealplanner import app, db
from mealplanner.models import Category, Recipe


@app.route("/")
def home():
    return render_template("categories.html")

@app.route("/categories")
def categories():
    return render_template("categories.html")


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    categories = list(Category.query.order_by(Category.food_category).all())
    if request.method == "POST":
        recipe = Recipe(
            recipe_name=request.form.get("recipe_name"),
            recipe_notes=request.form.get("recipe_notes"),
            recipe_cuisine=request.form.get("recipe_cuisine"),
            cook_time=request.form.get("cook_time"),
            recipe_location=request.form.get("recipe_location"),
            family_friendly=bool(True if request.form.get("family_friendly") else False),
            recipe_healthy=bool(True if request.form.get("recipe_healthy") else False),
            date_added=request.form.get("date_added"),
            category_id=request.form.get("category_id")
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_recipe.html", categories=categories)