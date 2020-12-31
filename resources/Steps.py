from run import db
from flask_restful import Resource, reqparse
from model.Steps import StepsModel
from flask_jwt_extended import jwt_required
import pandas as pd
import datetime
from flask import jsonify
from sqlalchemy.sql import func,and_



class Steps(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('ST_Value')
    parser.add_argument('ST_Date')
    parser.add_argument('ST_Time')
    parser.add_argument('ST_TimeTaken')
    parser.add_argument('ST_Calories')


    @jwt_required
    def get(self,ST_user_id):
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
                "Total Steps" : sum(total_steps),
                "Total Calories" : sum(total_calories),
                "Total Time" : sum(total_time)
                }


        return{
        "Status":"Error",
        "Response" :  "Item not found"
        }, 404


    @jwt_required
    def post(self,ST_user_id):

        data = Steps.parser.parse_args()
        ST_Date = datetime.date.today().strftime("%Y-%m-%d")

        step_today = int(data["ST_Value"])
        Calories = (step_today*.04)
        data["ST_Calories"] = Calories

        step = StepsModel(ST_user_id,**data)
        try:
            step.save_to_db()
        except:
            return{
            "Status" : "Error",
            "Response":"An error occurred while saving"
            }
        return{
        "Status" : "Success",
        "Response": data
        },201
