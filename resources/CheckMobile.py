from flask_restful import Resource, reqparse
from model.user import UserModel
from flask import jsonify
import requests
from model.OTP import OTPModel
import random




class CheckMobile(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('u_mobile', help='Mobile cannot be blank' , required=True)


    def post(self):
        user = CheckMobile.parser.parse_args()
        u_mobile = user['u_mobile']
        user_details = UserModel.find_by_mobile(u_mobile)
        if UserModel.find_by_mobile(u_mobile):
            user_dict = dict(user_details.json())
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

            result = {
                "message":"User Found",
                'u_id': user_dict["u_id"],
                'u_username' : user_dict["u_username"],
                'u_gender' : user_dict["u_gender"],
                'u_age': user_dict["u_age"],
            }

            return {
            "Status" : "Success",
            "Response" : result
            }

        return {
        "Status" : "Error",
        "Response" :{
        "Message" : "User Not Found",
        }
        }
