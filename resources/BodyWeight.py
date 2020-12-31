from run import db
from flask_restful import Resource , reqparse
from model.BodyWeight import BodyWeightModel
from flask_jwt_extended import jwt_required
import pandas as pd
import datetime
from flask import jsonify
from sqlalchemy.sql import func



class BodyWeight(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('BW_Value')
    parser.add_argument('BW_Date')
    parser.add_argument('BW_Time')


    @jwt_required
    def get(self, BW_user_id):
        if BodyWeightModel.find_by_id(BW_user_id):
            bodyweight = BodyWeightModel.find_by_id(BW_user_id)
            BW_Date = datetime.date.today().strftime("%Y-%m-%d")
            bodyweight_today = BodyWeightModel.find_by_today(BW_Date)
            bw_max =  int(pd.to_numeric(db.session.query(func.max(BodyWeightModel.BW_Value)).filter(BodyWeightModel.BW_user_id).first()))
            bw_min =  int(pd.to_numeric(db.session.query(func.min(BodyWeightModel.BW_Value)).filter(BodyWeightModel.BW_user_id).first()))
            bw_avg =  int(pd.to_numeric(db.session.query(func.avg(BodyWeightModel.BW_Value)).filter(BodyWeightModel.BW_user_id).first()))

            today_BW = {}
            for date in bodyweight_today:
                today_BW[str(date.BW_Time)] = int(date.BW_Value)
            if bodyweight:
                return{
                "Status" :"Success",
                "Today" : today_BW,
                "Min" : bw_min,
                "Max" : bw_max,
                "Avg": bw_avg
                }

        return{
        "Status":"Error",
        "Response" :  "Item not found"
        }, 404




    @jwt_required
    def post(self,BW_user_id):
        data = BodyWeight.parser.parse_args()

        bodyweight = BodyWeightModel(BW_user_id,**data)
        try:
            bodyweight.save_to_db()
        except:
            return {
            "Status":"Error",
            "Response" : 'An error occurred while saving'
            }
        return{
        "Status":"Success",
        "Response" : data
        },201
