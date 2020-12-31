from run import db
from model.user import UserModel

class StepsModel(db.Model):
    __tablename__ = 'Steps'

    ST_id = db.Column(db.Integer, primary_key=True)
    ST_user_id = db.Column(db.Integer, db.ForeignKey('users.u_id'))
    ST_Value = db.Column(db.Integer)
    ST_Date = db.Column(db.Date)
    ST_Time = db.Column(db.Time)
    ST_TimeTaken = db.Column(db.Float)
    ST_Calories = db.Column(db.Float)

    users = db.relationship('UserModel')

    def __init__(self,ST_user_id,ST_Value,ST_Date,ST_Time,ST_TimeTaken,ST_Calories):

        self.ST_user_id = ST_user_id
        self.ST_Value = ST_Value
        self.ST_Date = ST_Date
        self.ST_Time = ST_Time
        self.ST_TimeTaken = ST_TimeTaken
        self.ST_Calories = ST_Calories


    def json(self):
        return{
        'ST_Value' : self.ST_Value,
        'ST_Date' : str(self.ST_Date),
        'ST_Time' : str(self.ST_Time),
        'ST_TimeTaken' : self.ST_TimeTaken,
        }



    @classmethod
    def find_by_id(cls, ST_user_id):
        return cls.query.filter_by(ST_user_id = ST_user_id).first()

    @classmethod
    def find_by_today(cls, ST_Date):
        return cls.query.filter_by(ST_Date = ST_Date).all()



    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
