from run import db
from model.user import UserModel

class MedicineModel(db.Model):

    __tablename__ = 'Medicine'

    MD_id = db.Column(db.Integer, primary_key=True)
    MD_user_id = db.Column(db.Integer,db.ForeignKey('users.u_id'))
    MD_Date = db.Column(db.Date)
    MD_Time = db.Column(db.Time)
    MD_Name = db.Column(db.String(120))
    MD_Quantity = db.Column(db.Integer)

    users = db.relationship('UserModel')


    def __init__(self,MD_user_id,MD_Date,MD_Time,MD_Name,MD_Quantity):

        self.MD_user_id = MD_user_id
        self.MD_Date = MD_Date
        self.MD_Time = MD_Time
        self.MD_Name = MD_Name
        self.MD_Quantity = MD_Quantity


    def json(self):
        return{
        'MD_Date': str(self.MD_Date),
        'MD_Time': str(self.MD_Time),
        'MD_Name': self.MD_Name,
        'MD_Quantity': self.MD_Quantity,
        }



    @classmethod
    def find_by_id(cls, MD_user_id):
        return cls.query.filter_by(MD_user_id = MD_user_id).first()

    @classmethod
    def find_by_today(cls, MD_Date):
        return cls.query.filter_by(MD_Date = MD_Date).all()



    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
