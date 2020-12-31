from run import db
from flask import request
from werkzeug.utils import secure_filename
import os
import shutil
from flask_restful import Resource
from libs.IMGretina import ProcessRetina
from libs.ImgOCR import listToString
from flask_jwt_extended import jwt_required, get_jwt_identity
import tensorflow as tf
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
  try:
    for gpu in gpus:
      tf.config.experimental.set_memory_growth(gpu, True)
  except RuntimeError as e:
    print(e)
from model.RetinaUpload import RetinaUploadModel
import tensorflow as tf


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
Temp_FOLDER = 'static/Temp'
Infected = 'static/RetinaUpload/Infected'
Uninfected = 'static/RetinaUpload/Uninfected'


class RetinaUpload(Resource):


    @jwt_required
    def post(self,RU_user_id):
        def allowed_file(filename):
            return '.' in filename and \
                filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS



        RU_userid = get_jwt_identity()
        folder = f"user_{RU_userid}"

        file = request.files['inputFile']

        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)

            if os.path.isdir(Temp_FOLDER+'/'+folder):
                file.save(os.path.join(Temp_FOLDER,folder,filename))
            else:
                os.makedirs(Temp_FOLDER+'/'+folder)
                file.save(os.path.join(Temp_FOLDER,folder,filename))

            fpath = os.path.join(Temp_FOLDER,folder,filename)
            result = ProcessRetina(fpath)
            if result['RU_prediction'] == "Infected":
                file.save(os.path.join(Infected,filename) )
            else:
                file.save(os.path.join(Uninfected,filename))
            path = os.path.join(Temp_FOLDER,folder)
            shutil.rmtree(path)

            retinaupload = RetinaUploadModel(RU_user_id,RU_name=file.filename,**result,RU_report=file.read())
            try:

                retinaupload.save_to_db()
            except:
                return {
                "Status" : "Error",
                'Response': ' Error occurred while saving'},500

        else:
            return {
            "Status" : "Error",
            'Response':'File extension not allowed'},500

        return {
        "Status" : "Success",
        "Response" :   result},201


    def get(self,RU_user_id):
        retinaupload = RetinaUploadModel.find_by_id(RU_user_id)
        if retinaupload:
            return {
            "Status" : "Success",
            "Response" : retinaupload.json()
            }
        return {
        "Status" : "Error",
        'Response' :'Item not found'}, 404

    def delete(self,RU_user_id):
        ratinaupload = RetinaUploadModel.find_by_id(RU_user_id)
        if ratinaupload:
            ratinaupload.delete_from_db()
            return {
            "Status" : "Success",
            'Response': 'Item deleted successfully.'}
        return {
        "Status" : "Error",
        'Response': 'Item not found'}
