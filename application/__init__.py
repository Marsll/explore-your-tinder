"""Initialize app."""
from flask import Flask


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)

    # Application Configuration
    app.config.from_object('config.Config')

    with app.app_context():

        
        # Import parts of our application
        from .landing import landing_routes
        app.register_blueprint(landing_routes.landing_bp)


        # Import Dash application
        from .dashapp import dash_app
        app = dash_app.Add_Dash(app)

        return app
