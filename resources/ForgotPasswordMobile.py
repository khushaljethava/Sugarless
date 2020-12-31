from flask_restful import Resource, reqparse
from model.user import UserModel
from flask import jsonify
import requests
from model.OTP import OTPModel
import random


class ForgotPasswordMobile(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('mobile', help='Mobile cannot be blank' , required=True)

    def post(self):
        data = ForgotPasswordMobile.parser.parse_args()
        u_mobile = data['mobile']
        user =  UserModel.find_by_mobile(u_mobile)
        if UserModel.find_by_mobile(u_mobile):
            user = dict(user.json())
            url = "https://www.fast2sms.com/dev/bulk"

            otp = random.SystemRandom().randint(100000,999999)
            querystring = {"authorization":"PXX0LAHOO7bYpM0tZdGYPaoLWHSXcPdLbOIIeTVezz7X9JaQmX4uIz6BpVtc","sender_id":"FSTSMS","language":"english","route":"qt","numbers":"9662737937","message":"41820","variables":"{AA}|{CC}","variables_values":"5464|asdaswdx"}
            querystring["numbers"] = u_mobile
            querystring["variables_values"] = str(otp)+"|asdaswdx"
            headers = {
                'cache-control': "no-cache"
                }

            response = requests.request("GET", url, headers=headers, params=querystring)

            result = {"u_mobile": u_mobile,"otp" : otp}
            store_otp = OTPModel(**result)
            store_otp.save_to_db()
            return {
            "Status" :"Success",
            "Response" :{
            "Message" : "User Found",
            "u_id" : user['u_id'],
            }
            }

        return {
        "Status" : "Error",
        "Response" : {
        "Message" : "User Not Found",
        }
        }
