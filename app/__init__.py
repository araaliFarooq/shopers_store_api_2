from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# Add cors for cross origin resource sharing
CORS(app)

from app.views.authentication import auth_blueprint
from app.views.views import views_blueprint
app.register_blueprint(auth_blueprint)
app.register_blueprint(views_blueprint)

app.config['JWT_SECRET_KEY'] = 'sec-def-oscar-zulu-3-zero-niner'
from flask_jwt_extended import JWTManager
jwt = JWTManager(app)


