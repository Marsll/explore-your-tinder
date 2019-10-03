"""Routes for main pages."""
import json
import logging
import os

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


            # Todo catch exception if uuid (the url) is not unique in db

            filename = 'application/static/uploads/' + uuid + '.json'
            file.save(filename)
            custom_url = "/dashapp/" + uuid
            create_date, gender, gender_filter = get_some_data(filename)

            check_duplicate = User.query.filter_by(create_date=create_date).first()    
            if check_duplicate is not None:
                old_url = check_duplicate.url
                try:
                    os.remove(os.path.join('application/static/uploads/', old_url + '.json'))
                except: 
                    pass
                check_duplicate.url = uuid
                db.session.commit()
                app.logger.info("old_url: " + old_url)
                app.logger.info("new_url_generated " + check_duplicate.url)
                app.logger.info("new_url_queried "+ User.query.filter_by(create_date=create_date).first().url)

            else: 
                new_user = User(url=uuid,
                                create_date=create_date,
                                gender=gender,
                                gender_filter=gender_filter
                    ) 

                db.session.add(new_user)  # Adds new User record to database
                db.session.commit()  # Commits all changes
                app.logger.info("new user_url: " +  new_user.url)
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
