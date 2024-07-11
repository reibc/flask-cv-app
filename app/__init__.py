from flask import Flask
from flask_restx import Api


def create_app():
    app = Flask(__name__)

    from . import routes
    from . import cli

    api = Api(
        app,
        version='1.0',
        title='My API',
        description='A simple API',
        doc='/swagger',
    )

    # API namespace
    api.add_namespace(routes.api_namespace)

    # CLI commands
    app.cli.add_command(cli.show_command)

    return app
