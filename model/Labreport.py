from run import db
from model.user import UserModel


class LabReportModel(db.Model):
    __tablename__ = 'LabReport'


    LR_id = db.Column(db.Integer, primary_key=True)
    LR_user_id  = db.Column(db.Integer,db.ForeignKey('users.u_id'))
    LR_HPLC = db.Column(db.Float, nullable = True)
    LR_AVERAGE_BLOOD_GLUCOSE = db.Column(db.Float, nullable = True)
    LR_TOTAL_LEUCOCYTES_COUNT  = db.Column(db.Float, nullable = True)
    LR_NEUTROPHILS = db.Column(db.Float, nullable = True)
    LR_LYMPHOCYTE_PERCENTAGE = db.Column(db.Float, nullable = True)
    LR_MONOCYTES = db.Column(db.Float, nullable = True)
    LR_EOSINOPHILS = db.Column(db.Float, nullable = True)
    LR_BASOPHILS = db.Column(db.Float, nullable = True)
    LR_IMMATURE_GRANULOCYTE_PERCENTAGE = db.Column(db.Float, nullable = True)
    LR_NEUTROPHILS_ABSOLUTE_COUNT = db.Column(db.Float, nullable = True)
    LR_LYMPHOCYTES_ABSOLUTE_COUNT = db.Column(db.Float, nullable = True)
    LR_MONOCYTES_ABSOLUTE_COUNT = db.Column(db.Float, nullable = True)
    LR_BASOPHILS_ABSOLUTE_COUNT = db.Column(db.Float, nullable = True)
    LR_EOSINOPHILS_ABSOLUTE_COUNT = db.Column(db.Float, nullable = True)
    LR_IMMATURE_GRANULOCYTES = db.Column(db.Float, nullable = True)
    LR_TOTAL_RBC = db.Column(db.Float, nullable = True)
    LR_NUCLEATED_RED_BLOOD_CELLS = db.Column(db.Float, nullable = True)
    LR_HEMOGLOBIN = db.Column(db.Float, nullable = True)
    LR_HEMATOCRIT = db.Column(db.Float, nullable = True)
    LR_MEAN_CORPUSCULAR_VOLUME = db.Column(db.Float, nullable = True)
    LR_MEAN_CORPUSCULAR_HEMOGLOBIN = db.Column(db.Float, nullable = True)
    LR_MEAN_CORP_HEMO_CONC = db.Column(db.Float, nullable = True)
    LR_RED_CELL_DISTRIBUTION_WIDTH_SD = db.Column(db.Float, nullable = True)
    LR_RED_CELL_DISTRIBUTION_WIDTH_CV = db.Column(db.Float, nullable = True)
    LR_PLATELET_DISTRIBUTION_WIDTH = db.Column(db.Float, nullable = True)
    LR_MEAN_PLATELET_VOLUME = db.Column(db.Float, nullable = True)
    LR_PLATELET_COUNT = db.Column(db.Float, nullable = True)
    LR_PLATELET_TO_LARGE_CELL_RATIO = db.Column(db.Float, nullable = True)
    LR_PLATELETCRIT = db.Column(db.Float, nullable = True)
    LR_ARSENIC =  db.Column(db.Float, nullable = True)
    LR_CADMIUM = db.Column(db.Float, nullable = True)
    LR_MERCURY = db.Column(db.Float, nullable = True)
    LR_LEAD = db.Column(db.Float, nullable = True)
    LR_CHROMIUM = db.Column(db.Float, nullable = True)
    LR_BARIUM = db.Column(db.Float, nullable = True)
    LR_COBALT = db.Column(db.Float, nullable = True)
    LR_CAESIUM = db.Column(db.Float, nullable = True)
    LR_THALLIUM = db.Column(db.Float, nullable = True)
    LR_URANIUM = db.Column(db.Float, nullable = True)
    LR_STRONTIUM = db.Column(db.Float, nullable = True)
    LR_ANTIMONY = db.Column(db.Float, nullable = True)
    LR_TIN = db.Column(db.Float, nullable = True)
    LR_MOLYBDENUM = db.Column(db.Float, nullable = True)
    LR_SILVER = db.Column(db.Float, nullable = True)
    LR_VANADIUM = db.Column(db.Float, nullable = True)
    LR_BERYLLIUM = db.Column(db.Float, nullable = True)
    LR_BISMUTH = db.Column(db.Float, nullable = True)
    LR_SELENIUM = db.Column(db.Float, nullable = True)
    LR_ALUMINIUM = db.Column(db.Float, nullable = True)
    LR_NICKEL = db.Column(db.Float, nullable = True)
    LR_MANGANESE = db.Column(db.Float, nullable = True)
    LR_HOMOCYSTEINE = db.Column(db.Float, nullable = True)
    LR_CYSTATIN_C = db.Column(db.Float, nullable = True)
    LR_LIPOPROTEIN = db.Column(db.Float, nullable = True)
    LR_VITAMIN_B = db.Column(db.Float, nullable = True)
    LR_APOLIPOPROTEIN_A_APOA = db.Column(db.Float, nullable = True)
    LR_APOLIPOPROTEIN_B_APOB = db.Column(db.Float, nullable = True)
    LR_APOB_APOA_RATIO = db.Column(db.Float, nullable = True)
    LR_HSCRP = db.Column(db.Float, nullable = True)
    LR_SERUM_COPPER = db.Column(db.Float, nullable = True)
    LR_SERUM_ZINC = db.Column(db.Float, nullable = True)
    LR_TESTOSTERONE = db.Column(db.Float, nullable = True)
    LR_IRON = db.Column(db.Float, nullable = True)
    LR_TOTAL_IRON_BINDING_CAPACITY = db.Column(db.Float, nullable = True)
    LR_TRANSFERRIN_SATURATION = db.Column(db.Float, nullable = True)
    LR_ALKALINE_PHOSPHATASE = db.Column(db.Float, nullable = True)
    LR_BILIRUBIN_TOTAL = db.Column(db.Float, nullable = True)
    LR_BILIRUBIN_DIRECT = db.Column(db.Float, nullable = True)
    LR_BILIRUBIN_INDIRECT = db.Column(db.Float, nullable = True)
    LR_GAMMA_GLUTAMYL_TRANSFERASE = db.Column(db.Float, nullable = True)
    LR_ASPARTATE_AMINOTRANSFERASE = db.Column(db.Float, nullable = True)
    LR_ALANINE_TRANSAMINASE = db.Column(db.Float, nullable = True)
    LR_PROTEIN_TOTAL = db.Column(db.Float, nullable = True)
    LR_ALBUMIN_SERUM = db.Column(db.Float, nullable = True)
    LR_SERUM_ALB = db.Column(db.Float, nullable = True)
    LR_SERUM_GLOBULIN = db.Column(db.Float, nullable = True)
    LR_TOTAL_CHOLESTEROL = db.Column(db.Float, nullable = True)
    LR_HDL_CHOLESTEROL_DIRECT = db.Column(db.Float, nullable = True)
    LR_LDL_CHOLESTEROL_DIRECT = db.Column(db.Float, nullable = True)
    LR_TRIGLYCERIDES = db.Column(db.Float, nullable = True)
    LR_TC_HDL_CHOLESTEROL_RATIO = db.Column(db.Float, nullable = True)
    LR_LDL_HDL_RATIO = db.Column(db.Float, nullable = True)
    LR_VLDL_CHOLESTEROL = db.Column(db.Float, nullable = True)
    LR_NON_HDL_CHOLESTEROL = db.Column(db.Float, nullable = True)
    LR_TOTAL_TRIIODOTHYRONINE = db.Column(db.Float, nullable = True)
    LR_TOTAL_THYROXINE = db.Column(db.Float, nullable = True)
    LR_THYROID_STIMULATING_HORMONE = db.Column(db.Float, nullable = True)
    LR_BLOOD_UREA_NITROGEN = db.Column(db.Float, nullable = True)
    LR_CREATININE_SERUM = db.Column(db.Float, nullable = True)
    LR_BUN_SR_CREATININE_RATIO = db.Column(db.Float, nullable = True)
    LR_CALCIUM = db.Column(db.Float, nullable = True)
    LR_URIC_ACID = db.Column(db.Float, nullable = True)
    LR_EST_GLOMERULAR_FILTRATION_RATE = db.Column(db.Float, nullable = True)

    users = db.relationship('UserModel')


    def __init__(self,LR_user_id,LR_HPLC,LR_AVERAGE_BLOOD_GLUCOSE,LR_TOTAL_LEUCOCYTES_COUNT,LR_NEUTROPHILS,
                    LR_LYMPHOCYTE_PERCENTAGE,LR_MONOCYTES,LR_EOSINOPHILS,LR_BASOPHILS,LR_IMMATURE_GRANULOCYTE_PERCENTAGE,
                    LR_NEUTROPHILS_ABSOLUTE_COUNT,LR_LYMPHOCYTES_ABSOLUTE_COUNT,LR_MONOCYTES_ABSOLUTE_COUNT,LR_BASOPHILS_ABSOLUTE_COUNT,
                    LR_EOSINOPHILS_ABSOLUTE_COUNT,LR_IMMATURE_GRANULOCYTES,LR_TOTAL_RBC,LR_NUCLEATED_RED_BLOOD_CELLS,LR_HEMOGLOBIN,LR_HEMATOCRIT,
                    LR_MEAN_CORPUSCULAR_VOLUME,LR_MEAN_CORPUSCULAR_HEMOGLOBIN,
                    LR_MEAN_CORP_HEMO_CONC,LR_RED_CELL_DISTRIBUTION_WIDTH_SD,LR_RED_CELL_DISTRIBUTION_WIDTH_CV,LR_PLATELET_DISTRIBUTION_WIDTH,
                    LR_MEAN_PLATELET_VOLUME,LR_PLATELET_COUNT,LR_PLATELET_TO_LARGE_CELL_RATIO,LR_PLATELETCRIT,LR_ARSENIC,
                    LR_CADMIUM,LR_MERCURY,LR_LEAD,LR_CHROMIUM,LR_BARIUM,LR_COBALT,LR_CAESIUM,LR_THALLIUM,LR_URANIUM,LR_STRONTIUM,LR_ANTIMONY,LR_TIN,LR_MOLYBDENUM,LR_SILVER,
                    LR_VANADIUM,LR_BERYLLIUM,LR_BISMUTH,LR_SELENIUM,LR_ALUMINIUM,LR_NICKEL,LR_MANGANESE,LR_HOMOCYSTEINE,LR_CYSTATIN_C,LR_LIPOPROTEIN,LR_VITAMIN_B,
                    LR_APOLIPOPROTEIN_A_APOA,LR_APOLIPOPROTEIN_B_APOB,LR_APOB_APOA_RATIO,LR_HSCRP,LR_SERUM_COPPER,LR_SERUM_ZINC,LR_TESTOSTERONE,LR_IRON,
                    LR_TOTAL_IRON_BINDING_CAPACITY,LR_TRANSFERRIN_SATURATION,LR_ALKALINE_PHOSPHATASE,LR_BILIRUBIN_TOTAL,LR_BILIRUBIN_DIRECT,LR_BILIRUBIN_INDIRECT,
                    LR_GAMMA_GLUTAMYL_TRANSFERASE,LR_ASPARTATE_AMINOTRANSFERASE,LR_ALANINE_TRANSAMINASE,LR_PROTEIN_TOTAL,LR_ALBUMIN_SERUM,
                    LR_SERUM_ALB,LR_SERUM_GLOBULIN,LR_TOTAL_CHOLESTEROL,LR_HDL_CHOLESTEROL_DIRECT,LR_LDL_CHOLESTEROL_DIRECT,LR_TRIGLYCERIDES,
                    LR_TC_HDL_CHOLESTEROL_RATIO,LR_LDL_HDL_RATIO,LR_VLDL_CHOLESTEROL,LR_NON_HDL_CHOLESTEROL,LR_TOTAL_TRIIODOTHYRONINE,
                    LR_TOTAL_THYROXINE,LR_THYROID_STIMULATING_HORMONE,LR_BLOOD_UREA_NITROGEN,LR_CREATININE_SERUM,LR_BUN_SR_CREATININE_RATIO,
                    LR_CALCIUM,LR_URIC_ACID,LR_EST_GLOMERULAR_FILTRATION_RATE):


                self.LR_user_id = LR_user_id
                self.LR_HPLC = LR_HPLC
                self.LR_AVERAGE_BLOOD_GLUCOSE = LR_AVERAGE_BLOOD_GLUCOSE
                self.LR_TOTAL_LEUCOCYTES_COUNT  = LR_TOTAL_LEUCOCYTES_COUNT
                self.LR_NEUTROPHILS = LR_NEUTROPHILS
                self.LR_LYMPHOCYTE_PERCENTAGE = LR_LYMPHOCYTE_PERCENTAGE
                self.LR_MONOCYTES = LR_MONOCYTES
                self.LR_EOSINOPHILS = LR_EOSINOPHILS
                self.LR_BASOPHILS = LR_BASOPHILS
                self.LR_IMMATURE_GRANULOCYTE_PERCENTAGE = LR_IMMATURE_GRANULOCYTE_PERCENTAGE
                self.LR_NEUTROPHILS_ABSOLUTE_COUNT = LR_NEUTROPHILS_ABSOLUTE_COUNT
                self.LR_LYMPHOCYTES_ABSOLUTE_COUNT = LR_LYMPHOCYTES_ABSOLUTE_COUNT
                self.LR_MONOCYTES_ABSOLUTE_COUNT = LR_MONOCYTES_ABSOLUTE_COUNT
                self.LR_BASOPHILS_ABSOLUTE_COUNT = LR_BASOPHILS_ABSOLUTE_COUNT
                self.LR_EOSINOPHILS_ABSOLUTE_COUNT = LR_EOSINOPHILS_ABSOLUTE_COUNT
                self.LR_IMMATURE_GRANULOCYTES = LR_IMMATURE_GRANULOCYTES
                self.LR_TOTAL_RBC = LR_TOTAL_RBC
                self.LR_NUCLEATED_RED_BLOOD_CELLS = LR_NUCLEATED_RED_BLOOD_CELLS
                self.LR_HEMOGLOBIN = LR_HEMOGLOBIN
                self.LR_HEMATOCRIT = LR_HEMATOCRIT
                self.LR_MEAN_CORPUSCULAR_VOLUME = LR_MEAN_CORPUSCULAR_VOLUME
                self.LR_MEAN_CORPUSCULAR_HEMOGLOBIN = LR_MEAN_CORPUSCULAR_HEMOGLOBIN
                self.LR_MEAN_CORP_HEMO_CONC = LR_MEAN_CORP_HEMO_CONC
                self.LR_RED_CELL_DISTRIBUTION_WIDTH_SD = LR_RED_CELL_DISTRIBUTION_WIDTH_SD
                self.LR_RED_CELL_DISTRIBUTION_WIDTH_CV = LR_RED_CELL_DISTRIBUTION_WIDTH_CV
                self.LR_PLATELET_DISTRIBUTION_WIDTH = LR_PLATELET_DISTRIBUTION_WIDTH
                self.LR_MEAN_PLATELET_VOLUME = LR_MEAN_PLATELET_VOLUME
                self.LR_PLATELET_COUNT = LR_PLATELET_COUNT
                self.LR_PLATELET_TO_LARGE_CELL_RATIO = LR_PLATELET_TO_LARGE_CELL_RATIO
                self.LR_PLATELETCRIT = LR_PLATELETCRIT
                self.LR_ARSENIC = LR_ARSENIC
                self.LR_CADMIUM = LR_CADMIUM
                self.LR_MERCURY = LR_MERCURY
                self.LR_LEAD = LR_LEAD
                self.LR_CHROMIUM = LR_CHROMIUM
                self.LR_BARIUM = LR_BARIUM
                self.LR_COBALT = LR_COBALT
                self.LR_CAESIUM = LR_CAESIUM
                self.LR_THALLIUM = LR_THALLIUM
                self.LR_URANIUM = LR_URANIUM
                self.LR_STRONTIUM = LR_STRONTIUM
                self.LR_ANTIMONY = LR_ANTIMONY
                self.LR_TIN = LR_TIN
                self.LR_MOLYBDENUM = LR_MOLYBDENUM
                self.LR_SILVER = LR_SILVER
                self.LR_VANADIUM = LR_VANADIUM
                self.LR_BERYLLIUM = LR_BERYLLIUM
                self.LR_BISMUTH = LR_BISMUTH
                self.LR_SELENIUM = LR_SELENIUM
                self.LR_ALUMINIUM = LR_ALUMINIUM
                self.LR_NICKEL = LR_NICKEL
                self.LR_MANGANESE = LR_MANGANESE
                self.LR_HOMOCYSTEINE  = LR_HOMOCYSTEINE
                self.LR_CYSTATIN_C = LR_CYSTATIN_C
                self.LR_LIPOPROTEIN = LR_LIPOPROTEIN
                self.LR_VITAMIN_B = LR_VITAMIN_B
                self.LR_APOLIPOPROTEIN_A_APOA = LR_APOLIPOPROTEIN_A_APOA
                self.LR_APOLIPOPROTEIN_B_APOB = LR_APOLIPOPROTEIN_B_APOB
                self.LR_APOB_APOA_RATIO = LR_APOB_APOA_RATIO
                self.LR_HSCRP = LR_HSCRP
                self.LR_SERUM_COPPER = LR_SERUM_COPPER
                self.LR_SERUM_ZINC = LR_SERUM_ZINC
                self.LR_TESTOSTERONE = LR_TESTOSTERONE
                self.LR_IRON = LR_IRON
                self.LR_TOTAL_IRON_BINDING_CAPACITY = LR_TOTAL_IRON_BINDING_CAPACITY
                self.LR_TRANSFERRIN_SATURATION = LR_TRANSFERRIN_SATURATION
                self.LR_ALKALINE_PHOSPHATASE = LR_ALKALINE_PHOSPHATASE
                self.LR_BILIRUBIN_TOTAL = LR_BILIRUBIN_TOTAL
                self.LR_BILIRUBIN_DIRECT = LR_BILIRUBIN_DIRECT
                self.LR_BILIRUBIN_INDIRECT = LR_BILIRUBIN_INDIRECT
                self.LR_GAMMA_GLUTAMYL_TRANSFERASE = LR_GAMMA_GLUTAMYL_TRANSFERASE
                self.LR_ASPARTATE_AMINOTRANSFERASE = LR_ASPARTATE_AMINOTRANSFERASE
                self.LR_ALANINE_TRANSAMINASE = LR_ALANINE_TRANSAMINASE
                self.LR_PROTEIN_TOTAL = LR_PROTEIN_TOTAL
                self.LR_ALBUMIN_SERUM = LR_ALBUMIN_SERUM
                self.LR_SERUM_ALB = LR_SERUM_ALB
                self.LR_SERUM_GLOBULIN = LR_SERUM_GLOBULIN
                self.LR_TOTAL_CHOLESTEROL = LR_TOTAL_CHOLESTEROL
                self.LR_HDL_CHOLESTEROL_DIRECT = LR_HDL_CHOLESTEROL_DIRECT
                self.LR_LDL_CHOLESTEROL_DIRECT = LR_LDL_CHOLESTEROL_DIRECT
                self.LR_TRIGLYCERIDES = LR_TRIGLYCERIDES
                self.LR_TC_HDL_CHOLESTEROL_RATIO = LR_TC_HDL_CHOLESTEROL_RATIO
                self.LR_LDL_HDL_RATIO = LR_LDL_HDL_RATIO
                self.LR_VLDL_CHOLESTEROL = LR_VLDL_CHOLESTEROL
                self.LR_NON_HDL_CHOLESTEROL = LR_NON_HDL_CHOLESTEROL
                self.LR_TOTAL_TRIIODOTHYRONINE = LR_TOTAL_TRIIODOTHYRONINE
                self.LR_TOTAL_THYROXINE = LR_TOTAL_THYROXINE
                self.LR_THYROID_STIMULATING_HORMONE = LR_THYROID_STIMULATING_HORMONE
                self.LR_BLOOD_UREA_NITROGEN = LR_BLOOD_UREA_NITROGEN
                self.LR_CREATININE_SERUM = LR_CREATININE_SERUM
                self.LR_BUN_SR_CREATININE_RATIO = LR_BUN_SR_CREATININE_RATIO
                self.LR_CALCIUM = LR_CALCIUM
                self.LR_URIC_ACID = LR_URIC_ACID
                self.LR_EST_GLOMERULAR_FILTRATION_RATE = LR_EST_GLOMERULAR_FILTRATION_RATE


    def json(self):
        return {
        'LR_HPLC': self.LR_HPLC,
        'LR_AVERAGE_BLOOD_GLUCOSE': self.LR_AVERAGE_BLOOD_GLUCOSE,
        'LR_TOTAL_LEUCOCYTES_COUNT': self.LR_TOTAL_LEUCOCYTES_COUNT ,
        'LR_NEUTROPHILS': self.LR_NEUTROPHILS,
        'LR_LYMPHOCYTE_PERCENTAGE': self.LR_LYMPHOCYTE_PERCENTAGE,
        'LR_MONOCYTES': self.LR_MONOCYTES,
        'LR_EOSINOPHILS': self.LR_EOSINOPHILS,
        'LR_BASOPHILS': self.LR_BASOPHILS,
        'LR_IMMATURE_GRANULOCYTE_PERCENTAGE': self.LR_IMMATURE_GRANULOCYTE_PERCENTAGE,
        'LR_NEUTROPHILS_ABSOLUTE_COUNT': self.LR_NEUTROPHILS_ABSOLUTE_COUNT,
        'LR_LYMPHOCYTES_ABSOLUTE_COUNT': self.LR_LYMPHOCYTES_ABSOLUTE_COUNT,
        'LR_MONOCYTES_ABSOLUTE_COUNT': self.LR_MONOCYTES_ABSOLUTE_COUNT,
        'LR_BASOPHILS_ABSOLUTE_COUNT': self.LR_BASOPHILS_ABSOLUTE_COUNT,
        'LR_EOSINOPHILS_ABSOLUTE_COUNT': self.LR_EOSINOPHILS_ABSOLUTE_COUNT,
        'LR_IMMATURE_GRANULOCYTES': self.LR_IMMATURE_GRANULOCYTES,
        'LR_TOTAL_RBC': self.LR_TOTAL_RBC,
        'LR_NUCLEATED_RED_BLOOD_CELLS': self.LR_NUCLEATED_RED_BLOOD_CELLS,
        'LR_HEMOGLOBIN': self.LR_HEMOGLOBIN,
        'LR_HEMATOCRIT': self.LR_HEMATOCRIT,
        'LR_MEAN_CORPUSCULAR_VOLUME': self.LR_MEAN_CORPUSCULAR_VOLUME,
        'LR_MEAN_CORPUSCULAR_HEMOGLOBIN': self.LR_MEAN_CORPUSCULAR_HEMOGLOBIN,
        'LR_MEAN_CORP_HEMO_CONC': self.LR_MEAN_CORP_HEMO_CONC,
        'LR_RED_CELL_DISTRIBUTION_WIDTH_SD': self.LR_RED_CELL_DISTRIBUTION_WIDTH_SD,
        'LR_RED_CELL_DISTRIBUTION_WIDTH_CV': self.LR_RED_CELL_DISTRIBUTION_WIDTH_CV,
        'LR_PLATELET_DISTRIBUTION_WIDTH': self.LR_PLATELET_DISTRIBUTION_WIDTH,
        'LR_MEAN_PLATELET_VOLUME': self.LR_MEAN_PLATELET_VOLUME,
        'LR_PLATELET_COUNT': self.LR_PLATELET_COUNT,
        'LR_PLATELET_TO_LARGE_CELL_RATIO': self.LR_PLATELET_TO_LARGE_CELL_RATIO,
        'LR_PLATELETCRIT': self.LR_PLATELETCRIT,
        'LR_ARSENIC' : self.LR_ARSENIC,
        'LR_CADMIUM' :self.LR_CADMIUM,
        'LR_MERCURY': self.LR_MERCURY,
        'LR_LEAD': self.LR_LEAD,
        'LR_CHROMIUM': self.LR_CHROMIUM,
        'LR_BARIUM' : self.LR_BARIUM,
        'LR_COBALT': self.LR_COBALT,
        'LR_CAESIUM': self.LR_CAESIUM,
        'LR_THALLIUM': self.LR_THALLIUM,
        'LR_URANIUM': self.LR_URANIUM,
        'LR_STRONTIUM': self.LR_STRONTIUM,
        'LR_ANTIMONY': self.LR_ANTIMONY,
        'LR_TIN': self.LR_TIN,
        'LR_MOLYBDENUM': self.LR_MOLYBDENUM,
        'LR_SILVER': self.LR_SILVER,
        'LR_VANADIUM': self.LR_VANADIUM,
        'LR_BERYLLIUM': self.LR_BERYLLIUM,
        'LR_BISMUTH': self.LR_BISMUTH,
        'LR_SELENIUM': self.LR_SELENIUM,
        'LR_ALUMINIUM': self.LR_ALUMINIUM,
        'LR_NICKEL': self.LR_NICKEL,
        'LR_MANGANESE': self.LR_MANGANESE,
        'LR_HOMOCYSTEINE': self.LR_HOMOCYSTEINE,
        'LR_CYSTATIN_C': self.LR_CYSTATIN_C,
        'LR_LIPOPROTEIN': self.LR_LIPOPROTEIN,
        'LR_VITAMIN_B': self.LR_VITAMIN_B,
        'LR_APOLIPOPROTEIN_A_APOA' : self.LR_APOLIPOPROTEIN_A_APOA,
        'LR_APOLIPOPROTEIN_B_APOB': self.LR_APOLIPOPROTEIN_B_APOB,
        'LR_APOB_APOA_RATIO': self.LR_APOB_APOA_RATIO,
        'LR_HSCRP': self.LR_HSCRP,
        'LR_SERUM_COPPER': self.LR_SERUM_COPPER,
        'LR_SERUM_ZINC': self.LR_SERUM_ZINC,
        'LR_TESTOSTERONE': self.LR_TESTOSTERONE,
        'LR_IRON' :self.LR_IRON,
        'LR_TOTAL_IRON_BINDING_CAPACITY': self.LR_TOTAL_IRON_BINDING_CAPACITY,
        'LR_TRANSFERRIN_SATURATION': self.LR_TRANSFERRIN_SATURATION,
        'LR_ALKALINE_PHOSPHATASE': self.LR_ALKALINE_PHOSPHATASE,
        'LR_BILIRUBIN_TOTAL': self.LR_BILIRUBIN_TOTAL,
        'LR_BILIRUBIN_DIRECT': self.LR_BILIRUBIN_DIRECT,
        'LR_BILIRUBIN_INDIRECT': self.LR_BILIRUBIN_INDIRECT,
        'LR_GAMMA_GLUTAMYL_TRANSFERASE': self.LR_GAMMA_GLUTAMYL_TRANSFERASE,
        'LR_ASPARTATE_AMINOTRANSFERASE': self.LR_ASPARTATE_AMINOTRANSFERASE,
        'LR_ALANINE_TRANSAMINASE': self.LR_ALANINE_TRANSAMINASE,
        'LR_PROTEIN_TOTAL': self.LR_PROTEIN_TOTAL,
        'LR_ALBUMIN_SERUM': self.LR_ALBUMIN_SERUM,
        'LR_SERUM_ALB': self.LR_SERUM_ALB,
        'LR_SERUM_GLOBULIN': self.LR_SERUM_GLOBULIN,
        'LR_TOTAL_CHOLESTEROL': self.LR_TOTAL_CHOLESTEROL,
        'LR_HDL_CHOLESTEROL_DIRECT': self.LR_HDL_CHOLESTEROL_DIRECT,
        'LR_LDL_CHOLESTEROL_DIRECT': self.LR_LDL_CHOLESTEROL_DIRECT,
        'LR_TRIGLYCERIDES': self.LR_TRIGLYCERIDES,
        'LR_TC_HDL_CHOLESTEROL_RATIO': self.LR_TC_HDL_CHOLESTEROL_RATIO,
        'LR_LDL_HDL_RATIO': self.LR_LDL_HDL_RATIO,
        'LR_VLDL_CHOLESTEROL': self.LR_VLDL_CHOLESTEROL,
        'LR_NON_HDL_CHOLESTEROL': self.LR_NON_HDL_CHOLESTEROL,
        'LR_TOTAL_TRIIODOTHYRONINE': self.LR_TOTAL_TRIIODOTHYRONINE,
        'LR_TOTAL_THYROXINE': self.LR_TOTAL_THYROXINE,
        'LR_THYROID_STIMULATING_HORMONE': self.LR_THYROID_STIMULATING_HORMONE,
        'LR_BLOOD_UREA_NITROGEN': self.LR_BLOOD_UREA_NITROGEN,
        'LR_CREATININE_SERUM': self.LR_CREATININE_SERUM,
        'LR_BUN_SR_CREATININE_RATIO': self.LR_BUN_SR_CREATININE_RATIO,
        'LR_CALCIUM': self.LR_CALCIUM,
        'LR_URIC_ACID': self.LR_URIC_ACID,
        'LR_EST_GLOMERULAR_FILTRATION_RATE': self.LR_EST_GLOMERULAR_FILTRATION_RATE
        }




    @classmethod
    def find_by_id(cls, LR_user_id):
        return cls.query.filter_by(LR_user_id = LR_user_id).first()



    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
