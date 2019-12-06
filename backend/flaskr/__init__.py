import os
from flask import Flask, request, abort, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import random



app=Flask(__name__)
app.config.from_object('config')
CORS(app,resources={"*" : {"origins":"*"}})
db=SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)



'''
@TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
@TODO: Use the after_request decorator to set Access-Control-Allow
'''

# cors headers
@app.after_request
def after_request(response):
    # response.headers.add('Access-Control-Allow-Origin',r"*")
    response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods','GET,PATCH,POST,DELETE,OPTIONS')
    return response

api=Api(app)

from flaskr.models.category import CategoryModel
from flaskr.models.question import QuestionModel

from flaskr.resources.category import CategoryList,CategoryQuestions
from flaskr.resources.question import Question,DeleteQuestion,SearchQuestions,Quiz


'''
@TODO:
Create an endpoint to handle GET requests
for all available categories.
'''
api.add_resource(CategoryList,'/categories')

'''
@TODO:
Create an endpoint to handle GET requests for questions,
including pagination (every 10 questions).
This endpoint should return a list of questions,
number of total questions, current category, categories.

TEST: At this point, when you start the application
you should see questions and categories generated,
ten questions per page and pagination at the bottom of the screen for three pages.
Clicking on the page numbers should update the questions.
'''


'''
@TODO:
Create an endpoint to DELETE question using a question ID.

TEST: When you click the trash icon next to a question, the question will be removed.
This removal will persist in the database and when you refresh the page.
'''
api.add_resource(DeleteQuestion,'/questions/<int:id>')
'''
@TODO:
Create an endpoint to POST a new question,
which will require the question and answer text,
category, and difficulty score.

TEST: When you submit a question on the "Add" tab,
the form will clear and the question will appear at the end of the last page
of the questions list in the "List" tab.
'''
api.add_resource(Question,'/questions')

'''
@TODO:
Create a POST endpoint to get questions based on a search term.
It should return any questions for whom the search term
is a substring of the question.

TEST: Search by any phrase. The questions list will update to include
only question that include that string within their question.
Try using the word "title" to start.
'''

api.add_resource(SearchQuestions,'/questions/search')
'''
@TODO:
Create a GET endpoint to get questions based on category.

TEST: In the "List" tab / main screen, clicking on one of the
categories in the left column will cause only questions of that
category to be shown.
'''
api.add_resource( CategoryQuestions,'/categories/<int:id>/questions')

'''
@TODO:
Create a POST endpoint to get questions to play the quiz.
This endpoint should take category and previous question parameters
and return a random questions within the given category,
if provided, and that is not one of the previous questions.

TEST: In the "Play" tab, after a user selects "All" or a category,
one question at a time is displayed, the user is allowed to answer
and shown whether they were correct or not.
'''
api.add_resource( Quiz,'/quizzes')


'''
@TODO:
Create error handlers for all expected errors
including 404 and 422.
'''

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({
        "success":False,
        "error":404,
        "message":"Not found",
    }), 404

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success":False,
        "error":422,
        "message":"unprocessable",
    }),422
