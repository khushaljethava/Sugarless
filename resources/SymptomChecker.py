from run import db
from flask_restful import Resource, reqparse
from model.SymptomChecker import SymptomCheckerModel
from model.SymptomCheckerAnswer import SymptomCheckerAnswerModel
from model.User_Symptoms_Input import UserSymptomsInputModel
from flask import jsonify
from flask_jwt_extended import jwt_required



class SymptomChecker(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('UI_SCA_qid')
    parser.add_argument('UI_SCA_aid')

    @jwt_required
    def get(self,UI_user_id):
        SCA_qid = UI_user_id
        if SymptomCheckerAnswerModel.find_by_answer_id(SCA_qid):
            options = SymptomCheckerAnswerModel.find_by_answer_id(SCA_qid)
            answers = {}
            for option in options:
                answers[(option.SCA_id)]=(option.SCA_Ans)


            return {
                "Status" : "Success",
                "Response": answers
            }
        else:
            return {
            "Status" : "Error",
            "Response" : "Question Not Found"
            }
    @jwt_required
    def post(self,UI_user_id):
        data = SymptomChecker.parser.parse_args()
        symptom_checker = UserSymptomsInputModel(UI_user_id,**data)

        try:
            symptom_checker.save_to_db()
            return {
            "Status" : "Success"
            }
        except:
            return {'Status': 'Error'}
