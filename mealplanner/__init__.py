import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
if os.path.exists("env.py"):
    import env  # noqa


app=Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

# to allow flask migrate to make changes to tables using Alembic
migrate = Migrate(app, db)

from mealplanner import routes  # noqa