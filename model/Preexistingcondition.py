from run import db
from model.user import UserModel



class PreConditionModel(db.Model):
    __tablename__ = 'PreexistingCondition'

    PC_id = db.Column(db.Integer, primary_key=True)
    PC_user_id = db.Column(db.Integer,db.ForeignKey('users.u_id'))
    PC_Race = db.Column(db.String(120), nullable = False)
    PC_Smoking = db.Column(db.String(120), nullable = False)
    PC_Alcohol = db.Column(db.String(120), nullable = False)
    PC_Diabetes = db.Column(db.String(120), nullable = False)
    PC_Hear = db.Column(db.String(120), nullable = False)
    PC_Blood_Pressure = db.Column(db.String(120), nullable = False)
    PC_Chest_Pain = db.Column(db.String(120), nullable = False)
    PC_Stroke =  db.Column(db.String(120), nullable = False)
    PC_Kidney  = db.Column(db.String(120), nullable = False)
    PC_Blood_Clot = db.Column(db.String(120), nullable = False)
    PC_Metal_implants = db.Column(db.String(120), nullable = False)
    PC_Asthma = db.Column(db.String(120), nullable = False)
    PC_Cancer = db.Column(db.String(120), nullable = False)
    PC_Difficulty_Swallowing = db.Column(db.String(120), nullable = False)
    PC_Vascular_Problems = db.Column(db.String(120), nullable = False)
    PC_Peripheral_Neuropathy = db.Column(db.String(120), nullable = False)
    PC_Weightloss = db.Column(db.String(120), nullable = False)
    PC_Double_Vision = db.Column(db.String(120), nullable = False)
    PC_Night_Sweats = db.Column(db.String(120), nullable = False)
    PC_Night_Pain = db.Column(db.String(120), nullable = False)
    PC_Neurologic_Condition = db.Column(db.String(120), nullable = False)
    PC_Skin_Disease = db.Column(db.String(120), nullable = False)
    PC_Spinal_Cord_Injury = db.Column(db.String(120), nullable = False)
    PC_Degenerative_Joint_Disease = db.Column(db.String(120), nullable = False)
    PC_Sexual_Dysfunction = db.Column(db.String(120), nullable = False)
    PC_Bladder = db.Column(db.String(120), nullable = False)
    PC_Groin_Numbness = db.Column(db.String(120), nullable = False)
    PC_Arthritis = db.Column(db.String(120), nullable = False)
    PC_Osteoporosis = db.Column(db.String(120), nullable = False)
    PC_Phsychological_Problems = db.Column(db.String(120), nullable = False)
    PC_Seizures = db.Column(db.String(120), nullable = False)
    PC_Dizziness = db.Column(db.String(120), nullable = False)
    PC_Ringing_in_Ears = db.Column(db.String(120), nullable = False)
    PC_Allergy_to_Latex   = db.Column(db.String(120), nullable = False)
    PC_Head_Injury = db.Column(db.String(120), nullable = False)
    PC_Obesity = db.Column(db.String(120), nullable = False)
    PC_Chronic_Pain = db.Column(db.String(120), nullable = False)
    PC_Fractures  = db.Column(db.String(120), nullable = False)
    PC_Infection_Dissease  = db.Column(db.String(120), nullable = False)
    PC_Fever = db.Column(db.String(120), nullable = False)
    PC_Lower_Extremety = db.Column(db.String(120), nullable = False)
    PC_Nausea = db.Column(db.String(120), nullable = False)

    users = db.relationship('UserModel')


    def __init__(self,PC_user_id,PC_Race, PC_Smoking, PC_Alcohol, PC_Diabetes, PC_Hear, PC_Blood_Pressure, PC_Chest_Pain, PC_Stroke,
         PC_Kidney, PC_Blood_Clot, PC_Metal_implants, PC_Asthma, PC_Cancer, PC_Difficulty_Swallowing, PC_Vascular_Problems,
         PC_Peripheral_Neuropathy, PC_Weightloss, PC_Double_Vision, PC_Night_Sweats, PC_Night_Pain, PC_Neurologic_Condition,
          PC_Skin_Disease, PC_Spinal_Cord_Injury, PC_Degenerative_Joint_Disease, PC_Sexual_Dysfunction, PC_Bladder,
          PC_Groin_Numbness, PC_Arthritis, PC_Osteoporosis, PC_Phsychological_Problems, PC_Seizures, PC_Dizziness,
          PC_Ringing_in_Ears, PC_Allergy_to_Latex, PC_Head_Injury, PC_Obesity, PC_Chronic_Pain, PC_Fractures,
          PC_Infection_Dissease, PC_Fever, PC_Lower_Extremety, PC_Nausea):


        self.PC_user_id = PC_user_id
        self.PC_Race = PC_Race
        self.PC_Smoking = PC_Smoking
        self.PC_Alcohol = PC_Alcohol
        self.PC_Diabetes = PC_Diabetes
        self.PC_Hear = PC_Hear
        self.PC_Blood_Pressure = PC_Blood_Pressure
        self.PC_Chest_Pain = PC_Chest_Pain
        self.PC_Stroke =  PC_Stroke
        self.PC_Kidney  = PC_Kidney
        self.PC_Blood_Clot = PC_Blood_Clot
        self.PC_Metal_implants = PC_Metal_implants
        self.PC_Asthma = PC_Asthma
        self.PC_Cancer = PC_Cancer
        self.PC_Difficulty_Swallowing = PC_Difficulty_Swallowing
        self.PC_Vascular_Problems = PC_Vascular_Problems
        self.PC_Peripheral_Neuropathy = PC_Peripheral_Neuropathy
        self.PC_Weightloss = PC_Weightloss
        self.PC_Double_Vision = PC_Double_Vision
        self.PC_Night_Sweats = PC_Night_Sweats
        self.PC_Night_Pain = PC_Night_Pain
        self.PC_Neurologic_Condition = PC_Neurologic_Condition
        self.PC_Skin_Disease = PC_Skin_Disease
        self.PC_Spinal_Cord_Injury = PC_Spinal_Cord_Injury
        self.PC_Degenerative_Joint_Disease = PC_Degenerative_Joint_Disease
        self.PC_Sexual_Dysfunction = PC_Sexual_Dysfunction
        self.PC_Bladder = PC_Bladder
        self.PC_Groin_Numbness = PC_Groin_Numbness
        self.PC_Arthritis = PC_Arthritis
        self.PC_Osteoporosis = PC_Osteoporosis
        self.PC_Phsychological_Problems = PC_Phsychological_Problems
        self.PC_Seizures = PC_Seizures
        self.PC_Dizziness = PC_Dizziness
        self.PC_Ringing_in_Ears = PC_Ringing_in_Ears
        self.PC_Allergy_to_Latex   = PC_Allergy_to_Latex
        self.PC_Head_Injury = PC_Head_Injury
        self.PC_Obesity = PC_Obesity
        self.PC_Chronic_Pain = PC_Chronic_Pain
        self.PC_Fractures  = PC_Fractures
        self.PC_Infection_Dissease  = PC_Infection_Dissease
        self.PC_Fever = PC_Fever
        self.PC_Lower_Extremety = PC_Lower_Extremety
        self.PC_Nausea = PC_Nausea

    def json(self):
        return {
        'PC_Race' : self.PC_Race,
        'PC_Smoking' : self.PC_Smoking,
        'PC_Alcohol' :  self.PC_Alcohol,
        'PC_Diabetes' : self.PC_Diabetes,
        'PC_Hear' :  self.PC_Hear,
        'PC_Blood_Pressure' :  self.PC_Blood_Pressure,
        'PC_Chest_Pain' :  self.PC_Chest_Pain,
        'PC_Stroke' : self.PC_Stroke,
        'PC_Kidney': self.PC_Kidney,
        'PC_Blood_Clot' : self.PC_Blood_Clot,
        'PC_Metal_implants': self.PC_Metal_implants,
        'PC_Asthma': self.PC_Asthma,
        'PC_Cancer': self.PC_Cancer,
        'PC_Difficulty_Swallowing': self.PC_Difficulty_Swallowing,
        'PC_Vascular_Problems' : self.PC_Vascular_Problems,
        'PC_Peripheral_Neuropathy': self.PC_Peripheral_Neuropathy,
        'PC_Weightloss': self.PC_Weightloss,
        'PC_Double_Vision': self.PC_Double_Vision,
        'PC_Night_Sweats': self.PC_Night_Sweats,
        'PC_Night_Pain' : self.PC_Night_Pain,
        'PC_Neurologic_Condition': self.PC_Neurologic_Condition,
        'PC_Skin_Disease': self.PC_Skin_Disease,
        'PC_Spinal_Cord_Injury': self.PC_Spinal_Cord_Injury,
        'PC_Degenerative_Joint_Disease': self.PC_Degenerative_Joint_Disease,
        'PC_Sexual_Dysfunction': self.PC_Sexual_Dysfunction,
        'PC_Bladder': self.PC_Bladder,
        'PC_Groin_Numbness': self.PC_Groin_Numbness,
        'PC_Arthritis': self.PC_Arthritis,
        'PC_Osteoporosis': self.PC_Osteoporosis,
        'PC_Phsychological_Problems': self.PC_Phsychological_Problems,
        'PC_Seizures': self.PC_Seizures,
        'PC_Dizziness': self.PC_Dizziness,
        'PC_Ringing_in_Ears': self.PC_Ringing_in_Ears,
        'PC_Allergy_to_Latex': self.PC_Allergy_to_Latex,
        'PC_Head_Injury': self.PC_Head_Injury,
        'PC_Obesity': self.PC_Obesity,
        'PC_Chronic_Pain': self.PC_Chronic_Pain,
        'PC_Fractures': self.PC_Fractures,
        'PC_Infection_Dissease': self.PC_Infection_Dissease,
        'PC_Fever': self.PC_Fever,
        'PC_Lower_Extremety': self.PC_Lower_Extremety,
        'PC_Nausea': self.PC_Nausea
}


    @classmethod
    def find_by_id(cls, PC_user_id):
        return cls.query.filter_by(PC_user_id = PC_user_id).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
