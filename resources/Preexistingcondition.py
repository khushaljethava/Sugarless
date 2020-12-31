from run import db
from flask_restful import Resource, reqparse
from model.Preexistingcondition import PreConditionModel
from flask_jwt_extended import jwt_required


class PreexistingCondition(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('PC_Race', help=' PC_Race cannot be blank', required=True)
    parser.add_argument('PC_Smoking', help='PC_Smoking cannot be blank', required=True)
    parser.add_argument('PC_Alcohol', help='PC_Alcohol cannot be blank', required=True)
    parser.add_argument('PC_Diabetes', help='PC_Diabetes cannot be blank', required=True)
    parser.add_argument('PC_Hear', help='PC_Hear cannot be blank', required=True)
    parser.add_argument('PC_Blood_Pressure', help='PC_Blood_Pressure cannot be blank', required=True)
    parser.add_argument('PC_Chest_Pain', help='PC_Chest_Pain cannot be blank', required=True)
    parser.add_argument('PC_Stroke', help='PC_Stroke cannot be blank', required=True)
    parser.add_argument('PC_Kidney', help='PC_Kidney cannot be blank', required=True)
    parser.add_argument('PC_Blood_Clot', help='PC_Blood_Clot cannot be blank', required=True)
    parser.add_argument('PC_Metal_implants', help='PC_Metal_implants cannot be blank', required=True)
    parser.add_argument('PC_Asthma', help='PC_Asthma cannot be blank', required=True)
    parser.add_argument('PC_Cancer', help='PC_Cancer cannot be blank', required=True)
    parser.add_argument('PC_Difficulty_Swallowing', help='PC_Difficulty_Swallowing cannot be blank', required=True)
    parser.add_argument('PC_Vascular_Problems', help='PC_Vascular_Problems cannot be blank', required=True)
    parser.add_argument('PC_Peripheral_Neuropathy', help='PC_Peripheral_Neuropathy cannot be blank', required=True)
    parser.add_argument('PC_Weightloss', help='PC_Weightloss cannot be blank', required=True)
    parser.add_argument('PC_Double_Vision', help='PC_Double_Vision cannot be blank', required=True)
    parser.add_argument('PC_Night_Sweats', help='PC_Night_Sweats cannot be blank', required=True)
    parser.add_argument('PC_Night_Pain', help='PC_Night_Pain cannot be blank', required=True)
    parser.add_argument('PC_Neurologic_Condition', help='PC_Neurologic_Condition cannot be blank', required=True)
    parser.add_argument('PC_Skin_Disease', help='PC_Skin_Disease cannot be blank', required=True)
    parser.add_argument('PC_Spinal_Cord_Injury', help='PC_Spinal_Cord_Injury cannot be blank', required=True)
    parser.add_argument('PC_Degenerative_Joint_Disease', help='PC_Degenerative_Joint_Disease cannot be blank', required=True)
    parser.add_argument('PC_Sexual_Dysfunction', help='PC_Sexual_Dysfunction cannot be blank', required=True)
    parser.add_argument('PC_Bladder', help='PC_Bladder cannot be blank', required=True)
    parser.add_argument('PC_Groin_Numbness', help='PC_Groin_Numbness cannot be blank', required=True)
    parser.add_argument('PC_Arthritis', help='PC_Arthritis cannot be blank', required=True)
    parser.add_argument('PC_Osteoporosis', help='PC_Osteoporosis cannot be blank', required=True)
    parser.add_argument('PC_Phsychological_Problems', help='PC_Phsychological_Problems cannot be blank', required=True)
    parser.add_argument('PC_Seizures', help='PC_Seizures cannot be blank', required=True)
    parser.add_argument('PC_Dizziness', help='PC_Dizziness cannot be blank', required=True)
    parser.add_argument('PC_Ringing_in_Ears', help='PC_Ringing_in_Ears cannot be blank', required=True)
    parser.add_argument('PC_Allergy_to_Latex', help='PC_Allergy_to_Latex cannot be blank', required=True)
    parser.add_argument('PC_Head_Injury', help='PC_Head_Injury cannot be blank', required=True)
    parser.add_argument('PC_Obesity', help='PC_Obesity cannot be blank', required=True)
    parser.add_argument('PC_Chronic_Pain', help='PC_Chronic_Pain cannot be blank', required=True)
    parser.add_argument('PC_Fractures', help='PC_Fractures cannot be blank', required=True)
    parser.add_argument('PC_Infection_Dissease', help='PC_Infection_Dissease cannot be blank', required=True)
    parser.add_argument('PC_Fever', help='PC_Fever cannot be blank', required=True)
    parser.add_argument('PC_Lower_Extremety', help='PC_Lower_Extremety cannot be blank', required=True)
    parser.add_argument('PC_Nausea', help='PC_Nausea cannot be blank', required=True)


    @jwt_required
    def get(self, PC_user_id):
        preexistingcondition = PreConditionModel.find_by_id(PC_user_id)
        if  preexistingcondition:
            return{
            "Status" : "Success",
            "Response" : preexistingcondition.json()
            }
        return {
        "Status" : "Error",
        'Response': 'Item not found'}, 404
    @jwt_required
    def post(self, PC_user_id):
        if PreConditionModel.find_by_id(PC_user_id):
            return {
            "Status" : "Error",
            'Response': 'Item already exists'}

        data = PreexistingCondition.parser.parse_args()
        preexistingcondition = PreConditionModel(PC_user_id, **data)

        try:

            preexistingcondition.save_to_db()

        except:

            return {
            "Status" : "Error",
            'Response': 'An error occurred while saving' }

        return {
        "Status" : "Success",
        "Response" : preexistingcondition.json()} ,201

    @jwt_required
    def delete(self,PC_user_id):
        preexistingcondition = PreConditionModel.find_by_id(PC_user_id)
        if preexistingcondition:
            preexistingcondition.delete_from_db()
            return {
            "Status" : "Success",
            'Response': 'Item deleted successfully.'}

        return {
        "Status" : "Error",
        'Response': ' Item not Found'}

    @jwt_required
    def put(self, PC_user_id):
        data = PreexistingCondition.parser.parse_args()

        preexistingcondition = PreConditionModel.find_by_id(PC_user_id)
        if preexistingcondition:
                preexistingcondition.PC_Race = data['PC_Race']
                preexistingcondition.PC_Smoking = data['PC_Smoking']
                preexistingcondition.PC_Alcohol = data['PC_Alcohol']
                preexistingcondition.PC_Diabetes = data['PC_Diabetes']
                preexistingcondition.PC_Hear = data['PC_Hear']
                preexistingcondition.PC_Blood_Pressure = data['PC_Blood_Pressure']
                preexistingcondition.PC_Chest_Pain = data['PC_Chest_Pain']
                preexistingcondition.PC_Stroke = data['PC_Stroke']
                preexistingcondition.PC_Kidney  = data['PC_Kidney']
                preexistingcondition.PC_Blood_Clot = data['PC_Blood_Clot']
                preexistingcondition.PC_Metal_implants = data['PC_Metal_implants']
                preexistingcondition.PC_Asthma = data['PC_Asthma']
                preexistingcondition.PC_Cancer = data['PC_Cancer']
                preexistingcondition.PC_Difficulty_Swallowing = data['PC_Difficulty_Swallowing']
                preexistingcondition.PC_Vascular_Problems = data['PC_Vascular_Problems']
                preexistingcondition.PC_Peripheral_Neuropathy = data['PC_Peripheral_Neuropathy']
                preexistingcondition.PC_Weightloss = data['PC_Weightloss']
                preexistingcondition.PC_Double_Vision = data['PC_Double_Vision']
                preexistingcondition.PC_Night_Sweats = data['PC_Night_Sweats']
                preexistingcondition.PC_Night_Pain = data['PC_Night_Pain']
                preexistingcondition.PC_Neurologic_Condition = data['PC_Neurologic_Condition']
                preexistingcondition.PC_Skin_Disease = data['PC_Skin_Disease']
                preexistingcondition.PC_Spinal_Cord_Injury = data['PC_Spinal_Cord_Injury']
                preexistingcondition.PC_Degenerative_Joint_Disease = data['PC_Degenerative_Joint_Disease']
                preexistingcondition.PC_Sexual_Dysfunction = data['PC_Sexual_Dysfunction']
                preexistingcondition.PC_Bladder = data['PC_Bladder']
                preexistingcondition.PC_Groin_Numbness = data['PC_Groin_Numbness']
                preexistingcondition.PC_Arthritis = data['PC_Arthritis']
                preexistingcondition.PC_Osteoporosis = data['PC_Osteoporosis']
                preexistingcondition.PC_Phsychological_Problems = data['PC_Phsychological_Problems']
                preexistingcondition.PC_Seizures = data['PC_Seizures']
                preexistingcondition.PC_Dizziness = data['PC_Dizziness']
                preexistingcondition.PC_Ringing_in_Ears = data['PC_Ringing_in_Ears']
                preexistingcondition.PC_Allergy_to_Latex   = data['PC_Allergy_to_Latex']
                preexistingcondition.PC_Head_Injury = data['PC_Head_Injury']
                preexistingcondition.PC_Obesity = data['PC_Obesity']
                preexistingcondition.PC_Chronic_Pain = data['PC_Chronic_Pain']
                preexistingcondition.PC_Fractures  = data['PC_Fractures']
                preexistingcondition.PC_Infection_Dissease  = data['PC_Infection_Dissease']
                preexistingcondition.PC_Fever = data['PC_Fever']
                preexistingcondition.PC_Lower_Extremety = data['PC_Lower_Extremety']
                preexistingcondition.PC_Nausea = data['PC_Nausea']

        else:
            preexistingcondition = PreConditionModel(PC_user_id, **data)
        preexistingcondition.save_to_db()

        return {
        "Status" :"Success",
        "Response" : preexistingcondition.json()
        },201
