import os
import config
from flask import Flask
from models.base_model import db
from flask_jwt_extended import JWTManager
# from flask_wtf.csrf import CSRFProtect
web_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'team_osm_web')

app = Flask('NEXTAGRAM', root_path=web_dir)
app.config['JWT_SECRET_KEY'] = config.Config.SECRET_KEY
jwt = JWTManager(app)
# csrf = CSRFProtect(app)S


if os.getenv('FLASK_ENV') == 'production':
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")


@app.before_request
def before_request():
    db.connect()


@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        print(db)
        print(db.close())
    return exc
