from run import db
from flask import request
from flask_restful import Resource
from werkzeug.utils import secure_filename
import os
import pandas as pd
import shutil
import json
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from model.LabReportUpload import LabReportUploadModel
from model.Labreport import LabReportModel
from libs.ImgOCR import listToString
from flask_jwt_extended import jwt_required, get_jwt_identity
from pdf2image import convert_from_path
from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError,
 PDFSyntaxError
)


Report_FOLDER = 'static/Reports/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
Temp_FOLDER = 'static/Temp'
    # Word List for Keywords to Fetch Info
word_list = [
    'H.P.L.C',
    'AVERAGE BLOOD GLUCOSE (ABG)',
    'TOTAL LEUCOCYTES COUNT',
    'NEUTROPHILS',
    'LYMPHOCYTE PERCENTAGE',
    'MONOCYTES',
    'EOSINOPHILS',
    'BASOPHILS',
    'IMMATURE GRANULOCYTE PERCENTAGE(IG%)',
    'NEUTROPHILS - ABSOLUTE COUNT',
    'LYMPHOCYTES - ABSOLUTE COUNT',
    'MONOCYTES - ABSOLUTE COUNT',
    'BASOPHILS - ABSOLUTE COUNT',
    'EOSINOPHILS - ABSOLUTE COUNT',
    'IMMATURE GRANULOCYTES(IG)',
    'TOTAL RBC',
    'HEMOGLOBIN',
    'HEMATOCRIT(PCV)',
    'MEAN CORPUSCULAR VOLUME(MCV)',
    'MEAN CORPUSCULAR HEMOGLOBIN(MCH)',
    'MEAN CORP.HEMO.CONC(MCHC)',
    'RED CELL DISTRIBUTION WIDTH - SD(RDW-SD)',
    'RED CELL DISTRIBUTION WIDTH (RDW-CV)',
    'PLATELET DISTRIBUTION WIDTH(PDW)',
    'MEAN PLATELET VOLUME(MPV)',
    'PLATELET COUNT',
    'PLATELET TO LARGE CELL RATIO(PLCR)',
    'PLATELETCRIT(PCT)',
    'ARSENIC',
    'CADMIUM',
    'MERCURY',
    'LEAD',
    'CHROMIUM',
    'BARIUM',
    'COBALT',
    'CAESIUM',
    'THALLIUM',
    'URANIUM',
    'STRONTIUM',
    'ANTIMONY',
    'TIN',
    'MOLYBDENUM',
    'SILVER',
    'VANADIUM',
    'BERYLLIUM',
    'BISMUTH',
    'SELENIUM',
    'ALUMINIUM',
    'NICKEL',
    'MANGANESE',
    'HOMOCYSTEINE',
    'CYSTATIN C',
    'LIPOPROTEIN',
    'VITAMIN D (TOTAL)',
    'VITAMIN B-12',
    'APOLIPOPROTEIN - A1 (APO-A1)',
    'APOLIPOPROTEIN - B (APO-B)',
    'HIGH SENSITIVITY C-REACTIVE PROTEIN (HS-CRP)',
    'SERUM COPPER',
    'SERUM ZINC',
    'TESTOSTERONE',
    'IRON',
    'TOTAL IRON BINDING CAPACITY (TIBC)',
    '% TRANSFERRIN SATURATION',
    'TRANSFERRIN SATURATION',
    'ALKALINE PHOSPHATASE',
    'BILIRUBIN - TOTAL',
    'BILIRUBIN -DIRECT',
    'BILIRUBIN (INDIRECT)',
    'GAMMA GLUTAMYL TRANSFERASE (GGT)',
    'ASPARTATE AMINOTRANSFERASE (SGOT )',
    'ALANINE TRANSAMINASE (SGPT)',
    'PROTEIN - TOTAL',
    'ALBUMIN - SERUM',
    'SERUM ALB/GLOBULIN RATIO',
    'SERUM GLOBULIN',
    'TOTAL CHOLESTEROL',
    'HDL CHOLESTEROL - DIRECT',
    'LDL CHOLESTEROL - DIRECT',
    'TRIGLYCERIDES',
    'TC/ HDL CHOLESTEROL RATIO',
    'LDL / HDL RATIO',
    'VLDL CHOLESTEROL',
    'NON-HDL CHOLESTEROL',
    'TOTAL TRIIODOTHYRONINE (T3)',
    'TOTAL THYROXINE',
    'THYROID STIMULATING HORMONE',
    'BLOOD UREA NITROGEN (BUN)',
    'CREATININE - SERUM',
    'BUN / SR.CREATININE RATIO',
    'CALCIUM',
    'URIC ACID',
    'EST. GLOMERULAR FILTRATION RATE',
    'APO B / APO Ai RATIO (APO B/A1)',
    ]


