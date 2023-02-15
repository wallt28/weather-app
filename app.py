from flask import Flask
from flask_smorest import Api


from resources.weather import blp as WeatherBlueprint

def create_app(db_url=None):
    app = Flask(__name__)
    app.config["API_TITLE"] = "Weather APP"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"

    app.config["PROPAGATE_EXCEPTIONS"] = True

    api = Api(app)

    api.register_blueprint(WeatherBlueprint)

    return app


