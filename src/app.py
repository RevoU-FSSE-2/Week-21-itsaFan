from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from extensions import db, bcrypt
from config import Config
from routes.auth import auth_bp
from routes.tweet import tweet_bp
from utils.generate_roles import initialize_roles

# config
app = Flask(__name__)
app.config.from_object(Config)
# Extensions
db.init_app(app)
bcrypt.init_app(app)

# Create tables
with app.app_context():
    # db.drop_all()
    db.create_all()
    initialize_roles()


app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(tweet_bp, url_prefix='/api')