# Wordlist to Delete Useless data from the list
stopwords = ['0.02-0.1','3.9-4.8','58-159','X103pL','X103/pL','-','4.0-10.0','X103/uL','2.0-7.0','1.0-3.0','%','CLIA','ng/d|','ug/l 0.10 - 0.80',
                 'C.LI.A','HIU/ml','C.L.L.A','(SGOT','(SGOT)','CLA','<2','20.0-40.0','0.0-0.4','ul','39.0-46.0','0.0-0.3','C.L.I.A',
                '20-40','PERCENTAGE(IG%)','0-0.5','40-80','0.0-6.0','0.0-6.0','0-0.1','mg/dl','CLIA','HIU/ml','U/I','12.0-15.0',
                '<2','0-10','<','>', 'X', '103', '/', 'pL', '0.2-1','X1046/pL','<0.01','g/dL','13-17','fl','83-101','C.M.1.A','ng/di',
                'pq', '27-32','g/dL', '31.5-34.5','0-0.3','40-50','fL', '39-46','11.6-14','9.6-15.2','4.5-5.5','g/dl','25-OH',
                 'IMMUNOTURBIDIMETRY','ICP-MS','ug/l','<5','ug/I','0.10 - 1.50','<1','<4','<4','<15','yumol/L','0.10 - 0.80',
             'mg/L','(A)','[LP(A)]','pg/ml','mg/dL','ng/dL','Hg/dl','yg/dL',' CLIA','u/l','am/dl','8 - 38','< 0.8',
               'PHOTOMETRY','CALCULATED','(eGFR)', 'Ratio', '9:1-23:1', '(mg/dl)','0.02-0.5','X10%6/uL =:','36.0-46.0',
                 'mL/min/1.73', 'm2','uIU/ml', '0.3-5.5','85-130','35-80','125-200','gm/dL', '2.5-3.4','u/|', '<35','(',')','0.35 - 4.94',
                'u/I', '<55','gm/dl', '3.2-4.8''5.7-8.2','6.5-12','19.7-42.4','0.19-0.39','0.3-1.2','0-0.9','5.7-8.2',
                '3.2-4.8','3-5', 'ng/dl', '60-200','ug/dl', '4.5-12','7-25','0.6-1.1','8.8-10.6','-7.3','5-40','U/L','1.5-3.5',
                'RATIO','150-400','4.0-10.0','25-200','B12 pg/mL 911','B12' ,'pg/mL','911','0.2-1.0','uL','0.0-10.0','0.02-0.1',
                '83.0-101.0','27.0-32.0','3.2-6.1','0.5-0.8','C.M.1.A 0.35','C.M.1.A ng/di','ma/dl','0.9-2','<31','11.6-14.0','27.0-32.0','X%/uL','=:','=:',

            ]



class LabReportUpload(Resource):




    @jwt_required
    def post(self,LR_user_id):
        def solve(lis):
            for x in lis:
                try:
                    float(x)
                    return True
                except:
                    return False

        def ocr_core(filename):

            text = pytesseract.pytesseract.image_to_string(Image.open(filename))
            return text
        def allowed_file(filename):
            return '.' in filename and \
                filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS




        userid = get_jwt_identity()
        folder = f"user_{userid}"

        file = request.files['inputFile']



