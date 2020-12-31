from run import db
from flask_restful import Resource, reqparse
from model.Labreport import LabReportModel
from flask_jwt_extended import jwt_required
import pandas as pd
import json

class LabReport(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('LR_HPLC', help=' HPLC cannot be blank')
    parser.add_argument('LR_AVERAGE_BLOOD_GLUCOSE', help=' AVERAGE_BLOOD_GLUCOSE cannot be blank')
    parser.add_argument('LR_TOTAL_LEUCOCYTES_COUNT', help=' TOTAL_LEUCOCYTES_COUNT cannot be blank')
    parser.add_argument('LR_NEUTROPHILS', help=' NEUTROPHILS cannot be blank')
    parser.add_argument('LR_LYMPHOCYTE_PERCENTAGE', help=' LYMPHOCYTE_PERCENTAGE cannot be blank')
    parser.add_argument('LR_MONOCYTES', help=' MONOCYTES cannot be blank')
    parser.add_argument('LR_EOSINOPHILS', help=' EOSINOPHILS cannot be blank')
    parser.add_argument('LR_BASOPHILS', help=' BASOPHILS cannot be blank')
    parser.add_argument('LR_IMMATURE_GRANULOCYTE_PERCENTAGE', help=' IMMATURE_GRANULOCYTE_PERCENTAGE cannot be blank')
    parser.add_argument('LR_NEUTROPHILS_ABSOLUTE_COUNT', help=' NEUTROPHILS_ABSOLUTE_COUNT cannot be blank')
    parser.add_argument('LR_LYMPHOCYTES_ABSOLUTE_COUNT', help=' LYMPHOCYTES_ABSOLUTE_COUNT cannot be blank')
    parser.add_argument('LR_MONOCYTES_ABSOLUTE_COUNT', help=' MONOCYTES_ABSOLUTE_COUNT cannot be blank')
    parser.add_argument('LR_BASOPHILS_ABSOLUTE_COUNT', help=' BASOPHILS_ABSOLUTE_COUNT cannot be blank')
    parser.add_argument('LR_EOSINOPHILS_ABSOLUTE_COUNT', help=' EOSINOPHILS_ABSOLUTE_COUNT cannot be blank')
    parser.add_argument('LR_IMMATURE_GRANULOCYTES', help=' IMMATURE_GRANULOCYTES cannot be blank')
    parser.add_argument('LR_TOTAL_RBC', help=' TOTAL_RBC cannot be blank')
    parser.add_argument('LR_NUCLEATED_RED_BLOOD_CELLS', help=' NUCLEATED_RED_BLOOD_CELLS cannot be blank')
    parser.add_argument('LR_HEMOGLOBIN', help=' HEMOGLOBIN cannot be blank')
    parser.add_argument('LR_HEMATOCRIT', help=' HEMATOCRIT cannot be blank')
    parser.add_argument('LR_MEAN_CORPUSCULAR_VOLUME', help=' MEAN_CORPUSCULAR_VOLUME cannot be blank')
    parser.add_argument('LR_MEAN_CORPUSCULAR_HEMOGLOBIN', help=' MEAN_CORPUSCULAR_HEMOGLOBIN cannot be blank')
    parser.add_argument('LR_MEAN_CORP_HEMO_CONC', help=' MEAN_CORP_HEMO_CONC cannot be blank')
    parser.add_argument('LR_RED_CELL_DISTRIBUTION_WIDTH_SD', help=' RED_CELL_DISTRIBUTION_WIDTH_SD cannot be blank')
    parser.add_argument('LR_RED_CELL_DISTRIBUTION_WIDTH_CV', help=' RED_CELL_DISTRIBUTION_WIDTH_CV cannot be blank')
    parser.add_argument('LR_PLATELET_DISTRIBUTION_WIDTH', help=' PLATELET_DISTRIBUTION_WIDTH cannot be blank')
    parser.add_argument('LR_MEAN_PLATELET_VOLUME', help=' MEAN_PLATELET_VOLUME cannot be blank')
    parser.add_argument('LR_PLATELET_COUNT', help=' PLATELET_COUNT cannot be blank')
    parser.add_argument('LR_PLATELET_TO_LARGE_CELL_RATIO', help=' PLATELET_TO_LARGE_CELL_RATIO cannot be blank')
    parser.add_argument('LR_PLATELETCRIT', help=' PLATELETCRIT cannot be blank')
    parser.add_argument('LR_ARSENIC', help=' ARSENIC cannot be blank')
    parser.add_argument('LR_CADMIUM', help=' CADMIUM cannot be blank')
    parser.add_argument('LR_MERCURY', help='MERCURY cannot be blank')
    parser.add_argument('LR_LEAD', help='LEAD cannot be blank')
    parser.add_argument('LR_CHROMIUM', help='CHROMIUM cannot be blank')
    parser.add_argument('LR_BARIUM', help=' BARIUM cannot be blank')
    parser.add_argument('LR_COBALT', help=' COBALT cannot be blank')
    parser.add_argument('LR_CAESIUM', help=' CAESIUM cannot be blank')
    parser.add_argument('LR_THALLIUM', help=' THALLIUM cannot be blank')
    parser.add_argument('LR_URANIUM', help=' URANIUM cannot be blank')
    parser.add_argument('LR_STRONTIUM', help=' STRONTIUM cannot be blank')
    parser.add_argument('LR_ANTIMONY', help=' ANTIMONY cannot be blank')
    parser.add_argument('LR_TIN', help=' TIN cannot be blank')
    parser.add_argument('LR_MOLYBDENUM', help=' MOLYBDENUM cannot be blank')
    parser.add_argument('LR_SILVER', help=' SILVER cannot be blank')
    parser.add_argument('LR_VANADIUM', help=' VANADIUM cannot be blank')
    parser.add_argument('LR_BERYLLIUM', help=' BERYLLIUM cannot be blank')
    parser.add_argument('LR_BISMUTH', help=' BISMUTH cannot be blank')
    parser.add_argument('LR_SELENIUM', help=' SELENIUM cannot be blank')
    parser.add_argument('LR_ALUMINIUM', help=' ALUMINIUM cannot be blank')
    parser.add_argument('LR_NICKEL', help=' NICKEL cannot be blank')
    parser.add_argument('LR_MANGANESE', help=' MANGANESE cannot be blank')
    parser.add_argument('LR_HOMOCYSTEINE', help=' HOMOCYSTEINE cannot be blank')
    parser.add_argument('LR_CYSTATIN_C', help=' CYSTATIN_C cannot be blank')
    parser.add_argument('LR_LIPOPROTEIN', help=' LIPOPROTEIN cannot be blank')
    parser.add_argument('LR_VITAMIN_B', help=' VITAMIN B cannot be blank')
    parser.add_argument('LR_APOLIPOPROTEIN_A_APOA', help=' APOLIPOPROTEIN_A_APOA cannot be blank')
    parser.add_argument('LR_APOLIPOPROTEIN_B_APOB', help=' APOLIPOPROTEIN_B_APOB cannot be blank')
    parser.add_argument('LR_APOB_APOA_RATIO', help=' APOB_APOA_RATIO cannot be blank')
    parser.add_argument('LR_HSCRP', help=' HSCRP cannot be blank')
    parser.add_argument('LR_SERUM_COPPER', help=' SERUM_COPPER cannot be blank')
    parser.add_argument('LR_SERUM_ZINC', help=' SERUM_ZINC cannot be blank')
    parser.add_argument('LR_TESTOSTERONE', help=' TESTOSTERONE cannot be blank')
    parser.add_argument('LR_IRON', help=' IRON cannot be blank')
    parser.add_argument('LR_TOTAL_IRON_BINDING_CAPACITY', help=' TOTAL_IRON_BINDING_CAPACITY cannot be blank')
    parser.add_argument('LR_TRANSFERRIN_SATURATION', help=' TRANSFERRIN_SATURATION cannot be blank')
    parser.add_argument('LR_ALKALINE_PHOSPHATASE', help=' ALKALINE_PHOSPHATASE cannot be blank')
    parser.add_argument('LR_BILIRUBIN_TOTAL', help=' BILIRUBIN_TOTAL cannot be blank')
    parser.add_argument('LR_BILIRUBIN_DIRECT', help=' BILIRUBIN_DIRECT cannot be blank')
    parser.add_argument('LR_BILIRUBIN_INDIRECT', help=' BILIRUBIN_INDIRECT cannot be blank')
    parser.add_argument('LR_GAMMA_GLUTAMYL_TRANSFERASE', help=' GAMMA_GLUTAMYL_TRANSFERASE cannot be blank')
    parser.add_argument('LR_ASPARTATE_AMINOTRANSFERASE', help=' ASPARTATE_AMINOTRANSFERASE cannot be blank')
    parser.add_argument('LR_ALANINE_TRANSAMINASE', help=' ALANINE_TRANSAMINASE cannot be blank')
    parser.add_argument('LR_PROTEIN_TOTAL', help=' PlabreportEOSINOPHILSROTEIN_TOTAL cannot be blank')
    parser.add_argument('LR_ALBUMIN_SERUM', help=' ALBUMIN_SERUM cannot be blank')
    parser.add_argument('LR_SERUM_ALB', help=' SERUM_ALB cannot be blank')
    parser.add_argument('LR_SERUM_GLOBULIN', help=' SERUM_GLOBULIN cannot be blank')
    parser.add_argument('LR_TOTAL_CHOLESTEROL', help=' TOTAL_CHOLESTEROL cannot be blank')
    parser.add_argument('LR_HDL_CHOLESTEROL_DIRECT', help=' Huser_idDL_CHOLESTEROL_DIRECT cannot be blank')
    parser.add_argument('LR_LDL_CHOLESTEROL_DIRECT', help=' LDL_CHOLESTEROL_DIRECT cannot be blank')
    parser.add_argument('LR_TRIGLYCERIDES', help=' TRIGLYCERIDES cannot be blank')
    parser.add_argument('LR_TC_HDL_CHOLESTEROL_RATIO', help=' TC_HDL_CHOLESTEROL_RATIO cannot be blank')
    parser.add_argument('LR_LDL_HDL_RATIO', help=' LDL_HDL_RATIO cannot be blank')
    parser.add_argument('LR_VLDL_CHOLESTEROL', help=' VLDL_CHOLESTEROL cannot be blank')
    parser.add_argument('LR_NON_HDL_CHOLESTEROL', help=' NON_HDL_CHOLESTEROL cannot be blank')
    parser.add_argument('LR_TOTAL_TRIIODOTHYRONINE', help=' TOTAL_TRIIODOTHYRONINE cannot be blank')
    parser.add_argument('LR_TOTAL_THYROXINE', help=' TOTAL_THYROXINE cannot be blank')
    parser.add_argument('LR_THYROID_STIMULATING_HORMONE', help=' THYROID_STIMULATING_HORMONE cannot be blank')
    parser.add_argument('LR_BLOOD_UREA_NITROGEN', help=' BLOOD_UREA_NITROGEN cannot be blank')
    parser.add_argument('LR_CREATININE_SERUM', help=' CREATININE_SERUM cannot be blank')
    parser.add_argument('LR_BUN_SR_CREATININE_RATIO', help=' BUN_SR_CREATININE_RATIO cannot be blank')
    parser.add_argument('LR_CALCIUM', help=' CALCIUM cannot be blank')
    parser.add_argument('LR_URIC_ACID', help=' URIC_ACID cannot be blank')
    parser.add_argument('LR_EST_GLOMERULAR_FILTRATION_RATE', help=' EST_GLOMERULAR_FILTRATION_RATE cannot be blank')



    @jwt_required
    def get(self,LR_user_id):
        #lowrange = LabReportModel.Compare_IRON()
        #print(lowrange)
        labreport = LabReportModel.find_by_id(LR_user_id)
        if labreport:
            return {
            "Status" :"Success",
            "Response" : labreport.json()
            }

        else:
            return {
            "Status" : "Error",
            'Response': 'Item not found' }, 404
        #return lowrange



    @jwt_required
    def put (self,LR_user_id):
        data =  LabReport.parser.parse_args()
        labreport = LabReportModel.find_by_id(LR_user_id)
        if labreport:
            labreport.LR_HPLC = data['LR_HPLC']
            labreport.LR_AVERAGE_BLOOD_GLUCOSE = data['LR_AVERAGE_BLOOD_GLUCOSE']
            labreport.LR_TOTAL_LEUCOCYTES_COUNT  = data['LR_TOTAL_LEUCOCYTES_COUNT']
            labreport.LR_NEUTROPHILS = data['LR_NEUTROPHILS']
            labreport.LR_LYMPHOCYTE_PERCENTAGE = data['LR_LYMPHOCYTE_PERCENTAGE']
            labreport.LR_MONOCYTES = data['LR_MONOCYTES']
            labreport.LR_EOSINOPHILS = data['LR_EOSINOPHILS']
            labreport.LR_BASOPHILS = data['LR_BASOPHILS']
            labreport.LR_IMMATURE_GRANULOCYTE_PERCENTAGE = data['LR_IMMATURE_GRANULOCYTE_PERCENTAGE']
            labreport.LR_NEUTROPHILS_ABSOLUTE_COUNT = data['LR_NEUTROPHILS_ABSOLUTE_COUNT']
            labreport.LR_LYMPHOCYTES_ABSOLUTE_COUNT = data['LR_LYMPHOCYTES_ABSOLUTE_COUNT']
            labreport.LR_MONOCYTES_ABSOLUTE_COUNT = data['LR_MONOCYTES_ABSOLUTE_COUNT']
            labreport.LR_BASOPHILS_ABSOLUTE_COUNT = data['LR_BASOPHILS_ABSOLUTE_COUNT']
            labreport.LR_EOSINOPHILS_ABSOLUTE_COUNT = data['LR_EOSINOPHILS_ABSOLUTE_COUNT']
            labreport.LR_IMMATURE_GRANULOCYTES = data['LR_IMMATURE_GRANULOCYTES']
            labreport.LR_TOTAL_RBC = data['LR_TOTAL_RBC']
            labreport.LR_NUCLEATED_RED_BLOOD_CELLS = data['LR_NUCLEATED_RED_BLOOD_CELLS']
            labreport.LR_HEMOGLOBIN = data['LR_HEMOGLOBIN']
            labreport.LR_HEMATOCRIT = data['LR_HEMATOCRIT']
            labreport.LR_MEAN_CORPUSCULAR_VOLUME = data['LR_MEAN_CORPUSCULAR_VOLUME']
            labreport.LR_MEAN_CORPUSCULAR_HEMOGLOBIN = data['LR_MEAN_CORPUSCULAR_HEMOGLOBIN']
            labreport.LR_MEAN_CORP_HEMO_CONC = data['LR_MEAN_CORP_HEMO_CONC']
            labreport.LR_RED_CELL_DISTRIBUTION_WIDTH_SD = data['LR_RED_CELL_DISTRIBUTION_WIDTH_SD']
            labreport.LR_RED_CELL_DISTRIBUTION_WIDTH_CV = data['LR_RED_CELL_DISTRIBUTION_WIDTH_CV']
            labreport.LR_PLATELET_DISTRIBUTION_WIDTH = data['LR_PLATELET_DISTRIBUTION_WIDTH']
            labreport.LR_MEAN_PLATELET_VOLUME = data['LR_MEAN_PLATELET_VOLUME']
            labreport.LR_PLATELET_COUNT = data['LR_PLATELET_COUNT']
            labreport.LR_PLATELET_TO_LARGE_CELL_RATIO = data['LR_PLATELET_TO_LARGE_CELL_RATIO']
            labreport.LR_PLATELETCRIT = data['LR_PLATELETCRIT']
            labreport.LR_ARSENIC = data['LR_ARSENIC']
            labreport.LR_CADMIUM = data['LR_CADMIUM']
            labreport.LR_MERCURY = data['LR_MERCURY']
            labreport.LR_LEAD = data['LR_LEAD']
            labreport.LR_CHROMIUM = data['LR_CHROMIUM']
            labreport.LR_BARIUM = data['LR_BARIUM']
            labreport.LR_COBALT = data['LR_COBALT']
            labreport.LR_CAESIUM = data['LR_CAESIUM']
            labreport.LR_THALLIUM = data['LR_THALLIUM']
            labreport.LR_URANIUM = data['LR_URANIUM']
            labreport.LR_STRONTIUM = data['LR_STRONTIUM']
            labreport.LR_ANTIMONY = data['LR_ANTIMONY']
            labreport.LR_TIN = data['LR_TIN']
            labreport.LR_MOLYBDENUM = data['LR_MOLYBDENUM']
            labreport.LR_SILVER = data['LR_SILVER']
            labreport.LR_VANADIUM = data['LR_VANADIUM']
            labreport.LR_BERYLLIUM = data['LR_BERYLLIUM']
            labreport.LR_BISMUTH = data['LR_BISMUTH']
            labreport.LR_SELENIUM = data['LR_SELENIUM']
            labreport.LR_ALUMINIUM = data['LR_ALUMINIUM']
            labreport.LR_NICKEL = data['LR_NICKEL']
            labreport.LR_MANGANESE = data['LR_MANGANESE']
            labreport.LR_HOMOCYSTEINE = data['LR_HOMOCYSTEINE']
            labreport.LR_CYSTATIN_C = data['LR_CYSTATIN_C']
            labreport.LR_LIPOPROTEIN = data['LR_LIPOPROTEIN']
            labreport.LR_VITAMIN_B = data['LR_VITAMIN_B']
            labreport.LR_APOLIPOPROTEIN_A_APOA = data['LR_APOLIPOPROTEIN_A_APOA']
            labreport.LR_APOLIPOPROTEIN_B_APOB = data['LR_APOLIPOPROTEIN_B_APOB']
            labreport.LR_APOB_APOA_RATIO = data['LR_APOB_APOA_RATIO']
            labreport.LR_HSCRP = data['LR_HSCRP']
            labreport.LR_SERUM_COPPER = data['LR_SERUM_COPPER']
            labreport.LR_SERUM_ZINC = data['LR_SERUM_ZINC']
            labreport.LR_TESTOSTERONE = data['LR_TESTOSTERONE']
            labreport.LR_IRON = data['LR_IRON']
            labreport.LR_TOTAL_IRON_BINDING_CAPACITY = data['LR_TOTAL_IRON_BINDING_CAPACITY']
            labreport.LR_TRANSFERRIN_SATURATION = data['LR_TRANSFERRIN_SATURATION']
            labreport.LR_ALKALINE_PHOSPHATASE = data['LR_ALKALINE_PHOSPHATASE']
            labreport.LR_BILIRUBIN_TOTAL = data['LR_BILIRUBIN_TOTAL']
            labreport.LR_BILIRUBIN_DIRECT = data['LR_BILIRUBIN_DIRECT']
            labreport.LR_BILIRUBIN_INDIRECT = data['LR_BILIRUBIN_INDIRECT']
            labreport.LR_GAMMA_GLUTAMYL_TRANSFERASE = data['LR_GAMMA_GLUTAMYL_TRANSFERASE']
            labreport.LR_ASPARTATE_AMINOTRANSFERASE = data['LR_ASPARTATE_AMINOTRANSFERASE']
            labreport.LR_ALANINE_TRANSAMINASE = data['LR_ALANINE_TRANSAMINASE']
            labreport.LR_PROTEIN_TOTAL = data['LR_PROTEIN_TOTAL']
            labreport.LR_ALBUMIN_SERUM = data['LR_ALBUMIN_SERUM']
            labreport.LR_SERUM_ALB = data['LR_SERUM_ALB']
            labreport.LR_SERUM_GLOBULIN = data['LR_SERUM_GLOBULIN']
            labreport.LR_TOTAL_CHOLESTEROL = data['LR_TOTAL_CHOLESTEROL']
            labreport.LR_HDL_CHOLESTEROL_DIRECT = data['LR_HDL_CHOLESTEROL_DIRECT']
            labreport.LR_LDL_CHOLESTEROL_DIRECT = data['LR_LDL_CHOLESTEROL_DIRECT']
            labreport.LR_TRIGLYCERIDES = data['LR_TRIGLYCERIDES']
            labreport.LR_TC_HDL_CHOLESTEROL_RATIO = data['LR_TC_HDL_CHOLESTEROL_RATIO']
            labreport.LR_LDL_HDL_RATIO = data['LR_LDL_HDL_RATIO']
            labreport.LR_VLDL_CHOLESTEROL = data['LR_VLDL_CHOLESTEROL']
            labreport.LR_NON_HDL_CHOLESTEROL = data['LR_NON_HDL_CHOLESTEROL']
            labreport.LR_TOTAL_TRIIODOTHYRONINE = data['LR_TOTAL_TRIIODOTHYRONINE']
            labreport.LR_TOTAL_THYROXINE = data['LR_TOTAL_THYROXINE']
            labreport.LR_THYROID_STIMULATING_HORMONE = data['LR_THYROID_STIMULATING_HORMONE']
            labreport.LR_BLOOD_UREA_NITROGEN = data['LR_BLOOD_UREA_NITROGEN']
            labreport.LR_CREATININE_SERUM = data['LR_CREATININE_SERUM']
            labreport.LR_BUN_SR_CREATININE_RATIO = data['LR_BUN_SR_CREATININE_RATIO']
            labreport.LR_CALCIUM = data['LR_CALCIUM']
            labreport.LR_URIC_ACID = data['LR_URIC_ACID']
            labreport.LR_EST_GLOMERULAR_FILTRATION_RATE = data['LR_EST_GLOMERULAR_FILTRATION_RATE']


        else:

            labreport = LabReportModel(LR_user_id, **data)

        labreport.save_to_db()

        return {
        "Status" : "Success",
        "Response" : labreport.json()
        },201

    @jwt_required
    def delete(self, LR_user_id):
        labreport = LabReportModel.find_by_id(LR_user_id)
        if labreport:
            labreport.delete_from_db()
            return {
            "Status" : "Status",
            'Response': 'Item deleted successfully.'},201
        else:
            return {
            "Status" : "Error",
            'Response': ' Item Not Found'},404
