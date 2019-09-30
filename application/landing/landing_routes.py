"""Routes for main pages."""
import logging

import shortuuid
from flask import Blueprint
from flask import current_app as app
from flask import flash, redirect, render_template, request, url_for
from werkzeug import secure_filename

from ..models import User, db

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
            uuid = shortuuid.uuid()
            filename = 'application/static/uploads/' + filename + 'json'
            file.save(filename)
            custom_url = "/dashapp/" + uuid
            create_date, gender, gender_filter = get_some_data(filename)


            #ToDo

            
            #from random_string_file get create_date
            #search database for same create_date
            # if (equal) take old row and get old_random_string
                #1. delete old_random_strin_file
                #2 replace random_string in database
            #else add new user
            new_user = User(url=uuid,
                            create_date=create_date,
                            gender= gender,
                            gender_filter=gender_filter
                   ) 
            db.session.add(new_user)  # Adds new User record to database
            db.session.commit()  # Commits all changes
            return redirect(custom_url)

    return render_template('index.html',
                           title='Explore your Tinder | Upload')


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


def get_some_data(filename):
    with open(filename, encoding="utf8") as json_file:
        data = json.load(json_file)
    create_date = data["User"]['create_date']
    gender = data["User"]["gender"]
    gender_filter = data["User"]["gender_filter"]
    if gender_filter == "M and F":
        gender_filter = "D"

    return create_date, gender, gender_filter
