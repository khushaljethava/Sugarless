from flask_restful import Resource, reqparse
from model.user import UserModel
from flask import jsonify
import requests
from model.OTP import OTPModel
import random


class ForgotOTP(Resource):

    parser = reqparse.RequestParser()
    u_mobile = parser.add_argument('mobile')
    otp = parser.add_argument('otp')

    def post(self):

        user = ForgotOTP.parser.parse_args()
        u_mobile = user['mobile']
        otp = user['otp']
        current_user = OTPModel.find_by_mobile(u_mobile)
        main_user = UserModel.find_by_mobile(u_mobile)
        if current_user:
            main_user = dict(main_user.json())
            if (otp, current_user.otp):

                return{
                "Status" :"Success",
                "Response" : {
                "Message" :"User Verified",
                "u_id" :main_user['u_id']
                }
                }

        return {
        "Status" : "Error",
        "Response" : {
        "Message" :"Ve failed"
        }
        }
