from random import shuffle

from flask import abort
from flask_restful import Resource,request
from marshmallow import ValidationError
from flaskr.models.question import QuestionModel
from flaskr.schemas.question import QuestionSchema
from flaskr.models.category import CategoryModel
from flaskr.resources.category import category_list_schema
from config import QUESTIONS_PER_PAGE , QUESTIONS_PER_GAME

question_schema=QuestionSchema()
question_list_schema=QuestionSchema(many=True)



class Question(Resource):

    @classmethod
    def convert_category_name_to_id(cls,json_obj):
        '''
        helper method to convert category name to category id
        '''
        categories=CategoryModel.find_all()
        json_obj['category']=[x.id for x in categories if x.type.lower()==json_obj['category']][0]      
        return json_obj


    @classmethod
    def post(cls):
        '''
        Create an endpoint to POST a new question, 
        which will require the question and answer text, 
        category, and difficulty score.

        '''
        question_json=request.get_json()
        question_json=cls.convert_category_name_to_id(question_json)
        if not question_json:
            return {"message":"there isn't such category."} ,422
        
        try:
            question=question_schema.load(question_json)
        except ValidationError as err:
            return err.messages,400

        try:
            question.insert()
        except:
            return {"message":"An error occured while inserting the question"} , 500
        return question_schema.dump(question),201


    @classmethod    
    def get(cls):
        '''
        Create an endpoint to handle GET requests for questions, 
        including pagination (every 10 questions). 
        This endpoint should return a list of questions, 
        number of total questions, current category, categories. 

        '''
        page_num=request.args.get("page",1,type=int) 
        try:
            questions=QuestionModel.query.paginate(page=page_num,per_page=QUESTIONS_PER_PAGE)
            current_page=questions.page
            total_questions=questions.total
            categories=CategoryModel.find_all()
            

            return {"current page":current_page,
                    "total_questions":total_questions,
                    "categories":category_list_schema.dump(categories),
                    "questions":question_list_schema.dump(questions.items)} , 200
        except:
            return {"message":"questions not found"} , 404


        

class DeleteQuestion(Resource):
    @classmethod
    def delete(cls,id):
        '''
        Create an endpoint to DELETE question using a question ID.
        '''
        question=QuestionModel.find_by_id(id)
        if question:
            question.delete()
            return {"message":"question removed"} , 200
        return {"message":"question not found"} , 404

    
class SearchQuestions(Resource):
    @classmethod
    def post(cls):
        '''
        Create a POST endpoint to get questions based on a search term. 
        It should return any questions for whom the search term 
        is a substring of the question. 
        '''
        searchterm=request.get_json()['searchterm']
        if not searchterm:
            return {"message":"search term couldn't be empty"}
        questions = QuestionModel.search(searchterm)
        if questions:
            return {"questions":question_list_schema.dump(questions)} , 200
        else:
            return {"message": f'Questions with the word "{searchterm}" have not found' } , 404


class Quiz(Resource):
    @classmethod
    def post(cls):
        '''
        Create a POST endpoint to get questions to play the quiz. 
        This endpoint should take category and previous question parameters 
        and return a random questions within the given category, 
        if provided, and that is not one of the previous questions. 
        '''
        quiz_data=request.get_json()
        print(quiz_data)
        if quiz_data['category']:
            category=CategoryModel.find_by_id(quiz_data['category'])
            questions=category.questions.all()
        else:
            questions=QuestionModel.query.all()
        # print(questions) 
        if questions:
            # shuffling the questions so the game wouldnt be the same
            shuffle(questions)
            # print(questions)
            questions = questions[:QUESTIONS_PER_GAME]
            # print(questions)
        else:
            return {"message":"no more questions in that category"} , 404
        return {"questions": question_list_schema.dump(questions)} ,200

        





        
        
