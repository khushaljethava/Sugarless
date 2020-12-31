from run import db
from flask_restful import Resource, reqparse
from model.BodyWeight import BodyWeightModel
from flask_jwt_extended import jwt_required
import pandas as pd
import datetime
from flask import jsonify
from sqlalchemy.sql import func,and_

class bodyWeightStat(Resource):
    parser = reqparse.RequestParser()
    BW_user_id = parser.add_argument('u_id')

    def get(self):
        user_id = bodyWeightStat.parser.parse_args()
        BW_user_id = user_id['u_id']
        if BodyWeightModel.find_by_id(BW_user_id):
            bodyweight = BodyWeightModel.find_by_id(BW_user_id)
            BW_Date = datetime.date.today().strftime("%Y-%m-%d")
            bodyweight_today = BodyWeightModel.find_by_today(BW_Date)
            bw_max =  int(pd.to_numeric(db.session.query(func.max(BodyWeightModel.BW_Value)).filter(BodyWeightModel.BW_user_id).first()))
            bw_min =  int(pd.to_numeric(db.session.query(func.min(BodyWeightModel.BW_Value)).filter(BodyWeightModel.BW_user_id).first()))
            bw_avg =  int(pd.to_numeric(db.session.query(func.avg(BodyWeightModel.BW_Value)).filter(BodyWeightModel.BW_user_id).first()))


            if bodyweight:
                return{
                "Status" :"Success",
                "Response" : {
                "Min" : bw_min,
                "Max" : bw_max,
                "Avg": bw_avg
                }}

        return{
        "Status":"Error",
        "Response" :
        {
            "message" : "Item not found"
        }
        }, 404
