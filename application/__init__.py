"""Initialize app with the Application Factory Pattern."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    """Construct the core application."""
    app = Flask(__name__, template_folder="templates",
                instance_relative_config=False)
    # Application Configuration
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    
    with app.app_context():
            # Import parts of our application
            # Register blueprints
            from .landing import landing_routes
            app.register_blueprint(landing_routes.landing_bp)

            # Create tables for our models
            db.create_all()

            return app
