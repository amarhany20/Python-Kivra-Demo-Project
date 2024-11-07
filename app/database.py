from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def init_db(app):
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from .models import User, Location, Type, Mail
        db.create_all()
