from flask_restful import Resource, reqparse
from model.user import UserModel, RevokedTokenModel
from flask import jsonify


from flask_jwt_extended import (
        create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
        get_jwt_identity, get_raw_jwt
)

reg_parser = reqparse.RequestParser()
reg_parser.add_argument('u_username', help='Username cannot be blank', required=True)
reg_parser.add_argument('u_password', help='Password cannot be blank', required=True)
reg_parser.add_argument('u_fullname')
reg_parser.add_argument('u_email', help='Email cannot be blank', required=True)
reg_parser.add_argument('u_mobile', help='Mobile cannot be blank', required=True)
reg_parser.add_argument('u_gender')
reg_parser.add_argument('u_age')


log_parser = reqparse.RequestParser()
log_parser.add_argument('u_mobile', help='Mobile cannot be blank' , required=True)
log_parser.add_argument('u_password', help=' Password cannot be blank' , required=True)

class UserRegistration(Resource):

    def post(self):
        data = reg_parser.parse_args()
        if UserModel.find_by_username(data['u_username']):
            return {"Status" :"Error",
            'Response': {
            "Message" :'Username already exists'}}
        if UserModel.find_by_mobile(data['u_mobile']):
            return {
            "Status" :"Error",
            'Response': {
            "Message" :'Mobile Number already exists'}}
        if UserModel.find_by_email(data['u_email']):
            return {
            "Status" :"Error",
            'Response':{
             "Message" :'Mail id already exists'}}


        new_user = UserModel(
        u_username=data['u_username'],
        u_password=data['u_password'],
        u_fullname=data['u_fullname'],
        u_email=data['u_email'],
        u_mobile=data['u_mobile'],
        u_gender=data['u_gender'],
        u_age=data['u_age'])
        try:
            new_user.save_to_db()
            access_token = create_access_token(identity = data['u_mobile'])
            refresh_token = create_refresh_token(identity = data['u_mobile'])
            return {
            "Status" : "Success",
            'Response': {
            "Message" : "New User Created"
            }
            }
        except:
            return {
            "Status" : "Error",
            'Response':
            {
            "message" :'Something went wrong'}
            }, 500

class UserLogin(Resource):

    def post(self):
        data = log_parser.parse_args()
        current_user = UserModel.find_by_mobile(data['u_mobile'])
        if not current_user:
            return {
            "Status" : "Error",
            'Response':
            {
            "message" :"User not found"
            }
            }

        if UserModel.find_by_mobile(data['u_mobile']):
            if  (data['u_password'],current_user.u_password):
                user =  UserModel.find_by_mobile(data['u_mobile'])
                access_token = create_access_token(identity = data['u_mobile'])
                user_dict = dict(user.json())
                #refresh_token = create_refresh_token(identity = data['mobile'])
                result = {
                "message":"User Found",
                'u_id': user_dict["u_id"],
                'access_token': access_token,
                'u_username' : user_dict["u_username"],
                'u_gender' : user_dict["u_gender"],
                'u_age': user_dict["u_age"],
                }
                return {
                        "Status": "Success",
                        "Response" : result

                }
            else:
                return {'Status': 'Error ',
                "Response" : "Something went wrong"},500


class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {
            "Status" :"Success",
            'Response':'Access token has been revoked'}
        except:
            return {
            "Status" : "Error",
            'Response':'Something went wrong'}, 500


class UserLogoutRefersh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {
            "Status" :"Success",
            'Response': 'Refresh token has been revoked'}
        except:
            return {
            "Status" : "Error",
            'Response':'Something went wrong'}, 500


class TokenRefersh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {
        "Status" : "Success",
        'access_token': access_token}
