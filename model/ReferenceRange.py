from run import db

class ReferenceRangeModel(db.Model):
    __tablename__ = 'ReferenceRange'

    RR_id = db.Column(db.Integer, primary_key=True)
    RR_ProcessedBy = db.Column(db.String(120) )
    RR_Category = db.Column(db.String(120))
    RR_Lab_Test = db.Column(db.String(120))
    RR_Technology = db.Column(db.String(120))
    RR_Units = db.Column(db.String(120))
    RR_Age_Less = db.Column(db.Integer)
    RR_Age_More = db.Column(db.Integer)
    RR_gender = db.Column(db.String(120))
    RR_Range_Low = db.Column(db.Float)
    RR_Range_High = db.Column(db.Float)
    RR_Race = db.Column(db.String(120))
    RR_Location = db.Column(db.String(120))



    def __init__(self,RR_ProcessedBy,RR_Category,RR_Lab_Test,RR_Technology,RR_Units,RR_Age_Less,RR_Age_More,RR_gender,RR_Range_Low,RR_Range_High,RR_Race,RR_Location):

        self.RR_ProcessedBy = RR_ProcessedBy
        self.RR_Category = RR_Category
        self.RR_Lab_Test = RR_Lab_Test
        self.RR_Technology = RR_Technology
        self.RR_Age_Less = RR_Age_Less
        self.RR_Age_More = RR_Age_More
        self.RR_gender = RR_gender
        self.RR_Range_Low = RR_Range_Low
        self.RR_Range_High = RR_Range_High
        self.RR_Race = RR_Race
        self.RR_Location = RR_Location




    @classmethod
    def find_by_id(cls, RR_id):
        return cls.query.filter_by(RR_id = RR_id).first()

    @classmethod
    def Compare_IRON(cls):
#        Low_Range = db.select([ReferenceRangeModel.RR_Range_Low]).where(ReferenceRangeModel.RR_Lab_Test == 'Iron')
#        Low_Range = cls.query.filter([ReferenceRangeModel.RR_Range_Low]).where(ReferenceRangeModel.RR_Lab_Test =='ALKALINE PHOSPHATASE')
#        Low_Range = cls.query([ReferenceRangeModel.RR_Range_Low]).filter(ReferenceRangeModel.RR_Lab_Test == 'Iron')
#        Low_Range = cls.query(ReferenceRangeModel.RR_Range_Low).filter_by(ReferenceRangeModel.RR_Lab_Test == 'Iron').first()
#        Low_Range = ReferenceRangeModel.select().where(ReferenceRangeModel.RR_Lab_Test == 'ALKALINE PHOSPHATASE')
#        Low_Range = "SELECT RR_Range_Low FROM `ReferenceRange` WHERE RR_Lab_Test = 'ALKALINE PHOSPHATASE'"
#        result = db.session.execute(Low_Range)
        result = db.session.query(ReferenceRangeModel.RR_Range_Low).filter(ReferenceRangeModel.RR_Lab_Test == 'Iron', ReferenceRangeModel.RR_gender=='F').first()

        return result
