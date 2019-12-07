import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
# put your password where the ********* ...
SQLALCHEMY_DATABASE_URI = 'postgres://yosefco3:***************@localhost:5432/trivia'

QUESTIONS_PER_PAGE = 3

QUESTIONS_PER_GAME=5

SQLALCHEMY_TRACK_MODIFICATIONS=False


