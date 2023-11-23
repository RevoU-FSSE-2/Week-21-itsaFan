from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from extensions import db, bcrypt
from config import Config
from utils.generate_roles import initialize_roles

# Routes Import
from routes.authRoutes import auth_bp
from routes.tweetRoutes import tweet_bp
from routes.followRoutes import follow_bp
from routes.userRoutes import user_bp


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

# Routes
app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(tweet_bp, url_prefix='/api')
app.register_blueprint(follow_bp, url_prefix='/api')
app.register_blueprint(user_bp, url_prefix='/api')