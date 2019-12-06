from flaskr import ma 
from flaskr.models.category import CategoryModel
from flaskr.models.question import QuestionModel
from flaskr.schemas.question import QuestionSchema

class CategorySchema(ma.ModelSchema):

    class Meta:
        model=CategoryModel
        dump_only=("id",)
        load_only=("questions",)
        include_fk=True

class CategoryQuestionsSchema(ma.ModelSchema):
    questions=ma.Nested(QuestionSchema,many=True)

    class Meta:
        model=QuestionModel
        include_fk=True




