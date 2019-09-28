"""Routes for main pages."""
from flask import Blueprint
from flask import current_app as app
from flask import flash, redirect, render_template, request, url_for
from werkzeug import secure_filename

ALLOWED_EXTENSIONS = set(['json', 'zip', ])


# Blueprint Configuration
landing_bp = Blueprint('landing_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@landing_bp.route('/', methods=['GET', 'POST'])
def landing():
    """Homepage route."""
    #form = UploadForm()

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save('application/static/uploads/' + filename)
            #return redirect(url_for('/dashapp/'))

    return render_template('index.html',
                           title='Explore your Tinder | Upload',
                           template='home-template main',
                           body="Home")


@landing_bp.route('/about', methods=['GET'])
def about():
    """About page route."""
    return render_template('index.html',
                           title='Flask-Blueprint Tutorial | About',
                           template='about-template main',
                           body="About")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
