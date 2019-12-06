from flaskr import db

class CategoryModel(db.Model):  
  __tablename__ = 'categories'
  id = db.Column(db.Integer, primary_key=True)
  type = db.Column(db.String,unique=True)
  questions = db.relationship("QuestionModel", lazy="dynamic")

  @classmethod
  def find_by_id(cls,id):
      return cls.query.filter_by(id=id).first()
  
  @classmethod
  def find_all(cls):
      return cls.query.all()



  def __repr__(self):
    return f'<{self.type}>'
