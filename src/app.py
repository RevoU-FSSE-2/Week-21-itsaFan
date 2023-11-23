from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from extensions import db, bcrypt
from config import Config
from routes.auth import auth_bp

# config
app = Flask(__name__)
app.config.from_object(Config)
# Extensions
db.init_app(app)
bcrypt.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

app.register_blueprint(auth_bp, url_prefix='/api')