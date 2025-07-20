from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Database_URI
from routes.auth import auth_bp
from routes.main import main_bp
from routes.qc import QC_bp
from routes.weighing import weighing_bp
from models import db
def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(QC_bp)
    app.register_blueprint(weighing_bp)
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        
    return app