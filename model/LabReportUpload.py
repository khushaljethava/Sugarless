from run import db
from model.user import UserModel

class LabReportUploadModel(db.Model):
    __tablename__ = 'LabReportFiles'

    LR_id = db.Column(db.Integer,primary_key=True)
    LR_user_id  = db.Column(db.Integer,db.ForeignKey('users.u_id'))
    LR_name = db.Column(db.String(300))
    LR_report = db.Column(db.LargeBinary(length=(2**32)-1))

    users = db.relationship('UserModel')

    def __init__(self,LR_user_id,LR_name,LR_report):

                 self.LR_user_id = LR_user_id
                 self.LR_name = LR_name
                 self.LR_report = LR_report




    @classmethod
    def find_by_id(cls, LR_user_id):
        return cls.query.filter_by(LR_user_id = LR_user_id).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
