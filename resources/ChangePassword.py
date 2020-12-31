from flask_restful import Resource, reqparse
from model.user import UserModel
from flask import jsonify


class ChangePassword(Resource):

    parser = reqparse.RequestParser()
    u_id = parser.add_argument('u_id')
    u_Npassword = parser.add_argument('u_Npassword')


    def post(self):
        user = ChangePassword.parser.parse_args()
        u_id = user['u_id']
        u_Npassword = user['u_Npassword']
        user_details = UserModel.find_by_id(u_id)

        if user_details:
            user_details.u_password = user['u_Npassword']
            try:
                user_details.save_to_db()
            except:
                return {
                "Status" : "Error",
                "Response" : {
                "Message" : "Password not Updated",
                }
                }
        return {
        "Status" : "Success",
        "Response" :
        {
        "Message" : "Password Updated",
        }
        }
