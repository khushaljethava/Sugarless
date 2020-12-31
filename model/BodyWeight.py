from run import db
from model.user import UserModel

class BodyWeightModel(db.Model):
    __tablename__ = 'BodyWeight'

    BW_id = db.Column(db.Integer, primary_key=True)
    BW_user_id = db.Column(db.Integer, db.ForeignKey('users.u_id'))
    BW_Value = db.Column(db.Float)
    BW_Date = db.Column(db.Date)
    BW_Time = db.Column(db.Time)

    users = db.relationship('UserModel')

    def __init__(self, BW_user_id,BW_Value,BW_Date,BW_Time):
         self.BW_user_id = BW_user_id
         self.BW_Value = BW_Value
         self.BW_Date = BW_Date
         self.BW_Time = BW_Time



    def json(self):
        return {
        'BW_Value' : self.BW_Value,
        'BW_Date' : str(self.BW_Date),
        'BW_Time' : str(self.BW_Time),
        }



    @classmethod
    def find_by_id(cls, BW_user_id):
        return cls.query.filter_by(BW_user_id = BW_user_id).first()

    @classmethod
    def find_by_today(cls, BW_Date):
        return cls.query.filter_by(BW_Date = BW_Date).all()



    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
