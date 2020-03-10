from instagram_api.blueprints.users.views import users_api_blueprint
from instagram_api.blueprints.establishments.views import establishments_api_blueprint
from app import app
from flask_cors import CORS

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.register_blueprint(users_api_blueprint, url_prefix='/api/v1/users')
app.register_blueprint(establishments_api_blueprint,
                       url_prefix='/api/v1/establishment')
