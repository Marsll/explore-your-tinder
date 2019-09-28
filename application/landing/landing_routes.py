"""Routes for main pages."""
from flask import Blueprint
from flask import current_app as app
from flask import render_template
from flask import url_for, redirect, render_template
from werkzeug import secure_filename
from .forms import UploadForm

# Blueprint Configuration
landing_bp = Blueprint('landing_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@landing_bp.route('/', methods=['GET', 'POST'])
def landing():
  
    form = UploadForm()

    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)     
        form.file.data.save('application/static/uploads/' + filename)
        return redirect(url_for('/dashapp/'))

    """Homepage route."""
    return render_template('index.html',
                            form=form,
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
