from run import db
from flask_restful import Resource, reqparse
from model.Medicine import MedicineModel
from flask_jwt_extended import jwt_required
import pandas as pd
import datetime
from flask import jsonify
from sqlalchemy.sql import func,and_


class MedicineStat(Resource):

    parser = reqparse.RequestParser()
    MD_user_id = parser.add_argument('u_id')


    @jwt_required
    def get(self):
        user_id = MedicineStat.parser.parse_args()
        MD_user_id = user_id['u_id']
        if MedicineModel.find_by_id(MD_user_id):
            medicine = MedicineModel.find_by_id(MD_user_id)
            MD_Date = datetime.date.today().strftime("%Y-%m-%d")
            mrng = None
            noon = None
            nite = None
            if db.session.query((MedicineModel.MD_Name)).filter(MedicineModel.MD_user_id,MedicineModel.MD_Date == MD_Date,MedicineModel.MD_Time <= '12:00:00' ).first():
                mrng = True
            if db.session.query((MedicineModel.MD_Name)).filter(MedicineModel.MD_user_id,MedicineModel.MD_Date == MD_Date, MedicineModel.MD_Time >= '12:00:00',MedicineModel.MD_Time <= '19:00:00' ).first():
                noon = True
            if db.session.query((MedicineModel.MD_Name)).filter(MedicineModel.MD_user_id,MedicineModel.MD_Date == MD_Date, MedicineModel.MD_Time >= '19:00:00',MedicineModel.MD_Time <= '24:00:00' ).first():
                nite = True


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
