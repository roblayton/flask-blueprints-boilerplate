from flask import Flask
from flask.ext.cors import CORS
from config import config

def create_app(environment):
    app = Flask(__name__)
    cors = CORS(app)
    app.config.from_object(config[environment])

    from root import root
    from messages import messages

    app.register_blueprint(root)
    app.register_blueprint(messages, url_prefix='/messages')

    return app
