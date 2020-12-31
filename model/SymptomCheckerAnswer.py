from run import db
from model.user import UserModel


class SymptomCheckerAnswerModel(db.Model):
    __tablename__ = 'SymptomCheckerAnswer'

    SCA_id = db.Column(db.Integer, primary_key=True)
    SCA_Ans =  db.Column(db.String(120))
    SCA_qid = db.Column(db.Integer)

    def __init__(self, SCA_id, SCA_Ans):

        self.SCA_id = SCA_id
        self.SCA_Ans = SCA_Ans

    def json(self):
        return{

        'SCA_id' : self.SCA_id,
        'SCA_Ans' : self.SCA_Ans,
        }



    @classmethod
    def find_by_id(cls, SCA_user_id):
        return cls.query.filter_by(SCA_user_id = SCA_user_id).first()

    @classmethod
    def find_by_answer_id(cls, SCA_qid):
        return cls.query.filter_by(SCA_qid = SCA_qid).all()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
