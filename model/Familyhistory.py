from run import db
from model.user import UserModel

class FamilyHistoryModel(db.Model):
    __tablename__ = 'FamilyHistory'


    FH_id = db.Column(db.Integer, primary_key=True)
    FH_user_id  = db.Column(db.Integer,db.ForeignKey('users.u_id'))
    FH_Member = db.Column(db.String(120), nullable = False)
    FH_Alcoholism = db.Column(db.String(120), nullable = False)
    FH_Allergies= db.Column(db.String(120), nullable = False)
    FH_Anesthesia= db.Column(db.String(120), nullable = False)
    FH_Anxiety= db.Column(db.String(120), nullable = False)
    FH_Arthritis = db.Column(db.String(120), nullable = False)
    FH_Asthma = db.Column(db.String(120), nullable = False)
    FH_ADHD = db.Column(db.String(120), nullable = False)
    FH_Birth_Defects = db.Column(db.String(120), nullable = False)
    FH_Blood_Problem = db.Column(db.String(120), nullable = False)
    FH_Bone_Joint_Problems = db.Column(db.String(120), nullable = False)
    FH_Breast_Disease = db.Column(db.String(120), nullable = False)
    FH_Cancer = db.Column(db.String(120), nullable = False)
    FH_Chicken_Pox = db.Column(db.String(120), nullable = False)
    FH_Colitis = db.Column(db.String(120), nullable = False)
    FH_Depression = db.Column(db.String(120), nullable = False)
    FH_Diabetes = db.Column(db.String(120), nullable = False)
    FH_ENT_Problems = db.Column(db.String(120), nullable = False)
    FH_Eating_Disorders = db.Column(db.String(120), nullable = False)
    FH_Eczema = db.Column(db.String(120), nullable = False)
    FH_Epilepsy = db.Column(db.String(120), nullable = False)
    FH_Fertility = db.Column(db.String(120), nullable = False)
    FH_Gallbladder = db.Column(db.String(120), nullable = False)
    FH_Gynecology = db.Column(db.String(120), nullable = False)
    FH_Fever = db.Column(db.String(120), nullable = False)
    FH_Headaches = db.Column(db.String(120), nullable = False)
    FH_Heart_Problems = db.Column(db.String(120), nullable = False)
    FH_Heart_Attack_Over_60 = db.Column(db.String(120), nullable = False)
    FH_Heart_Attack_Under_60 = db.Column(db.String(120), nullable = False)
    FH_Heart_Murmur = db.Column(db.String(120), nullable = False)
    FH_Hepatitis = db.Column(db.String(120), nullable = False)
    FH_High_Blood_Pressure = db.Column(db.String(120), nullable = False)
    FH_High_Cholestorol  = db.Column(db.String(120), nullable = False)

    users = db.relationship('UserModel')

    def __init__(self,FH_user_id,FH_Member, FH_Alcoholism, FH_Allergies, FH_Anesthesia, FH_Anxiety, FH_Arthritis, FH_Asthma, FH_ADHD, FH_Birth_Defects, FH_Blood_Problem,
                 FH_Bone_Joint_Problems, FH_Breast_Disease, FH_Cancer, FH_Chicken_Pox, FH_Colitis, FH_Depression, FH_Diabetes, FH_ENT_Problems, FH_Eating_Disorders, FH_Eczema, FH_Epilepsy,
                 FH_Fertility, FH_Gallbladder, FH_Gynecology, FH_Fever, FH_Headaches, FH_Heart_Problems, FH_Heart_Attack_Over_60, FH_Heart_Attack_Under_60, FH_Heart_Murmur, FH_Hepatitis,
                 FH_High_Blood_Pressure, FH_High_Cholestorol):

                 self.FH_user_id = FH_user_id
                 self.FH_Member = FH_Member
                 self.FH_Alcoholism = FH_Alcoholism
                 self.FH_Allergies = FH_Allergies
                 self.FH_Anesthesia = FH_Anesthesia
                 self.FH_Anxiety = FH_Anxiety
                 self.FH_Arthritis = FH_Arthritis
                 self.FH_Asthma = FH_Asthma
                 self.FH_ADHD = FH_ADHD
                 self.FH_Birth_Defects = FH_Birth_Defects
                 self.FH_Blood_Problem = FH_Blood_Problem
                 self.FH_Bone_Joint_Problems = FH_Bone_Joint_Problems
                 self.FH_Breast_Disease = FH_Breast_Disease
                 self.FH_Cancer = FH_Cancer
                 self.FH_Chicken_Pox = FH_Chicken_Pox
                 self.FH_Colitis = FH_Colitis
                 self.FH_Depression = FH_Depression
                 self.FH_Diabetes = FH_Diabetes
                 self.FH_ENT_Problems = FH_ENT_Problems
                 self.FH_Eating_Disorders = FH_Eating_Disorders
                 self.FH_Eczema = FH_Eczema
                 self.FH_Epilepsy = FH_Epilepsy
                 self.FH_Fertility = FH_Fertility
                 self.FH_Gallbladder = FH_Gallbladder
                 self.FH_Gynecology = FH_Gynecology
                 self.FH_Fever = FH_Fever
                 self.FH_Headaches = FH_Headaches
                 self.FH_Heart_Problems = FH_Heart_Problems
                 self.FH_Heart_Attack_Over_60 = FH_Heart_Attack_Over_60
                 self.FH_Heart_Attack_Under_60 = FH_Heart_Attack_Under_60
                 self.FH_Heart_Murmur = FH_Heart_Murmur
                 self.FH_Hepatitis = FH_Hepatitis
                 self.FH_High_Blood_Pressure = FH_High_Blood_Pressure
                 self.FH_High_Cholestorol = FH_High_Cholestorol



    def json(self):
         return{
         'FH_Member' : self.FH_Member,
         'FH_Alcoholism' : self.FH_Alcoholism,
         'FH_Allergies': self.FH_Allergies,
         'FH_Anesthesia': self.FH_Anesthesia,
         'FH_Anxiety': self.FH_Anxiety,
         'FH_Arthritis': self.FH_Arthritis,
         'FH_Asthma': self.FH_Asthma,
         'FH_ADHD': self.FH_ADHD,
         'FH_Birth_Defects': self.FH_Birth_Defects,
         'FH_Blood_Problem': self.FH_Blood_Problem,
         'FH_Bone_Joint_Problems': self.FH_Bone_Joint_Problems,
         'FH_Breast_Disease': self.FH_Breast_Disease,
         'FH_Cancer' : self.FH_Cancer,
         'FH_Chicken_Pox': self.FH_Chicken_Pox,
         'FH_Colitis': self.FH_Colitis,
         'FH_Depression': self.FH_Depression,
         'FH_Diabetes': self.FH_Diabetes,
         'FH_ENT_Problems': self.FH_ENT_Problems,
         'FH_Eating_Disorders': self.FH_Eating_Disorders,
         'FH_Eczema' : self.FH_Eczema,
         'FH_Epilepsy': self.FH_Epilepsy,
         'FH_Fertility': self.FH_Fertility,
         'FH_Gallbladder': self.FH_Gallbladder,
         'FH_Gynecology': self.FH_Gynecology,
         'FH_Fever' : self.FH_Fever,
         'FH_Headaches': self.FH_Headaches,
         'FH_Heart_Problems': self.FH_Heart_Problems,
         'FH_Heart_Attack_Over_60': self.FH_Heart_Attack_Over_60,
         'FH_Heart_Attack_Under_60': self.FH_Heart_Attack_Under_60,
         'FH_Heart_Murmur': self.FH_Heart_Murmur,
         'FH_Hepatitis': self.FH_Hepatitis,
         'FH_High_Blood_Pressure': self.FH_High_Blood_Pressure,
         'FH_High_Cholestorol': self.FH_High_Cholestorol
}



    @classmethod
    def find_by_id(cls, FH_user_id):
        return cls.query.filter_by(FH_user_id = FH_user_id).first()


    @classmethod
    def find_by_FH_Member(cls, FH_Member):
        return cls.query.filter_by(FH_Member = FH_Member).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
