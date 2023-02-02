from flask import render_template, request, redirect, url_for
from mealplanner import app, db
from mealplanner.models import Category, Recipe


@app.route("/")
def home():
    return render_template("categories.html")

@app.route("/categories")
def categories():
    return render_template("categories.html")

@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(food_category=request.form.get("food_category"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")