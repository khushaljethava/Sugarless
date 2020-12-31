from run import db
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from model.ReferenceRange import ReferenceRangeModel
from model.Labreport import LabReportModel
from model.user import UserModel
import pandas as pd

class ReferenceRange(Resource):

    def get(self,user_id):



        #if IRON >= db.session.query(ReferenceRangeModel.Range_Low).filter(ReferenceRangeModel.Lab_Test == 'Iron', ReferenceRangeModel.gender=='F').first() and IRON <= db.session.query(ReferenceRangeModel.Range_High).filter(ReferenceRangeModel.Lab_Test == 'Iron', ReferenceRangeModel.gender=='F').first():
        #    print('Working')
        labreport = LabReportModel.find_by_id(user_id)
        user =  UserModel.find_by_id(user_id)
        print(labreport.json())
        user_gender = (dict(user.json())['u_gender'])
        if user_gender == 'Male':
            user_gender = 'M'
        else:
            user_gender ='F'

        labreport = dict(labreport.json())


        LR_HPLC = labreport["LR_HPLC"]
        LR_AVERAGE_BLOOD_GLUCOSE = labreport["LR_AVERAGE_BLOOD_GLUCOSE"]
        LR_TOTAL_LEUCOCYTES_COUNT  = labreport["LR_TOTAL_LEUCOCYTES_COUNT"]
        LR_NEUTROPHILS = labreport["LR_NEUTROPHILS"]
        LR_LYMPHOCYTE_PERCENTAGE = labreport["LR_LYMPHOCYTE_PERCENTAGE"]
        LR_MONOCYTES = labreport["LR_MONOCYTES"]
        LR_EOSINOPHILS = labreport["LR_EOSINOPHILS"]
        LR_BASOPHILS = labreport["LR_BASOPHILS"]
        LR_IMMATURE_GRANULOCYTE_PERCENTAGE = labreport["LR_IMMATURE_GRANULOCYTE_PERCENTAGE"]
        LR_NEUTROPHILS_ABSOLUTE_COUNT = labreport["LR_NEUTROPHILS_ABSOLUTE_COUNT"]
        LR_LYMPHOCYTES_ABSOLUTE_COUNT = labreport["LR_LYMPHOCYTES_ABSOLUTE_COUNT"]
        LR_MONOCYTES_ABSOLUTE_COUNT = labreport["LR_MONOCYTES_ABSOLUTE_COUNT"]
        LR_BASOPHILS_ABSOLUTE_COUNT = labreport["LR_BASOPHILS_ABSOLUTE_COUNT"]
        LR_EOSINOPHILS_ABSOLUTE_COUNT = labreport["LR_EOSINOPHILS_ABSOLUTE_COUNT"]
        LR_IMMATURE_GRANULOCYTES = labreport["LR_IMMATURE_GRANULOCYTES"]
        LR_TOTAL_RBC = labreport["LR_TOTAL_RBC"]
        LR_NUCLEATED_RED_BLOOD_CELLS = labreport["LR_NUCLEATED_RED_BLOOD_CELLS"]
        LR_HEMOGLOBIN = labreport["LR_HEMOGLOBIN"]
        LR_HEMATOCRIT = labreport["LR_HEMATOCRIT"]
        LR_MEAN_CORPUSCULAR_VOLUME = labreport["LR_MEAN_CORPUSCULAR_VOLUME"]
        LR_MEAN_CORPUSCULAR_HEMOGLOBIN = labreport["LR_MEAN_CORPUSCULAR_HEMOGLOBIN"]
        LR_MEAN_CORP_HEMO_CONC = labreport["LR_MEAN_CORP_HEMO_CONC"]
        LR_RED_CELL_DISTRIBUTION_WIDTH_SD = labreport["LR_RED_CELL_DISTRIBUTION_WIDTH_SD"]
        LR_RED_CELL_DISTRIBUTION_WIDTH_CV = labreport["LR_RED_CELL_DISTRIBUTION_WIDTH_CV"]
        LR_PLATELET_DISTRIBUTION_WIDTH = labreport["LR_PLATELET_DISTRIBUTION_WIDTH"]
        LR_MEAN_PLATELET_VOLUME = labreport["LR_MEAN_PLATELET_VOLUME"]
        LR_PLATELET_COUNT = labreport["LR_PLATELET_COUNT"]
        LR_PLATELET_TO_LARGE_CELL_RATIO = labreport["LR_PLATELET_TO_LARGE_CELL_RATIO"]
        LR_PLATELETCRIT = labreport["LR_PLATELETCRIT"]
        LR_ARSENIC = labreport["LR_ARSENIC"]
        LR_CADMIUM = labreport["LR_CADMIUM"]
        LR_MERCURY = labreport["LR_MERCURY"]
        LR_LEAD = labreport["LR_LEAD"]
        LR_CHROMIUM = labreport["LR_CHROMIUM"]
        LR_BARIUM = labreport["LR_BARIUM"]
        LR_COBALT = labreport["LR_COBALT"]
        LR_CAESIUM = labreport["LR_CAESIUM"]
        LR_THALLIUM = labreport["LR_THALLIUM"]
        LR_URANIUM = labreport["LR_URANIUM"]
        LR_STRONTIUM = labreport["LR_STRONTIUM"]
        LR_ANTIMONY = labreport["LR_ANTIMONY"]
        LR_TIN = labreport["LR_TIN"]
        LR_MOLYBDENUM = labreport["LR_MOLYBDENUM"]
        LR_SILVER = labreport["LR_SILVER"]
        LR_VANADIUM = labreport["LR_VANADIUM"]
        LR_BERYLLIUM = labreport["LR_BERYLLIUM"]
        LR_BISMUTH = labreport["LR_BISMUTH"]
        LR_SELENIUM = labreport["LR_SELENIUM"]
        LR_ALUMINIUM = labreport["LR_ALUMINIUM"]
        LR_NICKEL = labreport["LR_NICKEL"]
        LR_MANGANESE = labreport["LR_MANGANESE"]
        LR_HOMOCYSTEINE  = labreport["LR_HOMOCYSTEINE"]
        LR_CYSTATIN_C = labreport["LR_CYSTATIN_C"]
        LR_LIPOPROTEIN = labreport["LR_LIPOPROTEIN"]
        LR_VITAMIN_B = labreport["LR_VITAMIN_B"]
        LR_APOLIPOPROTEIN_A_APOA = labreport["LR_APOLIPOPROTEIN_A_APOA"]
        LR_APOLIPOPROTEIN_B_APOB = labreport["LR_APOLIPOPROTEIN_B_APOB"]
        LR_APOB_APOA_RATIO = labreport["LR_APOB_APOA_RATIO"]
        LR_HSCRP = labreport["LR_HSCRP"]
        LR_SERUM_COPPER = labreport["LR_SERUM_COPPER"]
        LR_SERUM_ZINC = labreport["LR_SERUM_ZINC"]
        LR_TESTOSTERONE = labreport["LR_TESTOSTERONE"]
        LR_IRON = labreport["LR_IRON"]
        LR_TOTAL_IRON_BINDING_CAPACITY = labreport["LR_TOTAL_IRON_BINDING_CAPACITY"]
        LR_TRANSFERRIN_SATURATION = labreport["LR_TRANSFERRIN_SATURATION"]
        LR_ALKALINE_PHOSPHATASE = labreport["LR_ALKALINE_PHOSPHATASE"]
        LR_BILIRUBIN_TOTAL = labreport["LR_BILIRUBIN_TOTAL"]
        LR_BILIRUBIN_DIRECT = labreport["LR_BILIRUBIN_DIRECT"]
        LR_BILIRUBIN_INDIRECT = labreport["LR_BILIRUBIN_INDIRECT"]
        LR_GAMMA_GLUTAMYL_TRANSFERASE = labreport["LR_GAMMA_GLUTAMYL_TRANSFERASE"]
        LR_ASPARTATE_AMINOTRANSFERASE = labreport["LR_ASPARTATE_AMINOTRANSFERASE"]
        LR_ALANINE_TRANSAMINASE = labreport["LR_ALANINE_TRANSAMINASE"]
        LR_PROTEIN_TOTAL = labreport["LR_PROTEIN_TOTAL"]
        LR_ALBUMIN_SERUM = labreport["LR_ALBUMIN_SERUM"]
        LR_SERUM_ALB = labreport["LR_SERUM_ALB"]
        LR_SERUM_GLOBULIN = labreport["LR_SERUM_GLOBULIN"]
        LR_TOTAL_CHOLESTEROL = labreport["LR_TOTAL_CHOLESTEROL"]
        LR_HDL_CHOLESTEROL_DIRECT = labreport["LR_HDL_CHOLESTEROL_DIRECT"]
        LR_LDL_CHOLESTEROL_DIRECT = labreport["LR_LDL_CHOLESTEROL_DIRECT"]
        LR_TRIGLYCERIDES = labreport["LR_TRIGLYCERIDES"]
        LR_TC_HDL_CHOLESTEROL_RATIO = labreport["LR_TC_HDL_CHOLESTEROL_RATIO"]
        LR_LDL_HDL_RATIO = labreport["LR_LDL_HDL_RATIO"]
        LR_VLDL_CHOLESTEROL = labreport["LR_VLDL_CHOLESTEROL"]
        LR_NON_HDL_CHOLESTEROL = labreport["LR_NON_HDL_CHOLESTEROL"]
        LR_TOTAL_TRIIODOTHYRONINE = labreport["LR_TOTAL_TRIIODOTHYRONINE"]
        LR_TOTAL_THYROXINE = labreport["LR_TOTAL_THYROXINE"]
        LR_THYROID_STIMULATING_HORMONE = labreport["LR_THYROID_STIMULATING_HORMONE"]
        LR_BLOOD_UREA_NITROGEN = labreport["LR_BLOOD_UREA_NITROGEN"]
        LR_CREATININE_SERUM = labreport["LR_CREATININE_SERUM"]
        LR_BUN_SR_CREATININE_RATIO = labreport["LR_BUN_SR_CREATININE_RATIO"]
        LR_CALCIUM = labreport["LR_CALCIUM"]
        LR_URIC_ACID = labreport["LR_URIC_ACID"]
        LR_EST_GLOMERULAR_FILTRATION_RATE = labreport["LR_EST_GLOMERULAR_FILTRATION_RATE"]


    #    if labreport:
    #        return labreport.json()


    #
