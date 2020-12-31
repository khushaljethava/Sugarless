from run import db
from model.user import UserModel

class UserSymptomsInputModel(db.Model):
    __tablename__ = 'user_symptoms_input'

    UI_id = db.Column(db.Integer, primary_key=True)
    UI_SCA_qid = db.Column(db.Integer)
    UI_SCA_aid = db.Column(db.String(120))
    UI_user_id = db.Column(db.Integer, db.ForeignKey('users.u_id'))

    users = db.relationship('UserModel')

    def __init__(self, UI_user_id,UI_SCA_qid,UI_SCA_aid):

        self.UI_SCA_qid = UI_SCA_qid
        self.UI_SCA_aid = UI_SCA_aid
        self.UI_user_id = UI_user_id


    @classmethod
    def find_by_id(cls, UI_SCA_qid):
        return cls.query.filter_by(UI_SCA_qid = UI_SCA_qid).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
