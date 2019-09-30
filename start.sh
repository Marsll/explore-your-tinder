# start.sh

export FLASK_APP=wsgi.py
export FLASK_DEBUG=1
export APP_CONFIG_FILE=config.py
export SECRET_KEY=dev
export SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
export SQLALCHEMY_TRACK_MODIFICATIONS=True
flask run
