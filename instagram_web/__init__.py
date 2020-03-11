from app import app
from flask import render_template
from instagram_web.blueprints.users.views import users_blueprint
from instagram_web.blueprints.establishments.views import establishments_blueprint
from instagram_web.blueprints.employees.views import employees_blueprint
from instagram_web.blueprints.sessions.views import sessions_blueprint
from flask_assets import Environment, Bundle
from .util.assets import bundles
from flask_login import LoginManager
from models.employee import Employee

assets = Environment(app)
assets.register(bundles)

app.register_blueprint(users_blueprint, url_prefix="/users")
app.register_blueprint(establishments_blueprint, url_prefix="/establishments")
app.register_blueprint(employees_blueprint, url_prefix="/employees")
app.register_blueprint(sessions_blueprint, url_prefix="/sessions")


login_manager = LoginManager()
login_manager.init_app(app)


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(401)
def forbidden(e):
    return render_template('401.html'), 401


@app.route("/")
def home():
    return render_template('home.html')


@login_manager.user_loader
def load_user(user_id):
    return Employee.get_by_id(user_id)
