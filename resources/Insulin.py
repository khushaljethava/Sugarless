from run import db
from flask_restful import Resource, reqparse
from model.Insulin import InsulinModel
from flask_jwt_extended import jwt_required
import pandas as pd
import datetime
from flask import jsonify
from sqlalchemy.sql import func,and_

class Insulin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('IN_Value')
    parser.add_argument('IN_Date')
    parser.add_argument('IN_Time')


    @jwt_required
    def get(self,IN_user_id):
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


    @jwt_required
    def post(self,IN_user_id):

        data = Insulin.parser.parse_args()

        insulin = InsulinModel(IN_user_id, **data)

        try:
            insulin.save_to_db()
        except:
            return{
            "Status" :"Error",
            "Response" :{
            "message" :"An error occurred while saving"}
            }

        return{
        "Status":"Success",
        "Response" : data
        },201
