from run import db

from flask_jwt_extended import jwt_required
from flask import jsonify
import datetime
from sqlalchemy import text
from flask_restful import Resource , reqparse
from model.Blood_Glucose import BloodGlucoseModel
from model.BodyWeight import BodyWeightModel
from model.Insulin import InsulinModel
from model.Steps import StepsModel

class HomeBanner(Resource):

    @jwt_required
    def get(self, user_id,today_date):
        '''
        BG_user_id= user_id
        IN_user_id= user_id
        BW_user_id= user_id
        ST_user_id= user_id
        bloodglucose = BloodGlucoseModel.find_by_id(BG_user_id)
        insulin = InsulinModel.find_by_id(IN_user_id)
        bodyweight = BodyWeightModel.find_by_id(BW_user_id)
        step = StepsModel.find_by_id(ST_user_id)

        BG_Date = datetime.date.today().strftime("%Y-%m-%d")
        insulin_today = InsulinModel.find_by_today(BG_Date)
        bloodglucose_today = BloodGlucoseModel.find_by_today(BG_Date)
        bodyweight_today = BodyWeightModel.find_by_today(BG_Date)
        step_today = StepsModel.find_by_today(BG_Date)

        result = []
        today_BG ={}
        for date in bloodglucose_today:
            bg_dict = {"title":"Blood Glucose"}

            bg_value = today_BG[str(date.BG_Time)] = int(date.BG_Value)
            bg_time = today_BG[str(date.BG_Time)] = int(date.BG_Time)
            bg_dict["value"] = bg_value


        today_IN = {}
        for date in insulin_today:
            in_dict = {"title": "Insulin"}
            IN_value = today_IN[str(date.IN_Time)] = int(date.IN_Value)
            in_dict["value"] = IN_value

        today_BW = {}
        for date in bodyweight_today:
            bw_dict = {"title": "Body Weight"}
            bw_value = today_BW[str(date.BW_Time)] = int(date.BW_Value)
            bw_dict["value"] = bw_value

        today_ST = {}
        for date in step_today:
            st_dict = {"title": "Steps"}

            st_value = today_ST[str(date.ST_Time)] = int(date.ST_Value)
            st_dict["value"] = st_value


        if bloodglucose:
            return {
            "Status" :"Success",
            "Response" : bg_dict,
            "result" : result

            }'''
        #today_date = '2020-12-21'
        query = ("SELECT BloodGlucose.BG_id as id, BloodGlucose.BG_Value as value,BloodGlucose.BG_Time as time ,'Blood Glucose' as title FROM `BloodGlucose` WHERE BloodGlucose.BG_Date = '{raw_date}' AND BloodGlucose.BG_user_id = {raw_user}  UNION SELECT Insulin.IN_id as id, Insulin.IN_Value as value,Insulin.IN_Time as time,'Insulin' as title FROM `Insulin` WHERE Insulin.IN_Date='{raw_date}' AND Insulin.IN_user_id = {raw_user} UNION SELECT BodyWeight.BW_id as id, BodyWeight.BW_Value as value,BodyWeight.BW_Time as time,'Body Weight' as title FROM `BodyWeight` WHERE BodyWeight.BW_Date='{raw_date}' AND BodyWeight.BW_user_id = {raw_user} UNION SELECT Steps.ST_id as id, Steps.ST_Value as value,Steps.ST_Time as time,'Steps' as title FROM `Steps` WHERE Steps.ST_Date='{raw_date}' AND Steps.ST_user_id = {raw_user} ORDER BY time DESC").format(raw_user=user_id,raw_date = today_date)
        main = {}
        output = []
        #query = ("SELECT BloodGlucose.BG_id as id, BloodGlucose.BG_Value as value,BloodGlucose.BG_Time as time,'Blood Glucose' as title FROM `BloodGlucose` WHERE BloodGlucose.BG_Date = '2020-12-21' AND BloodGlucose.BG_user_id = {} UNION SELECT Insulin.IN_id as id, Insulin.IN_Value as value,Insulin.IN_Time as time,'Insulin' as title FROM `Insulin` WHERE Insulin.IN_Date='2020-12-21' AND Insulin.IN_user_id = {}  ORDER BY time DESC").format(user_id,user_id)
        result = db.engine.execute(query)

        for rem in result:
            #print(rem)

            main["title"] = rem[3]
            main["value"] = rem[1]
            main["time"] = str(rem[2])
            output.append(main.copy())

        return {
        "Status" : "Success",
        "Response" : output
        }

        return{
        "Status":"Error",
        "Response" :  "Item not found"
        }, 404
