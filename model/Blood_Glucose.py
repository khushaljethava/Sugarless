from run import db
from model.user import UserModel

class BloodGlucoseModel(db.Model):
    __tablename__ = 'BloodGlucose'
    BG_id = db.Column(db.Integer, primary_key=True)
    BG_user_id = db.Column(db.Integer,db.ForeignKey('users.u_id'))
    BG_Value = db.Column(db.Float)
    BG_Date = db.Column(db.Date)
    BG_Time = db.Column(db.Time)

    users = db.relationship('UserModel')

    def __init__(self, BG_user_id, BG_Value, BG_Date, BG_Time):

        self.BG_user_id = BG_user_id
        self.BG_Value = BG_Value
        self.BG_Date = BG_Date
        self.BG_Time = BG_Time


    def json(self):
        return {
        'BG_Value' : self.BG_Value,
        'BG_Date' : str(self.BG_Date),
        'BG_Time' : str(self.BG_Time),

        }





    @classmethod
    def find_by_id(cls, BG_user_id):
        return cls.query.filter_by(BG_user_id = BG_user_id).first()

    @classmethod
    def find_by_today(cls, BG_Date):
        return cls.query.filter_by(BG_Date = BG_Date).all()




    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
