from run import db
import requests
from flask_restful import Resource, reqparse
from model.OTP import OTPModel
import random
class SendOTP(Resource):

    def get(self):
        url = "https://www.fast2sms.com/dev/bulk"

        otp = random.SystemRandom().randint(100000,999999)
        u_mobile = 9662737937
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
        "Message" : response.text,
        "Result" : result
        }
