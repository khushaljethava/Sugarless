from run import db
from flask_restful import Resource, reqparse
from model.Blood_Glucose import BloodGlucoseModel
from flask_jwt_extended import jwt_required
import pandas as pd
import datetime
from flask import jsonify
from sqlalchemy.sql import func

class BloodGlucose(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('BG_Value')
    parser.add_argument('BG_Date')
    parser.add_argument('BG_Time')





    @jwt_required
    def get(self,BG_user_id):
        if BloodGlucoseModel.find_by_id(BG_user_id):
            bloodglucose = BloodGlucoseModel.find_by_id(BG_user_id)
            BG_Date = datetime.date.today().strftime("%Y-%m-%d")
            bloodglucose_today = BloodGlucoseModel.find_by_today(BG_Date)
            bg_max =  int(pd.to_numeric(db.session.query(func.max(BloodGlucoseModel.BG_Value)).filter(BloodGlucoseModel.BG_user_id).first()))
            bg_min =  int(pd.to_numeric(db.session.query(func.min(BloodGlucoseModel.BG_Value)).filter(BloodGlucoseModel.BG_user_id).first()))
            bg_avg =  int(pd.to_numeric(db.session.query(func.avg(BloodGlucoseModel.BG_Value)).filter(BloodGlucoseModel.BG_user_id).first()))

            today_BG ={}
            for date in bloodglucose_today:
                today_BG[str(date.BG_Time)] = int(date.BG_Value)

            if bloodglucose:
                return {
                "Status" :"Success",
                "Today" : today_BG,
                "Min" : bg_min,
                "Max" : bg_max,
                "Avg" : bg_avg,


                }

        return{
        "Status":"Error",
        "Response" :  "Item not found"
        }, 404


    @jwt_required
    def post(self,BG_user_id):

        data = BloodGlucose.parser.parse_args()

#        data["BG_Date"] = datetime.date.today().strftime("%Y-%m-%d")
#        Time = datetime.datetime.now()
#        data["BG_Time"] = Time.strftime("%H:%M:%S")
        bloodglucose = BloodGlucoseModel(BG_user_id,**data)
        try:
            bloodglucose.save_to_db()
        except:

            return {
            "Status" : "Error",
            'Response': 'An error occurred while saving' }

        return{
        "Status" :"Success",
        "Response" : data
        },201