#        folder = f"user_{user_id}"
#        print(user_id)

        if file and allowed_file(file.filename):
            #file.save('extracted_file.pdf')
            filename = secure_filename(file.filename)
            if os.path.isdir(Report_FOLDER+'/'+folder):
                file.save(os.path.join(Report_FOLDER,folder, filename))
                path_loc = os.path.join(Report_FOLDER,folder, filename)
                #DataFile os.path.join(Report_FOLDER,folder, filename)
                raw_text = []
                images = convert_from_path(path_loc)
                for i, image in enumerate(images):
                    fname = "image" + str(i) + ".png"
                #    image.save(fname, "PNG")
                    if os.path.isdir(Temp_FOLDER+'/'+folder):
                        image.save(os.path.join(Temp_FOLDER,folder,fname),"PNG")
                    else:
                        os.makedirs(Temp_FOLDER+'/'+folder)
                        image.save(os.path.join(Temp_FOLDER,folder,fname),"PNG")
                    fpath = os.path.join(Temp_FOLDER,folder,'image' + str(i) + '.png')
                    text  =  ocr_core(fpath)
                    text = listToString(text)
                    raw_text.append(text)
                    extracted_text = listToString(raw_text)
                    #os.remove(fname)
                    #os.remove('extracted_file.pdf')
                    path = os.path.join(Temp_FOLDER,folder)
                    shutil.rmtree(path)
                    #print(extracted_text)


            else:
                os.makedirs(Report_FOLDER+'/'+folder)
                file.save(os.path.join(Report_FOLDER,folder, filename))
                path_loc = os.path.join(Report_FOLDER,folder, filename)

                #DataFile os.path.join(Report_FOLDER,folder, filename)
                raw_text = []
                images = convert_from_path(path_loc)
                for i, image in enumerate(images):
                    fname = "image" + str(i) + ".png"
                #    image.save(fname, "PNG")
                    if os.path.isdir(Temp_FOLDER+'/'+folder):
                        image.save(os.path.join(Temp_FOLDER,folder,fname),"PNG")
                    else:
                        os.makedirs(Temp_FOLDER+'/'+folder)
                        image.save(os.path.join(Temp_FOLDER,folder,fname),"PNG")
                    fpath = os.path.join(Temp_FOLDER,folder,'image' + str(i) + '.png')
                    text  =  ocr_core(fpath)
                    text = listToString(text)
                    raw_text.append(text)
                    extracted_text = listToString(raw_text)
                    #print(extracted_text)
                    #os.remove(fname)
                   #os.remove('extracted_file.pdf')
                    path = os.path.join(Temp_FOLDER,folder)
                    shutil.rmtree(path)






        #print(type(Report_Data))
        Report_List = []
        for row in extracted_text.split('\n'):
            for word in list(word_list):
                if row.startswith(word):
                    word = row.split()
                    word = word
                    for word_name in list(word):
                        if word_name in stopwords:
                            word.remove(word_name)
                    for i in word:
                        if  solve(i):
                            null = i
                            word.remove(null)
                            i = float(i)
                    word = [x for x in word if not isinstance(x, int)]
                    word = [' '.join(word)]
                    #print(word)
                    word.append(i)
                    #word.remove(str(i))
                    #print(word)

                    Report_List.append(word)
        extracted_DataFrame = pd.DataFrame(Report_List)
        #Data Cleaning
        extracted_DataFrame.columns = ['Keys','Values']
    #        extracted_DataFrame.rename(columns={'Keys':'Values'},inplace=True)
        extracted_DataFrame['Keys'] = extracted_DataFrame['Keys'].str.replace('\d+', '')
        extracted_DataFrame['Keys'] = extracted_DataFrame['Keys'].str.replace('\.','')
        extracted_DataFrame['Keys'] = extracted_DataFrame['Keys'].str.replace('\-','')
        extracted_DataFrame['Keys'] = extracted_DataFrame['Keys'].str.rstrip()
        extracted_DataFrame['Values'] = extracted_DataFrame['Values'].apply(lambda x: pd.to_numeric(x, errors = 'coerce')).dropna()
        extracted_DataFrame = extracted_DataFrame.dropna(axis=0)
        #DataFrame to Dictionary
        extracted_Dictionary = extracted_DataFrame.set_index('Keys')['Values'].to_dict()

        Report_Dictionary = {}

        if 'HPLC' in extracted_Dictionary.keys():
            HPLC = extracted_Dictionary['HPLC']
            Report_Dictionary["LR_HPLC"] = HPLC
        else:
            Report_Dictionary["LR_HPLC"] = None
        if 'AVERAGE BLOOD GLUCOSE (ABG)' in extracted_Dictionary.keys():
            AVERAGE_BLOOD_GLUCOSE = extracted_Dictionary['AVERAGE BLOOD GLUCOSE (ABG)']
            Report_Dictionary["LR_AVERAGE_BLOOD_GLUCOSE"] = AVERAGE_BLOOD_GLUCOSE
        else:
            Report_Dictionary["LR_AVERAGE_BLOOD_GLUCOSE"] = None
        if 'TOTAL LEUCOCYTES COUNT' in extracted_Dictionary.keys():
            TOTAL_LEUCOCYTES_COUNT = extracted_Dictionary['TOTAL LEUCOCYTES COUNT']
            Report_Dictionary["LR_TOTAL_LEUCOCYTES_COUNT"] = TOTAL_LEUCOCYTES_COUNT
        else:
            Report_Dictionary["LR_TOTAL_LEUCOCYTES_COUNT"] = None

        if 'NEUTROPHILS' in extracted_Dictionary.keys():
            NEUTROPHILS = extracted_Dictionary['NEUTROPHILS']
            Report_Dictionary["LR_NEUTROPHILS"] = NEUTROPHILS
        else:
            Report_Dictionary["LR_NEUTROPHILS"] = None

        if 'LYMPHOCYTE PERCENTAGE' in extracted_Dictionary.keys():
            LYMPHOCYTE_PERCENTAGE = extracted_Dictionary['LYMPHOCYTE PERCENTAGE']
            Report_Dictionary["LR_LYMPHOCYTE_PERCENTAGE"] = LYMPHOCYTE_PERCENTAGE
        else:
            Report_Dictionary["LR_LYMPHOCYTE_PERCENTAGE"] = None

        if 'MONOCYTES' in extracted_Dictionary.keys():
            MONOCYTES = extracted_Dictionary['MONOCYTES']
            Report_Dictionary["LR_MONOCYTES"] = MONOCYTES
        else:
            Report_Dictionary["LR_MONOCYTES"] = None

        if 'EOSINOPHILS' in extracted_Dictionary.keys():
            EOSINOPHILS = extracted_Dictionary['EOSINOPHILS']
            Report_Dictionary["LR_EOSINOPHILS"] = EOSINOPHILS
        else:
            Report_Dictionary["LR_EOSINOPHILS"] = None

        if 'BASOPHILS' in extracted_Dictionary.keys():
            BASOPHILS = extracted_Dictionary['BASOPHILS']
            Report_Dictionary["LR_BASOPHILS"] = BASOPHILS
        else:
            Report_Dictionary["LR_BASOPHILS"] = None

        if 'IMMATURE GRANULOCYTE' in extracted_Dictionary.keys():
            IMMATURE_GRANULOCYTE_PERCENTAGE = extracted_Dictionary['IMMATURE GRANULOCYTE']
            Report_Dictionary["LR_IMMATURE_GRANULOCYTE_PERCENTAGE"] = IMMATURE_GRANULOCYTE_PERCENTAGE
        else:
            Report_Dictionary["LR_IMMATURE_GRANULOCYTE_PERCENTAGE"] = None

        if 'NEUTROPHILS ABSOLUTE COUNT' in extracted_Dictionary.keys():
            NEUTROPHILS_ABSOLUTE_COUNT = extracted_Dictionary['NEUTROPHILS ABSOLUTE COUNT']
            Report_Dictionary["LR_NEUTROPHILS_ABSOLUTE_COUNT"] = NEUTROPHILS_ABSOLUTE_COUNT
        else:
            Report_Dictionary["LR_NEUTROPHILS_ABSOLUTE_COUNT"] = None

        if 'LYMPHOCYTES ABSOLUTE COUNT' in extracted_Dictionary.keys():
            LYMPHOCYTES_ABSOLUTE_COUNT = extracted_Dictionary['LYMPHOCYTES ABSOLUTE COUNT']
            Report_Dictionary["LR_LYMPHOCYTES_ABSOLUTE_COUNT"] = LYMPHOCYTES_ABSOLUTE_COUNT
        else:
            Report_Dictionary["LR_LYMPHOCYTES_ABSOLUTE_COUNT"] = None

        if 'MONOCYTES ABSOLUTE COUNT' in extracted_Dictionary.keys():
            MONOCYTES_ABSOLUTE_COUNT = extracted_Dictionary['MONOCYTES ABSOLUTE COUNT']
            Report_Dictionary["LR_MONOCYTES_ABSOLUTE_COUNT"] = MONOCYTES_ABSOLUTE_COUNT
        else:
            Report_Dictionary["LR_MONOCYTES_ABSOLUTE_COUNT"] = None

        if 'BASOPHILS ABSOLUTE COUNT' in extracted_Dictionary.keys():
            BASOPHILS_ABSOLUTE_COUNT = extracted_Dictionary['BASOPHILS ABSOLUTE COUNT']
            Report_Dictionary["LR_BASOPHILS_ABSOLUTE_COUNT"] = BASOPHILS_ABSOLUTE_COUNT
        else:
            Report_Dictionary["LR_BASOPHILS_ABSOLUTE_COUNT"] = None

        if 'EOSINOPHILS ABSOLUTE COUNT' in extracted_Dictionary.keys():
            EOSINOPHILS_ABSOLUTE_COUNT = extracted_Dictionary['EOSINOPHILS ABSOLUTE COUNT']
            Report_Dictionary["LR_EOSINOPHILS_ABSOLUTE_COUNT"] = EOSINOPHILS_ABSOLUTE_COUNT
        else:
            Report_Dictionary["LR_EOSINOPHILS_ABSOLUTE_COUNT"] = None

        if 'IMMATURE GRANULOCYTES(IG)' in extracted_Dictionary.keys():
            IMMATURE_GRANULOCYTES = extracted_Dictionary['IMMATURE GRANULOCYTES(IG)']
            Report_Dictionary["LR_IMMATURE_GRANULOCYTES"] = IMMATURE_GRANULOCYTES
        else:
            Report_Dictionary["LR_IMMATURE_GRANULOCYTES"] = None

        if 'TOTAL RBC' in extracted_Dictionary.keys():
            TOTAL_RBC = extracted_Dictionary['TOTAL RBC']
            Report_Dictionary["LR_TOTAL_RBC"] = TOTAL_RBC
        else:
            Report_Dictionary["LR_TOTAL_RBC"] = None

        if 'NUCLEATED RED BLOOD CELLS' in extracted_Dictionary.keys():
            NUCLEATED_RED_BLOOD_CELLS = extracted_Dictionary['NUCLEATED RED BLOOD CELLS']
            Report_Dictionary["LR_NUCLEATED_RED_BLOOD_CELLS"] = NUCLEATED_RED_BLOOD_CELL

        else:
            Report_Dictionary["LR_NUCLEATED_RED_BLOOD_CELLS"] = None


        if 'HEMOGLOBIN' in extracted_Dictionary.keys():
            HEMOGLOBIN = extracted_Dictionary['HEMOGLOBIN']
            Report_Dictionary["LR_HEMOGLOBIN"] = HEMOGLOBIN
        else:
            Report_Dictionary["LR_HEMOGLOBIN"] = None

        if 'HEMATOCRIT(PCV)' in extracted_Dictionary.keys():
            HEMATOCRIT = extracted_Dictionary['HEMATOCRIT(PCV)']
            Report_Dictionary["LR_HEMATOCRIT"] = HEMATOCRIT
        else:
            Report_Dictionary["LR_HEMATOCRIT"] = None

        if 'MEAN CORPUSCULAR VOLUME(MCV)' in extracted_Dictionary.keys():
            MEAN_CORPUSCULAR_VOLUME = extracted_Dictionary['MEAN CORPUSCULAR VOLUME(MCV)']
            Report_Dictionary["LR_MEAN_CORPUSCULAR_VOLUME"] = MEAN_CORPUSCULAR_VOLUME
        else:
            Report_Dictionary["LR_MEAN_CORPUSCULAR_VOLUME"] = None

        if 'MEAN CORPUSCULAR HEMOGLOBIN(MCH)' in extracted_Dictionary.keys():
            MEAN_CORPUSCULAR_HEMOGLOBIN = extracted_Dictionary['MEAN CORPUSCULAR HEMOGLOBIN(MCH)']
            Report_Dictionary["LR_MEAN_CORPUSCULAR_HEMOGLOBIN"] = MEAN_CORPUSCULAR_HEMOGLOBIN
        else:
            Report_Dictionary["LR_MEAN_CORPUSCULAR_HEMOGLOBIN"] = None

        if 'MEAN CORPHEMOCONC(MCHC)' in extracted_Dictionary.keys():
            MEAN_CORP_HEMO_CONC = extracted_Dictionary['MEAN CORPHEMOCONC(MCHC)']
            Report_Dictionary["LR_MEAN_CORP_HEMO_CONC"] = MEAN_CORP_HEMO_CONC
        else:
            Report_Dictionary["LR_MEAN_CORP_HEMO_CONC"] = None

        if 'RED CELL DISTRIBUTION WIDTH SD(RDWSD)' in extracted_Dictionary.keys():
            RED_CELL_DISTRIBUTION_WIDTH_SD = extracted_Dictionary['RED CELL DISTRIBUTION WIDTH SD(RDWSD)']
            Report_Dictionary["LR_RED_CELL_DISTRIBUTION_WIDTH_SD"] = RED_CELL_DISTRIBUTION_WIDTH_SD
        else:
            Report_Dictionary["LR_RED_CELL_DISTRIBUTION_WIDTH_SD"] = None

        if 'RED CELL DISTRIBUTION WIDTH (RDWCV)' in extracted_Dictionary.keys():
            RED_CELL_DISTRIBUTION_WIDTH_CV = extracted_Dictionary['RED CELL DISTRIBUTION WIDTH (RDWCV)']
            Report_Dictionary["LR_RED_CELL_DISTRIBUTION_WIDTH_CV"] = RED_CELL_DISTRIBUTION_WIDTH_CV
        else:
            Report_Dictionary["LR_RED_CELL_DISTRIBUTION_WIDTH_CV"] = None

        if 'PLATELET DISTRIBUTION WIDTH(PDW)' in extracted_Dictionary.keys():
            PLATELET_DISTRIBUTION_WIDTH = extracted_Dictionary['PLATELET DISTRIBUTION WIDTH(PDW)']
            Report_Dictionary["LR_PLATELET_DISTRIBUTION_WIDTH"] = PLATELET_DISTRIBUTION_WIDTH
        else:
            Report_Dictionary["LR_PLATELET_DISTRIBUTION_WIDTH"] = None

        if 'MEAN PLATELET VOLUME(MPV)' in extracted_Dictionary.keys():
            MEAN_PLATELET_VOLUME = extracted_Dictionary['MEAN PLATELET VOLUME(MPV)']
            Report_Dictionary["LR_MEAN_PLATELET_VOLUME"] = MEAN_PLATELET_VOLUME
        else:
            Report_Dictionary["LR_MEAN_PLATELET_VOLUME"] = None

        if 'PLATELET COUNT' in extracted_Dictionary.keys():
            PLATELET_COUNT = extracted_Dictionary['PLATELET COUNT']
            Report_Dictionary["LR_PLATELET_COUNT"] = PLATELET_COUNT
        else:
            Report_Dictionary["LR_PLATELET_COUNT"] = None

        if 'PLATELET TO LARGE CELL RATIO(PLCR)' in extracted_Dictionary.keys():
            PLATELET_TO_LARGE_CELL_RATIO = extracted_Dictionary['PLATELET TO LARGE CELL RATIO(PLCR)']
            Report_Dictionary["LR_PLATELET_TO_LARGE_CELL_RATIO"] = PLATELET_TO_LARGE_CELL_RATIO
        else:
            Report_Dictionary["LR_PLATELET_TO_LARGE_CELL_RATIO"] = None

        if 'PLATELETCRIT(PCT)' in extracted_Dictionary.keys():
            PLATELETCRIT = extracted_Dictionary['PLATELETCRIT(PCT)']
            Report_Dictionary["LR_PLATELETCRIT"] = PLATELETCRIT
        else:
            Report_Dictionary["LR_PLATELETCRIT"] = None

        if 'ARSENIC' in extracted_Dictionary.keys():
            ARSENIC = extracted_Dictionary['ARSENIC']
            Report_Dictionary["LR_ARSENIC"] = ARSENIC
        else:
            Report_Dictionary["LR_ARSENIC"] = None


        if 'CADMIUM' in extracted_Dictionary.keys():
            CADMIUM = extracted_Dictionary['CADMIUM']
            Report_Dictionary["LR_CADMIUM"] = CADMIUM
        else:
            Report_Dictionary["LR_CADMIUM"] = None


        if 'MERCURY' in extracted_Dictionary.keys():
            MERCURY = extracted_Dictionary['MERCURY']
            Report_Dictionary["LR_MERCURY"] = MERCURY
        else:
            Report_Dictionary["LR_MERCURY"] = None


        if 'LEAD' in extracted_Dictionary.keys():
            LEAD = extracted_Dictionary['LEAD']
            Report_Dictionary["LR_LEAD"] = LEAD
        else:
            Report_Dictionary["LR_LEAD"] = None


        if 'CHROMIUM' in extracted_Dictionary.keys():
            CHROMIUM = extracted_Dictionary['CHROMIUM']
            Report_Dictionary["LR_CHROMIUM"] = CHROMIUM
        else:
            Report_Dictionary["LR_CHROMIUM"] = None


        if 'BARIUM' in extracted_Dictionary.keys():
            BARIUM = extracted_Dictionary['BARIUM']
            Report_Dictionary["LR_BARIUM"] = BARIUM
        else:
            Report_Dictionary["LR_BARIUM"] = None


        if 'COBALT' in extracted_Dictionary.keys():
            COBALT = extracted_Dictionary['COBALT']
            Report_Dictionary["LR_COBALT"] = COBALT
        else:
            Report_Dictionary["LR_COBALT"] = None


        if 'CAESIUM' in extracted_Dictionary.keys():
            CAESIUM = extracted_Dictionary['CAESIUM']
            Report_Dictionary["LR_CAESIUM"] = CAESIUM
        else:
            Report_Dictionary["LR_CAESIUM"] = None


        if 'THALLIUM' in extracted_Dictionary.keys():
            THALLIUM = extracted_Dictionary['THALLIUM']
            Report_Dictionary["LR_THALLIUM"] = THALLIUM
        else:
            Report_Dictionary["LR_THALLIUM"] = None


        if 'URANIUM' in extracted_Dictionary.keys():
            URANIUM = extracted_Dictionary['URANIUM']
            Report_Dictionary["LR_URANIUM"] = URANIUM
        else:
            Report_Dictionary["LR_URANIUM"] = None


        if 'STRONTIUM' in extracted_Dictionary.keys():
            STRONTIUM = extracted_Dictionary['STRONTIUM']
            Report_Dictionary["LR_STRONTIUM"] = STRONTIUM
        else:
            Report_Dictionary["LR_STRONTIUM"] = None


        if 'ANTIMONY' in extracted_Dictionary.keys():
            ANTIMONY = extracted_Dictionary['ANTIMONY']
            Report_Dictionary["LR_ANTIMONY"] = ANTIMONY
        else:
            Report_Dictionary["LR_ANTIMONY"] = None


        if 'TIN' in extracted_Dictionary.keys():
            TIN = extracted_Dictionary['TIN']
            Report_Dictionary["LR_TIN"] = TIN
        else:
            Report_Dictionary["LR_TIN"] = None


        if 'MOLYBDENUM' in extracted_Dictionary.keys():
            MOLYBDENUM = extracted_Dictionary['MOLYBDENUM']
            Report_Dictionary["LR_MOLYBDENUM"] = MOLYBDENUM
        else:
            Report_Dictionary["LR_MOLYBDENUM"] = None



        if 'SILVER' in extracted_Dictionary.keys():
            SILVER = extracted_Dictionary['SILVER']
            Report_Dictionary["LR_SILVER"] = SILVER
        else:
            Report_Dictionary["LR_SILVER"] = None


        if 'VANADIUM' in extracted_Dictionary.keys():
            VANADIUM = extracted_Dictionary['VANADIUM']
            Report_Dictionary["LR_VANADIUM"] = VANADIUM
        else:
            Report_Dictionary["LR_VANADIUM"] = None


        if 'BERYLLIUM' in extracted_Dictionary.keys():
            BERYLLIUM = extracted_Dictionary['BERYLLIUM']
            Report_Dictionary["LR_BERYLLIUM"] = BERYLLIUM
        else:
            Report_Dictionary["LR_BERYLLIUM"] = None



        if 'BISMUTH' in extracted_Dictionary.keys():
            BISMUTH = extracted_Dictionary['BISMUTH']
            Report_Dictionary["LR_BISMUTH"] = BISMUTH
        else:
            Report_Dictionary["LR_BISMUTH"] = None


        if 'SELENIUM' in extracted_Dictionary.keys():
            SELENIUM = extracted_Dictionary['SELENIUM']
            Report_Dictionary["LR_SELENIUM"] = SELENIUM
        else:
            Report_Dictionary["LR_SELENIUM"] = None


        if 'ALUMINIUM' in extracted_Dictionary.keys():
            ALUMINIUM = extracted_Dictionary['ALUMINIUM']
            Report_Dictionary["LR_ALUMINIUM"] = ALUMINIUM
        else:
            Report_Dictionary["LR_ALUMINIUM"] = None


        if 'NICKEL' in extracted_Dictionary.keys():
            NICKEL = extracted_Dictionary['NICKEL']
            Report_Dictionary["LR_NICKEL"] = NICKEL
        else:
            Report_Dictionary["LR_NICKEL"] = None


        if 'MANGANESE' in extracted_Dictionary.keys():
            MANGANESE = extracted_Dictionary['MANGANESE']
            Report_Dictionary["LR_MANGANESE"] = MANGANESE
        else:
            Report_Dictionary["LR_MANGANESE"] = None


        if 'HOMOCYSTEINE' in extracted_Dictionary.keys():
            HOMOCYSTEINE = extracted_Dictionary['HOMOCYSTEINE']
            Report_Dictionary["LR_HOMOCYSTEINE"] = HOMOCYSTEINE
        else:
            Report_Dictionary["LR_HOMOCYSTEINE"] = None


        if 'CYSTATIN C' in extracted_Dictionary.keys():
            CYSTATIN_C = extracted_Dictionary['CYSTATIN C']
            Report_Dictionary["LR_CYSTATIN_C"] = CYSTATIN_C
        else:
            Report_Dictionary["LR_CYSTATIN_C"] = None

        if 'LIPOPROTEIN' in extracted_Dictionary.keys():
            LIPOPROTEIN = extracted_Dictionary['LIPOPROTEIN']
            Report_Dictionary["LR_LIPOPROTEIN"] = LIPOPROTEIN
        else:
            Report_Dictionary["LR_LIPOPROTEIN"] = None


        if 'VITAMIN B' in extracted_Dictionary.keys():
            VITAMIN_B = extracted_Dictionary['VITAMIN B']
            Report_Dictionary["LR_VITAMIN_B"] = VITAMIN_B
        else:
            Report_Dictionary["LR_VITAMIN_B"] = None


        if 'APOLIPOPROTEIN A (APOA)' in extracted_Dictionary.keys():
            APOLIPOPROTEIN_A_APOA = extracted_Dictionary['APOLIPOPROTEIN A (APOA)']
            Report_Dictionary["LR_APOLIPOPROTEIN_A_APOA"] = APOLIPOPROTEIN_A_APOA
        else:
            Report_Dictionary["LR_APOLIPOPROTEIN_A_APOA"] = None


        if 'APOLIPOPROTEIN B (APOB)' in extracted_Dictionary.keys():
            APOLIPOPROTEIN_B_APOB = extracted_Dictionary['APOLIPOPROTEIN B (APOB)']
            Report_Dictionary["LR_APOLIPOPROTEIN_B_APOB"] = APOLIPOPROTEIN_B_APOB
        else:
            Report_Dictionary["LR_APOLIPOPROTEIN_B_APOB"] = None

        if 'APO B APO Ai (APO B/A)' in extracted_Dictionary.keys():
            APOB_APOA_RATIO = extracted_Dictionary['APO B APO Ai (APO B/A)']
            Report_Dictionary["LR_APOB_APOA_RATIO"] = APOB_APOA_RATIO
        else:
            Report_Dictionary["LR_APOB_APOA_RATIO"] = None



        if 'HIGH SENSITIVITY CREACTIVE PROTEIN (HSCRP)' in extracted_Dictionary.keys():
            HSCRP = extracted_Dictionary['HIGH SENSITIVITY CREACTIVE PROTEIN (HSCRP)']
            Report_Dictionary["LR_HSCRP"] = HSCRP
        else:
            Report_Dictionary["LR_HSCRP"] = None


        if 'SERUM COPPER' in extracted_Dictionary.keys():
            SERUM_COPPER = extracted_Dictionary['SERUM COPPER']
            Report_Dictionary["LR_SERUM_COPPER"] = SERUM_COPPER
        else:
            Report_Dictionary["LR_SERUM_COPPER"] = None


        if 'SERUM ZINC' in extracted_Dictionary.keys():
            SERUM_ZINC = extracted_Dictionary['SERUM ZINC']
            Report_Dictionary["LR_SERUM_ZINC"] = SERUM_ZINC
        else:
            Report_Dictionary["LR_SERUM_ZINC"] = None


        if 'TESTOSTERONE' in extracted_Dictionary.keys():
            TESTOSTERONE = extracted_Dictionary['TESTOSTERONE']
            Report_Dictionary["LR_TESTOSTERONE"] = TESTOSTERONE
        else:
            Report_Dictionary["LR_TESTOSTERONE"] = None

        if 'IRON' in extracted_Dictionary.keys():
            IRON = extracted_Dictionary['IRON']
            Report_Dictionary["LR_IRON"] = IRON
        else:
            Report_Dictionary["LR_IRON"] = None

        if 'TOTAL IRON BINDING CAPACITY (TIBC)' in extracted_Dictionary.keys():
            TOTAL_IRON_BINDING_CAPACITY = extracted_Dictionary['TOTAL IRON BINDING CAPACITY (TIBC)']
            Report_Dictionary["LR_TOTAL_IRON_BINDING_CAPACITY"] = TOTAL_IRON_BINDING_CAPACITY
        else:
            Report_Dictionary["LR_TOTAL_IRON_BINDING_CAPACITY"] = None


        if 'TRANSFERRIN SATURATION' in extracted_Dictionary.keys():
            TRANSFERRIN_SATURATION = extracted_Dictionary['TRANSFERRIN SATURATION']
            Report_Dictionary["LR_TRANSFERRIN_SATURATION"] = TRANSFERRIN_SATURATION
        else:
            Report_Dictionary["LR_TRANSFERRIN_SATURATION"] = None

        if 'ALKALINE PHOSPHATASE' in extracted_Dictionary.keys():
            ALKALINE_PHOSPHATASE = extracted_Dictionary['ALKALINE PHOSPHATASE']
            Report_Dictionary["LR_ALKALINE_PHOSPHATASE"] = ALKALINE_PHOSPHATASE
        else:
            Report_Dictionary["LR_ALKALINE_PHOSPHATASE"] = None

        if 'BILIRUBIN TOTAL' in extracted_Dictionary.keys():
            BILIRUBIN_TOTAL = extracted_Dictionary['BILIRUBIN TOTAL']
            Report_Dictionary["LR_BILIRUBIN_TOTAL"] = BILIRUBIN_TOTAL
        else:
            Report_Dictionary["LR_BILIRUBIN_TOTAL"] = None

        if 'BILIRUBIN DIRECT' in extracted_Dictionary.keys():
            BILIRUBIN_DIRECT = extracted_Dictionary['BILIRUBIN DIRECT']
            Report_Dictionary["LR_BILIRUBIN_DIRECT"] = BILIRUBIN_DIRECT
        else:
            Report_Dictionary["LR_BILIRUBIN_DIRECT"] = None

        if 'BILIRUBIN (INDIRECT)' in extracted_Dictionary.keys():
            BILIRUBIN_INDIRECT = extracted_Dictionary['BILIRUBIN (INDIRECT)']
            Report_Dictionary["LR_BILIRUBIN_INDIRECT"] = BILIRUBIN_INDIRECT
        else:
            Report_Dictionary["LR_BILIRUBIN_INDIRECT"] = None

        if 'GAMMA GLUTAMYL TRANSFERASE (GGT)' in extracted_Dictionary.keys():
            GAMMA_GLUTAMYL_TRANSFERASE = extracted_Dictionary['GAMMA GLUTAMYL TRANSFERASE (GGT)']
            Report_Dictionary["LR_GAMMA_GLUTAMYL_TRANSFERASE"] = GAMMA_GLUTAMYL_TRANSFERASE
        else:
            Report_Dictionary["LR_GAMMA_GLUTAMYL_TRANSFERASE"] = None


        if 'ASPARTATE AMINOTRANSFERASE' in extracted_Dictionary.keys():
            ASPARTATE_AMINOTRANSFERASE = extracted_Dictionary['ASPARTATE AMINOTRANSFERASE']
            Report_Dictionary["LR_ASPARTATE_AMINOTRANSFERASE"] = ASPARTATE_AMINOTRANSFERASE
        else:
            Report_Dictionary["LR_ASPARTATE_AMINOTRANSFERASE"] = None

        if 'ALANINE TRANSAMINASE (SGPT)' in extracted_Dictionary.keys():
            ALANINE_TRANSAMINASE = extracted_Dictionary['ALANINE TRANSAMINASE (SGPT)']
            Report_Dictionary["LR_ALANINE_TRANSAMINASE"] = ALANINE_TRANSAMINASE
        else:
            Report_Dictionary["LR_ALANINE_TRANSAMINASE"] = None

        if 'PROTEIN TOTAL' in extracted_Dictionary.keys():
            PROTEIN_TOTAL = extracted_Dictionary['PROTEIN TOTAL']
            Report_Dictionary["LR_PROTEIN_TOTAL"] = PROTEIN_TOTAL
        else:
            Report_Dictionary["LR_PROTEIN_TOTAL"] = None

        if 'ALBUMIN SERUM' in extracted_Dictionary.keys():
            ALBUMIN_SERUM = extracted_Dictionary['ALBUMIN SERUM']
            Report_Dictionary["LR_ALBUMIN_SERUM"] = ALBUMIN_SERUM
        else:
            Report_Dictionary["LR_ALBUMIN_SERUM"] = None

        if 'SERUM ALB/GLOBULIN' in extracted_Dictionary.keys():
            SERUM_ALB = extracted_Dictionary['SERUM ALB/GLOBULIN']
            Report_Dictionary["LR_SERUM_ALB"] = SERUM_ALB
        else:
            Report_Dictionary["LR_SERUM_ALB"] = None

        if 'SERUM GLOBULIN' in extracted_Dictionary.keys():
            SERUM_GLOBULIN = extracted_Dictionary['SERUM GLOBULIN']
            Report_Dictionary["LR_SERUM_GLOBULIN"] = SERUM_GLOBULIN
        else:
            Report_Dictionary["LR_SERUM_GLOBULIN"] = None

        if 'TOTAL CHOLESTEROL' in extracted_Dictionary.keys():
            TOTAL_CHOLESTEROL = extracted_Dictionary['TOTAL CHOLESTEROL']
            Report_Dictionary["LR_TOTAL_CHOLESTEROL"] = TOTAL_CHOLESTEROL
        else:
            Report_Dictionary["LR_TOTAL_CHOLESTEROL"] = None

        if 'HDL CHOLESTEROL DIRECT' in extracted_Dictionary.keys():
            HDL_CHOLESTEROL_DIRECT = extracted_Dictionary['HDL CHOLESTEROL DIRECT']
            Report_Dictionary["LR_HDL_CHOLESTEROL_DIRECT"] = HDL_CHOLESTEROL_DIRECT
        else:
            Report_Dictionary["LR_HDL_CHOLESTEROL_DIRECT"] = None

        if 'LDL CHOLESTEROL DIRECT' in extracted_Dictionary.keys():
            LDL_CHOLESTEROL_DIRECT = extracted_Dictionary['LDL CHOLESTEROL DIRECT']
            Report_Dictionary["LR_LDL_CHOLESTEROL_DIRECT"] = LDL_CHOLESTEROL_DIRECT
        else:
            Report_Dictionary["LR_LDL_CHOLESTEROL_DIRECT"] = None

        if 'TRIGLYCERIDES' in extracted_Dictionary.keys():
            TRIGLYCERIDES = extracted_Dictionary['TRIGLYCERIDES']
            Report_Dictionary["LR_TRIGLYCERIDES"] = TRIGLYCERIDES
        else:
            Report_Dictionary["LR_TRIGLYCERIDES"] = None

        if 'TC/ HDL CHOLESTEROL' in extracted_Dictionary.keys():
            TC_HDL_CHOLESTEROL_RATIO = extracted_Dictionary['TC/ HDL CHOLESTEROL']
            Report_Dictionary["LR_TC_HDL_CHOLESTEROL_RATIO"] = TC_HDL_CHOLESTEROL_RATIO
        else:
            Report_Dictionary["LR_TC_HDL_CHOLESTEROL_RATIO"] = None

        if 'LDL HDL' in extracted_Dictionary.keys():
            LDL_HDL_RATIO = extracted_Dictionary['LDL HDL']
            Report_Dictionary["LR_LDL_HDL_RATIO"] = LDL_HDL_RATIO
        else:
            Report_Dictionary["LR_LDL_HDL_RATIO"] = None


        if 'VLDL CHOLESTEROL' in extracted_Dictionary.keys():
            VLDL_CHOLESTEROL = extracted_Dictionary['VLDL CHOLESTEROL']
            Report_Dictionary["LR_VLDL_CHOLESTEROL"] = VLDL_CHOLESTEROL
        else:
            Report_Dictionary["LR_VLDL_CHOLESTEROL"] = None

        if 'NONHDL CHOLESTEROL' in extracted_Dictionary.keys():
            NON_HDL_CHOLESTEROL = extracted_Dictionary['NONHDL CHOLESTEROL']
            Report_Dictionary["LR_NON_HDL_CHOLESTEROL"] = NON_HDL_CHOLESTEROL
        else:
            Report_Dictionary["LR_NON_HDL_CHOLESTEROL"] = None


        if 'TOTAL TRIIODOTHYRONINE (T)' in extracted_Dictionary.keys():
            TOTAL_TRIIODOTHYRONINE = extracted_Dictionary['TOTAL TRIIODOTHYRONINE (T)']
            Report_Dictionary["LR_TOTAL_TRIIODOTHYRONINE"] = TOTAL_TRIIODOTHYRONINE
        else:
            Report_Dictionary["LR_TOTAL_TRIIODOTHYRONINE"] = None

        if 'TOTAL THYROXINE (T)' in extracted_Dictionary.keys():
            TOTAL_THYROXINE = extracted_Dictionary['TOTAL THYROXINE (T)']
            Report_Dictionary["LR_TOTAL_THYROXINE"] = TOTAL_THYROXINE
        else:
            Report_Dictionary["LR_TOTAL_THYROXINE"] = None

        if 'THYROID STIMULATING HORMONE (TSH)' in extracted_Dictionary.keys():
            THYROID_STIMULATING_HORMONE = extracted_Dictionary['THYROID STIMULATING HORMONE (TSH)']
            Report_Dictionary["LR_THYROID_STIMULATING_HORMONE"] = THYROID_STIMULATING_HORMONE
        else:
            Report_Dictionary["LR_THYROID_STIMULATING_HORMONE"] = None

        if 'BLOOD UREA NITROGEN (BUN)' in extracted_Dictionary.keys():
            BLOOD_UREA_NITROGEN = extracted_Dictionary['BLOOD UREA NITROGEN (BUN)']
            Report_Dictionary["LR_BLOOD_UREA_NITROGEN"] = BLOOD_UREA_NITROGEN
        else:
            Report_Dictionary["LR_BLOOD_UREA_NITROGEN"] = None

        if 'CREATININE SERUM' in extracted_Dictionary.keys():
            CREATININE_SERUM = extracted_Dictionary['CREATININE SERUM']
            Report_Dictionary["LR_CREATININE_SERUM"] = CREATININE_SERUM
        else:
            Report_Dictionary["LR_CREATININE_SERUM"] = None

        if 'BUN SRCREATININE' in extracted_Dictionary.keys():
            BUN_SR_CREATININE_RATIO = extracted_Dictionary['BUN SRCREATININE']
            Report_Dictionary["LR_BUN_SR_CREATININE_RATIO"] = BUN_SR_CREATININE_RATIO
        else:
            Report_Dictionary["LR_BUN_SR_CREATININE_RATIO"] = None

        if 'CALCIUM' in extracted_Dictionary.keys():
            CALCIUM = extracted_Dictionary['CALCIUM']
            Report_Dictionary["LR_CALCIUM"] = CALCIUM
        else:
            Report_Dictionary["LR_CALCIUM"] = None

        if 'URIC ACID' in extracted_Dictionary.keys():
            URIC_ACID = extracted_Dictionary['URIC ACID']
            Report_Dictionary["LR_URIC_ACID"] = URIC_ACID
        else:
            Report_Dictionary["LR_URIC_ACID"] = None


        if 'EST GLOMERULAR FILTRATION RATE' in extracted_Dictionary.keys():
            EST_GLOMERULAR_FILTRATION_RATE = extracted_Dictionary['EST GLOMERULAR FILTRATION RATE']
            Report_Dictionary["LR_EST_GLOMERULAR_FILTRATION_RATE"] = EST_GLOMERULAR_FILTRATION_RATE
        else:
            Report_Dictionary["LR_EST_GLOMERULAR_FILTRATION_RATE"] = None




        labreportupload = LabReportUploadModel(LR_user_id,LR_name=file.filename,LR_report=file.read())
        labreport = LabReportModel(LR_user_id, **Report_Dictionary)

        try:
            labreportupload.save_to_db()
            labreport.save_to_db()

        except:

            return {
            "Status" : "Error",
            'message': 'An Error occurred while saving'}
        return {
        "Status" : "Success",
        "Response" : Report_Dictionary
        },201


    @jwt_required
    def delete(self, LR_user_id):
        labreportupload =LabReportUploadModel.find_by_id(LR_user_id)
        userid = get_jwt_identity()
        folder = f"user_{userid}"

        if labreportupload:
            labreportupload.delete_from_db()
            path = os.path.join(Report_FOLDER,folder)
            shutil.rmtree(path)

            return {
            "Status" : "Success",
            'Response': 'Item deleted successfully.'},201
        return {
        "Status" :"Error",
        'Response': 'Item not found'},404
