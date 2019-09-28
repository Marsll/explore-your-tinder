"""Routes for main pages."""
from flask import Blueprint
from flask import current_app as app
from flask import render_template

# Blueprint Configuration
landing_bp = Blueprint('landing_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@landing_bp.route('/', methods=['GET'])
def landing():
    """Homepage route."""
    return render_template('index.html',
                           title='Landing',
                           template='home-template main',
                           body="Home")


@landing_bp.route('/about', methods=['GET'])
def about():
    """About page route."""
    return render_template('index.html',
                           title='Flask-Blueprint Tutorial | About',
                           template='about-template main',
                           body="About")
