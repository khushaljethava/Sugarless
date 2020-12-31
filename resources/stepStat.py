from run import db

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify
import datetime
import pandas as pd
from sqlalchemy import text
from flask_restful import Resource , reqparse,request
from model.Insulin import InsulinModel
from model.Steps import StepsModel


class stepStat(Resource):

    parser = reqparse.RequestParser()
    ST_user_id = parser.add_argument('u_id')

    @jwt_required
    def get(self):
        user_id = stepStat.parser.parse_args()
        ST_user_id = user_id['u_id']
        if StepsModel.find_by_id(ST_user_id):
            step = StepsModel.find_by_id(ST_user_id)
            ST_Date = datetime.date.today().strftime("%Y-%m-%d")
            step_today = StepsModel.find_by_today(ST_Date)
            total_steps = []
            total_calories = []
            total_time = []
            for date in step_today:
                 total_steps.append(int(date.ST_Value))

            for date in step_today:
                 total_calories.append(int(date.ST_Calories))

            for date in step_today:
                total_time.append(int(date.ST_TimeTaken))

            if step:
                return{
                "Status" :"Success",
                "Response" : {
                "Total Steps" : sum(total_steps),
                "Total Calories" : sum(total_calories),
                "Total Time" : sum(total_time)
                }}


        return{
        "Status":"Error",
        "Response" :  "Item not found"
        }, 404
