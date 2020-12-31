from run import db
from flask_restful import Resource, reqparse
from model.Familyhistory import FamilyHistoryModel
from flask_jwt_extended import jwt_required


class FamilyHistory(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('FH_Member', help=' FH_Member cannot be blank', required=True)
    parser.add_argument('FH_Alcoholism', help='FH_Alcoholism cannot be blank', required=True)
    parser.add_argument('FH_Allergies', help='FH_Allergies cannot be blank', required=True)
    parser.add_argument('FH_Anesthesia', help='FH_Anesthesia cannot be blank', required=True)
    parser.add_argument('FH_Anxiety', help='FH_Anxiety cannot be blank', required=True)
    parser.add_argument('FH_Arthritis', help='FH_Arthritis cannot be blank', required=True)
    parser.add_argument('FH_Asthma', help='FH_Asthma cannot be blank', required=True)
    parser.add_argument('FH_ADHD', help='FH_ADHD cannot be blank', required=True)
    parser.add_argument('FH_Birth_Defects', help='FH_Birth_Defects cannot be blank', required=True)
    parser.add_argument('FH_Blood_Problem', help=' FH_Blood_Problem cannot be blank', required=True)
    parser.add_argument('FH_Bone_Joint_Problems', help='FH_Bone_Joint_Problems cannot be blank', required=True)
    parser.add_argument('FH_Breast_Disease', help='FH_Breast_Disease cannot be blank', required=True)
    parser.add_argument('FH_Cancer', help='FH_Cancer cannot be blank', required=True)
    parser.add_argument('FH_Chicken_Pox', help='FH_Chicken_Pox cannot be blank', required=True)
    parser.add_argument('FH_Colitis', help='FH_Colitis cannot be blank', required=True)
    parser.add_argument('FH_Depression', help='FH_Depression cannot be blank', required=True)
    parser.add_argument('FH_Diabetes', help='FH_Diabetes cannot be blank', required=True)
    parser.add_argument('FH_ENT_Problems', help='FH_ENT_Problems cannot be blank', required=True)
    parser.add_argument('FH_Eating_Disorders', help=' FH_Eating_Disorders cannot be blank', required=True)
    parser.add_argument('FH_Eczema', help='FH_Eczema cannot be blank', required=True)
    parser.add_argument('FH_Epilepsy', help='FH_Epilepsy cannot be blank', required=True)
    parser.add_argument('FH_Fertility', help='FH_Fertility cannot be blank', required=True)
    parser.add_argument('FH_Gallbladder', help='FH_Gallbladder cannot be blank', required=True)
    parser.add_argument('FH_Gynecology', help='FH_Gynecology cannot be blank', required=True)
    parser.add_argument('FH_Fever', help='FH_Fever cannot be blank', required=True)
    parser.add_argument('FH_Headaches', help='FH_Headaches cannot be blank', required=True)
    parser.add_argument('FH_Heart_Problems', help='FH_Heart_Problems cannot be blank', required=True)
    parser.add_argument('FH_Heart_Attack_Over_60', help='FH_Heart_Attack_Over_60 cannot be blank', required=True)
    parser.add_argument('FH_Heart_Attack_Under_60', help='Heart_Attack_Under_60 cannot be blank', required=True)
    parser.add_argument('FH_Heart_Murmur', help='FH_Heart_Murmur cannot be blank', required=True)
    parser.add_argument('FH_Hepatitis', help='FH_Hepatitis cannot be blank', required=True)
    parser.add_argument('FH_High_Blood_Pressure', help='FH_High_Blood_Pressure cannot be blank', required=True)
    parser.add_argument('FH_High_Cholestorol', help='FH_High_Cholestorol cannot be blank', required=True)

    @jwt_required
    def get(self,FH_user_id,FH_Member):
        familyhistory = FamilyHistoryModel.find_by_id(FH_user_id)
        familyhistory_Member = FamilyHistoryModel.find_by_FH_Member(FH_Member)
        if familyhistory_Member:
            return familyhistory_Member.json()
        else:
            return {
            "Status" : "Error",
            'Response': 'Item not found'
             }, 404

    @jwt_required
    def post(self, FH_user_id, FH_Member):
        if FamilyHistoryModel.find_by_id(FH_user_id) and FamilyHistoryModel.find_by_FH_Member(FH_Member):
            return {
            'Status' : 'Error',
            'Response': 'Item already exists'}
        else:

            data = FamilyHistory.parser.parse_args()

            familyhistory = FamilyHistoryModel(FH_user_id, **data)

            try:

                familyhistory.save_to_db()

            except:

                return {
                'Status': 'Error',
                'Response': 'An Error occurred while saving'}

            return {
            "Status": "Status",
            "Response": familyhistory.json()
            }, 201


    @jwt_required
    def put(self,FH_user_id, FH_Member):
        data = FamilyHistory.parser.parse_args()
        familyhistory = FamilyHistoryModel.find_by_id(FH_user_id)

        if familyhistory:
            familyhistory.FH_Member = data['FH_Member']
            familyhistory.FH_Alcoholism = data['FH_Alcoholism']
            familyhistory.FH_Allergies = data['FH_Allergies']
            familyhistory.FH_Anesthesia = data['FH_Anesthesia']
            familyhistory.FH_Anxiety = data['FH_Anxiety']
            familyhistory.FH_Arthritis = data['FH_Arthritis']
            familyhistory.FH_Asthma = data['FH_Asthma']
            familyhistory.FH_ADHD = data['FH_ADHD']
            familyhistory.FH_Birth_Defects = data['FH_Birth_Defects']
            familyhistory.FH_Blood_Problem = data['FH_Blood_Problem']
            familyhistory.FH_Bone_Joint_Problems = data['FH_Bone_Joint_Problems']
            familyhistory.FH_Breast_Disease = data['FH_Breast_Disease']
            familyhistory.FH_Cancer = data['FH_Cancer']
            familyhistory.FH_Chicken_Pox = data['FH_Chicken_Pox']
            familyhistory.FH_Colitis = data['FH_Colitis']
            familyhistory.FH_Depression = data['FH_Depression']
            familyhistory.FH_Diabetes = data['FH_Diabetes']
            familyhistory.FH_ENT_Problems = data['FH_ENT_Problems']
            familyhistory.FH_Eating_Disorders = data['FH_Eating_Disorders']
            familyhistory.FH_Eczema = data['FH_Eczema']
            familyhistory.FH_Epilepsy = data['FH_Epilepsy']
            familyhistory.FH_Fertility = data['FH_Fertility']
            familyhistory.FH_Gallbladder = data['FH_Gallbladder']
            familyhistory.FH_Gynecology = data['FH_Gynecology']
            familyhistory.FH_Fever = data['FH_Fever']
            familyhistory.FH_Headaches = data['FH_Headaches']
            familyhistory.FH_Heart_Problems = data['FH_Heart_Problems']
            familyhistory.FH_Heart_Attack_Over_60 = data['FH_Heart_Attack_Over_60']
            familyhistory.FH_Heart_Attack_Under_60 = data['FH_Heart_Attack_Under_60']
            familyhistory.FH_Heart_Murmur = data['FH_Heart_Murmur']
            familyhistory.FH_Hepatitis = data['FH_Hepatitis']
            familyhistory.FH_High_Blood_Pressure = data['FH_High_Blood_Pressure']
            familyhistory.FH_High_Cholestorol = data['FH_High_Cholestorol']

        else:

            familyhistory = FamilyHistoryModel(FH_user_id, **data)

        familyhistory.save_to_db()

        return {"Status" : "Success",
                "Response" : familyhistory.json()
                }, 201


    @jwt_required
    def delete(self, FH_user_id, FH_Member):
        familyhistory = FamilyHistoryModel.find_by_id(FH_user_id)
        if familyhistory:
            familyhistory.delete_from_db()
            return {
            "Status" : "Success",
            'Response': 'Item deleted successfully.'}
        else:
            return {
            "Status" : "Error",
            'Response': 'Item not found'}, 404
