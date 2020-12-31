from run import db
from flask_restful import Resource, reqparse
from model.Blood_Glucose import BloodGlucoseModel
from flask_jwt_extended import jwt_required
import pandas as pd
import datetime
from flask import jsonify
from sqlalchemy.sql import func,and_



class BloodGlucoseStat(Resource):

    parser = reqparse.RequestParser()
    BG_user_id = parser.add_argument('u_id')


    @jwt_required
    def get(self):
        user_id = BloodGlucoseStat.parser.parse_args()
        BG_user_id = user_id['u_id']
        if BloodGlucoseModel.find_by_id(BG_user_id):
            bloodglucose = BloodGlucoseModel.find_by_id(BG_user_id)
            BG_Date = datetime.date.today().strftime("%Y-%m-%d")
            bloodglucose_today = BloodGlucoseModel.find_by_today(BG_Date)
            bg_max =  int(pd.to_numeric(db.session.query(func.max(BloodGlucoseModel.BG_Value)).filter(BloodGlucoseModel.BG_user_id).first()))
            bg_min =  int(pd.to_numeric(db.session.query(func.min(BloodGlucoseModel.BG_Value)).filter(BloodGlucoseModel.BG_user_id).first()))
            bg_avg =  int(pd.to_numeric(db.session.query(func.avg(BloodGlucoseModel.BG_Value)).filter(BloodGlucoseModel.BG_user_id).first()))

            if bloodglucose:
                return {
                "Status" :"Success",
                "Response" :{
                "Min" : bg_min,
                "Max" : bg_max,
                "Avg" : bg_avg,
                    }

                }

        return{
        "Status":"Error",
        "Response" :
        {
        "message" : "No Values found"
        }
        }, 404
