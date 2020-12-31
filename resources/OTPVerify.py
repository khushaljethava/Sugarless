from run import db
from flask_restful import Resource , reqparse
from model.OTP import OTPModel
from flask_jwt_extended import (
        create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
        get_jwt_identity, get_raw_jwt
)


class OTPVerify(Resource):

    parser = reqparse.RequestParser()
    u_mobile = parser.add_argument('u_mobile')
    otp = parser.add_argument('otp')


    def post(self):
        user = OTPVerify.parser.parse_args()
        u_mobile = user['u_mobile']
        otp = user['otp']
        current_user = OTPModel.find_by_mobile(u_mobile)
        if current_user:
            if (otp , current_user.otp):
                access_token = create_access_token(identity = u_mobile)
                current_user.delete_from_db()
                return {
                "Status" : "Success",
                "Response" :{
                "message" :"user verfied",
                "access_token" : access_token
                }
                }
        return {
        "Status" : "Error",
        "Response" :{
        "Message" : "Verification failed",
        }
        }
