from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message_category = 'info'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login.init_app(app)

    from blogapp.auth.routes import auth_bp as auth
    from blogapp.blog.routes import blog
    from blogapp.admin.routes import admin_bp as admin
    from blogapp.user.routes import user_bp as user

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(blog)
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(user)

    with app.app_context():
        db.create_all()

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('errors/500.html'), 500

    return app
