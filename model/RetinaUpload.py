from run import db
from model.user import UserModel

class RetinaUploadModel(db.Model):
    __tablename__ = 'RetinaReport'

    RU_id = db.Column(db.Integer,primary_key=True)
    RU_user_id  = db.Column(db.Integer,db.ForeignKey('users.u_id'))
    RU_name = db.Column(db.String(300))
    RU_prediction = db.Column(db.String(300))
    RU_accuracy = db.Column(db.Float)
    RU_report = db.Column(db.LargeBinary(length=(2**32)-1))
    #report = db.Column(db.String(300))

    users = db.relationship('UserModel')

    def __init__(self,RU_user_id,RU_name,RU_prediction,RU_accuracy,RU_report):

                 self.RU_user_id = RU_user_id
                 self.RU_name = RU_name
                 self.RU_prediction = RU_prediction
                 self.RU_accuracy = RU_accuracy
                 self.RU_report = RU_report



    def json(self):
        return{
                 'RU_name' : self.RU_name,
                 'RU_prediction' : self.RU_prediction,
                 'RU_accuracy' : self.RU_accuracy,


        }
    @classmethod
    def find_by_id(cls, RU_user_id):
        return cls.query.filter_by(RU_user_id = RU_user_id).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
