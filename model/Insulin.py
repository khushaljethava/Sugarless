from run import db
from model.user import UserModel

class InsulinModel(db.Model):
    __tablename__ = 'Insulin'

    IN_id = db.Column(db.Integer, primary_key=True)
    IN_user_id = db.Column(db.Integer, db.ForeignKey('users.u_id'))
    IN_Value = db.Column(db.Float)
    IN_Date = db.Column(db.Date)
    IN_Time = db.Column(db.Time)
    users = db.relationship('UserModel')


    def __init__(self,IN_user_id,IN_Value,IN_Date,IN_Time):
        self.IN_user_id = IN_user_id
        self.IN_Value = IN_Value
        self.IN_Date = IN_Date
        self.IN_Time = IN_Time


    def json(self):
        return {
        'IN_Value' : self.IN_Value,
        'IN_Date' : str(self.IN_Date),
        'IN_Time' : str(self.IN_Time),
        }



    @classmethod
    def find_by_id(cls, IN_user_id):
        return cls.query.filter_by(IN_user_id = IN_user_id).first()

    @classmethod
    def find_by_today(cls, IN_Date):
        return cls.query.filter_by(IN_Date = IN_Date).all()



    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
