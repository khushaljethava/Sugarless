from run import db

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify
import datetime
import pandas as pd
from sqlalchemy import text
from flask_restful import Resource , reqparse,request
from model.Insulin import InsulinModel

class insulinStat(Resource):

    parser = reqparse.RequestParser()
    IN_user_id = parser.add_argument('u_id')

    @jwt_required
    def get(self):
        user_id = insulinStat.parser.parse_args()
        IN_user_id = user_id['u_id']
        if InsulinModel.find_by_id(IN_user_id):
            insulin = InsulinModel.find_by_id(IN_user_id)
            IN_Date = datetime.date.today().strftime("%Y-%m-%d")
            insulin_today = InsulinModel.find_by_today(IN_Date)
            mrng = None
            noon = None
            nite = None
            if db.session.query((InsulinModel.IN_Value)).filter(InsulinModel.IN_user_id,InsulinModel.IN_Date == IN_Date,InsulinModel.IN_Time <= '12:00:00' ).first():
                mrng = int(pd.to_numeric(db.session.query((InsulinModel.IN_Value)).filter(InsulinModel.IN_user_id,InsulinModel.IN_Date == IN_Date, InsulinModel.IN_Time <= '12:00:00' ).first()))
            if db.session.query((InsulinModel.IN_Value)).filter(InsulinModel.IN_user_id,InsulinModel.IN_Date == IN_Date, InsulinModel.IN_Time >= '12:00:00',InsulinModel.IN_Time <= '19:00:00' ).first():
                noon = int(pd.to_numeric(db.session.query((InsulinModel.IN_Value)).filter(InsulinModel.IN_user_id,InsulinModel.IN_Date == IN_Date, InsulinModel.IN_Time >= '12:00:00',InsulinModel.IN_Time <= '19:00:00' ).first()))
            if db.session.query((InsulinModel.IN_Value)).filter(InsulinModel.IN_user_id,InsulinModel.IN_Date == IN_Date, InsulinModel.IN_Time >= '19:00:00',InsulinModel.IN_Time <= '24:00:00' ).first():
                nite = int(pd.to_numeric(db.session.query((InsulinModel.IN_Value)).filter(InsulinModel.IN_user_id,InsulinModel.IN_Date == IN_Date, InsulinModel.IN_Time >= '19:00:00',InsulinModel.IN_Time <= '24:00:00' ).first()))

            #nite = int(pd.to_numeric(db.session.query((InsulinModel.IN_Value)).filter(InsulinModel.IN_user_id, InsulinModel.IN_Time <= '12:00:00' ).first()))


            if insulin:
                output = {}
                if mrng:
                    output.update({"Morning":mrng})
                if noon:
                    output.update({"Afternoon":noon})
                if nite:
                    output.update({"Night":nite})
                return{
                "Status" :"Success",
                "Response" : output
                }


        return{
        "Status":"Error",
        "Response" : {
        "Message" : "No Values found"}
        }, 404
