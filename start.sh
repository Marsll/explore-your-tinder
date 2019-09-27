# start.sh

export FLASK_APP=wsgi.py
export APP_CONFIG_FILE=config.py
export SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
export SQLALCHEMY_TRACK_MODIFICATIONS=True
export SECRET_KEY=dev
flask run