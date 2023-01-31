from flask import render_template
from mealplanner import app, db
from mealplanner.models import Category, Recipe


@app.route("/")
def home():
    return render_template("base.html")