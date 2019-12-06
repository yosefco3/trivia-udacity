from flask_restful import Resource, request
from flask import abort
from marshmallow import ValidationError
from flaskr.models.category import CategoryModel
from flaskr.schemas.category import CategorySchema,CategoryQuestionsSchema
from config import QUESTIONS_PER_PAGE

category_schema=CategorySchema()
category_list_schema=CategorySchema(many=True)
category_questions_schema=CategoryQuestionsSchema(many=True)

class Category(Resource):
    @classmethod
    def get(cls,id):
        category=CategoryModel.find_by_id(id)
        if category:
            return category_schema.dump(category),200
        return {"message":"Category not found"} , 404

class CategoryList(Resource):
    @classmethod
    def get(cls):
        try:
            categories=CategoryModel.find_all()
        except:
            return {"message":"categories not found"}, 404
        return {"categories":category_list_schema.dump(categories)}, 200
        
        

class CategoryQuestions(Resource):
    @classmethod
    def get(cls,id):
        '''
        Create a GET endpoint to get questions based on category. 
        '''
        page_num=request.args.get("page",1,type=int) 

        category=CategoryModel.find_by_id(id)
        if category:
            try:
                questions=category.questions.paginate(page=page_num,per_page=QUESTIONS_PER_PAGE)
                current_page=questions.page
                total_questions=questions.total
                print(questions.items)

                return {
                    "current_page":current_page,
                    "total_questions":total_questions,
                    "current_category":category.type,
                    "category_id":category.id,
                    "questions": category_questions_schema.dump(questions.items)

                },200
            except:
                return {"message":"questions not found"} , 404
            # return category_questions_schema.dump(category) ,200
        return {"message":"Category not found"},404

