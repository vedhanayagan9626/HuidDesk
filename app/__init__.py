from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Database_URI
from routes.auth import auth_bp
def create_app():

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = Database_URI
    app.register_blueprint(auth_bp)
    db = SQLAlchemy(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        
    return app