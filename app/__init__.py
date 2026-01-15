from flask import Flask, request, g
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_babel import Babel
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Veuillez vous connecter pour accéder à cette page.'
babel = Babel()

def get_locale():
    # Try to get locale from user settings
    user = getattr(g, 'user', None)
    if user is not None and hasattr(user, 'language'):
        return user.language
    # Try to get from session
    from flask import session
    if 'language' in session:
        return session['language']
    # Fall back to accept languages header
    return request.accept_languages.best_match(Config.BABEL_SUPPORTED_LOCALES)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    login_manager.init_app(app)
    babel.init_app(app, locale_selector=get_locale)
    
    # Register blueprints
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.teacher import teacher_bp
    from app.routes.student import student_bp
    from app.routes.forum import forum_bp
    from app.routes.chatbot import chatbot_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(teacher_bp, url_prefix='/enseignant')
    app.register_blueprint(student_bp, url_prefix='/eleve')
    app.register_blueprint(forum_bp, url_prefix='/forum')
    app.register_blueprint(chatbot_bp, url_prefix='/chatbot')
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app
