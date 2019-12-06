from flaskr import app,db
from flaskr.models.category import CategoryModel

#
# 
class QuestionModel(db.Model):  
  __tablename__ = 'questions'

  id = db.Column(db.Integer, primary_key=True)
  question = db.Column(db.String)
  answer = db.Column(db.String)
  difficulty = db.Column(db.Integer)
  category=db.Column(db.Integer,db.ForeignKey('categories.id'))
  



  @classmethod
  def find_by_id(cls,id):
    return cls.query.filter_by(id=id).first()
  
  @classmethod
  def search(cls,searchterm):
    return cls.query.filter(cls.question.ilike("%" + searchterm + "%")).all()

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()
  
  
  def __repr__(self):
    return f'<{self.question} - {self.category}>'
