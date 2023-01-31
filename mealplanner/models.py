from mealplanner import db


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    food_category = db.Column(db.String(25), unique=True, nullable=False)
    recipes = db.relationship("Recipe", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.food_category


class Recipe(db.Model):
    # schema for the Recipe model
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(50), unique=True, nullable=False)
    recipe_notes = db.Column(db.Text, nullable=False)
    recipe_cuisine = db.Column(db.String)
    cook_time = db.Column(db.Integer, nullable=False)
    recipe_location = db.Column(db.Text, nullable=False)
    family_friendly = db.Column(db.Boolean, default=False, nullable=False)
    recipe_healthy = db.Column(db.Boolean, default=False, nullable=False)
    date_added = db.Column(db.Date, nullable=False)
    added_by = db.Column(db.String(20), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Recipe: {1} | Cook: {2} mins".format(
            self.id, self.recipe_name, self.cook_time
        )