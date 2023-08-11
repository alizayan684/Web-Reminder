from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the app and the database instances
app = Flask(__name__)

# set the configuration options
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # change this to your desired database
app.config['SECRET_KEY'] = 'jw8s0vm4x1'  # change this to a random and secure string

# create the tables if they don't exist
db = SQLAlchemy(app)


def creator():
    with app.app_context():
        db.create_all()


# import the routes before creating the app context
from routes import *

# run the app in debug mode only for development
if __name__ == '__main__':
    app.run(debug=True)
