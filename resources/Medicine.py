from run import db
from flask_restful import Resource, reqparse
from model.Medicine import MedicineModel
from flask_jwt_extended import jwt_required
import pandas as pd
import datetime
from flask import jsonify
from sqlalchemy.sql import func


class Medicine(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('MD_Date')
    parser.add_argument('MD_Time')
    parser.add_argument('MD_Name')
    parser.add_argument('MD_Quantity')



    @jwt_required
    def get(self,MD_user_id):

        if MedicineModel.find_by_id(MD_user_id):
            medicine = MedicineModel.find_by_id(MD_user_id)
            MD_Date = datetime.date.today().strftime("%Y-%m-%d")
            mrng = None
            noon = None
            nite = None
            if db.session.query((MedicineModel.MD_Name)).filter(MedicineModel.MD_user_id,MedicineModel.MD_Date == MD_Date,MedicineModel.MD_Time <= '12:00:00' ).first():
                mrng = str(db.session.query((MedicineModel.MD_Name)).filter(MedicineModel.MD_user_id,MedicineModel.MD_Date == MD_Date, MedicineModel.MD_Time <= '12:00:00' ).first())
                mrng = [str(path) for path in mrng]
                mrng = mrng[0]
            if db.session.query((MedicineModel.MD_Name)).filter(MedicineModel.MD_user_id,MedicineModel.MD_Date == MD_Date, MedicineModel.MD_Time >= '12:00:00',MedicineModel.MD_Time <= '19:00:00' ).first():
                noon = db.session.query((MedicineModel.MD_Name)).filter(MedicineModel.MD_user_id,MedicineModel.MD_Date == MD_Date, MedicineModel.MD_Time >= '12:00:00',MedicineModel.MD_Time <= '19:00:00' ).first()
                noon = [str(path) for path in noon]
                noon = noon[0]
            if db.session.query((MedicineModel.MD_Name)).filter(MedicineModel.MD_user_id,MedicineModel.MD_Date == MD_Date, MedicineModel.MD_Time >= '19:00:00',MedicineModel.MD_Time <= '24:00:00' ).first():
                nite = str(db.session.query((MedicineModel.MD_Name)).filter(MedicineModel.MD_user_id,MedicineModel.MD_Date == MD_Date, MedicineModel.MD_Time >= '19:00:00',MedicineModel.MD_Time <= '24:00:00' ).first())
                nite = [str(path) for path in nite]
                nite = nite[0]


            if medicine:
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
    def post(self,MD_user_id):

        data = Medicine.parser.parse_args()

        medicine = MedicineModel(MD_user_id,**data)

        try:
            medicine.save_to_db()
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
