from flaskr import ma 
from flaskr.models.question import QuestionModel


class QuestionSchema(ma.ModelSchema):
    class Meta:
        model=QuestionModel
        dump_only=("id",)
        include_fk=True
    

        


        
        


