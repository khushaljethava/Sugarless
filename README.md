# Login_Reg

# registration

	POST /registration

	{
	    "u_username": "Khus54645",
	    "u_fullname": "Khushal Jethwa",
	    "u_mobile" : 9662737937,
	    "u_email" : "Khushaljethwa14@.com",
	    "u_Gerder" : "Male",
	    "u_Age" : 25    

	}

	{

# Login


	{
	   "u_mobile" : 9662737937
	}



# Logout

	POST  /logout/access




# pre_existing_condition

	POST : /preexisting/<int:user_id>
	GET : /preexisting/<int:user_id>
	PUT : /preexisting/<int:user_id>
	DELETE : /preexisting/<int:user_id>

Example :  localhost/preexisting/5,
          localhost/preexisting/453,



	{

	"PC_Race" : 1,
	"PC_Smoking": 1,
	"PC_Alcohol": 1,
	"PC_Diabetes": 1,
	"PC_Hear": 1,
	"PC_Blood_Pressure": 1,
	"PC_Chest_Pain": 1,
	"PC_Stroke": 1,
	"PC_Kidney": 1,
	"PC_Blood_Clot": 1,
	"PC_Metal_implants": 1,
	"PC_Asthma": 1,
	"PC_Cancer": 1,
	"PC_Difficulty_Swallowing": 1,
	"PC_Vascular_Problems": 1,
	"PC_Peripheral_Neuropathy": 1,
	"PC_Weightloss": 1,
	"PC_Double_Vision": 1,
	"PC_Night_Sweats": 1,
	"PC_Night_Pain": 1,
	"PC_Neurologic_Condition": 1,
	"PC_Skin_Disease": 1,
	"PC_Spinal_Cord_Injury": 1,
	"PC_Degenerative_Joint_Disease": 1,
	"PC_Sexual_Dysfunction": 1,
	"PC_Bladder": 1,
	"PC_Groin_Numbness": 1,
	"PC_Ringing_in_Ears": 1,
	"PC_Allergy_to_Latex": 1,
	"PC_Head_Injury": 1,
	"PC_Obesity": 1,
	"PC_Chronic_Pain": 1,
	"PC_Fractures": 1,
	"PC_Infection_Dissease": 1,
	"PC_Fever": 1,
	"PC_Lower_Extremety": 1,
	"PC_Nausea": 1,
	"PC_Arthritis": 1,
	"PC_Osteoporosis": 1,
	"PC_Phsychological_Problems": 1,
	"PC_Seizures": 1,
	"PC_Dizziness": 1,
	"PC_Ringing_in_Ears": 1,
	"PC_Allergy_to_Latex": 1,
	"PC_Head_Injury": 1,
	"PC_Obesity": 1,
	"PC_Chronic_Pain": 1,
	"PC_Fractures": 1,
	"PC_Infection_Dissease": 1,
	"PC_Fever": 1,
	"PC_Lower_Extremety": 1,
	"PC_Nausea": 1
	}


# Family History  
		POST : /familyhistory/<int:user_id>/<string:Member>
	  GET : /familyhistory/<int:user_id>/<string:Member>
	  PUT : /familyhistory/<int:user_id>/<string:Member>
	  DELETE : /familyhistory/<int:user_id>/<string:Member>

	  {
	  "FH_Member": "Mother",
	  "FH_Alcoholism": 1,
	  "FH_Allergies": "1" ,
	  "FH_Anesthesia": 1 ,
	  "FH_Anxiety": 1 ,
	  "FH_Arthritis": 1 ,
	  "FH_Asthma": 1 ,
	  "FH_ADHD": 1 ,
	  "FH_Birth_Defects": 1 ,
	  "FH_Blood_Problem": 1 ,
	  "FH_Bone_Joint_Problems": 1 ,
	  "FH_Breast_Disease": 1 ,
	  "FH_Cancer": "1" ,
	  "FH_Chicken_Pox": 1 ,
	  "FH_Colitis": 1 ,
	  "FH_Depression": 1 ,
	  "FH_Diabetes": 1 ,
	  "FH_ENT_Problems": 1 ,
	  "FH_Eating_Disorders": 1 ,
	  "FH_Eczema": 1 ,
	  "FH_Epilepsy": 1 ,
	  "FH_Fertility": 1 ,
	  "FH_Gallbladder": 1 ,
	  "FH_Gynecology": 1 ,
	  "FH_Fever": 1 ,
	  "FH_Headaches": 1 ,
	  "FH_Heart_Problems": 1 ,
	  "FH_Heart_Attack_Over_60": 1 ,
	  "FH_Heart_Attack_Under_60": 1 ,
	  "FH_Heart_Murmur": 1 ,
	  "FH_Hepatitis": 1 ,
	  "FH_High_Blood_Pressure": 1 ,
	  "FH_High_Cholestorol": 1
	  }

# Lab Reports

POST method is not Available.

	  GET : /labreport/<int:user_id>
	  PUT : /labreport/<int:user_id>
	  DELETE : /labreport/<int:user_id>


Parameters for Put Method


	{
	    "LR_HPLC": 5.9,
	    "LR_AVERAGE_BLOOD_GLUCOSE": 123.0,
	    "LR_TOTAL_LEUCOCYTES_COUNT": 8.3,
	    "LR_NEUTROPHILS": 52.2,
	    "LR_LYMPHOCYTE_PERCENTAGE": 42.8,
	    "LR_MONOCYTES": 3.3,
	    "LR_EOSINOPHILS": 1.3,
	    "LR_BASOPHILS": 0.2,
	    "LR_IMMATURE_GRANULOCYTE_PERCENTAGE": 0.2,
	    "LR_NEUTROPHILS_ABSOLUTE_COUNT": null,
	    "LR_LYMPHOCYTES_ABSOLUTE_COUNT": 3.55,
	    "LR_MONOCYTES_ABSOLUTE_COUNT": 0.27,
	    "LR_BASOPHILS_ABSOLUTE_COUNT": 0.02,
	    "LR_EOSINOPHILS_ABSOLUTE_COUNT": null,
	    "LR_IMMATURE_GRANULOCYTES": null,
	    "LR_TOTAL_RBC": 4.83,
	    "LR_NUCLEATED_RED_BLOOD_CELLS": null,
	    "LR_HEMOGLOBIN": 9.4,
	    "LR_HEMATOCRIT": 37.2,
	    "LR_MEAN_CORPUSCULAR_VOLUME": 77.0,
	    "LR_MEAN_CORPUSCULAR_HEMOGLOBIN": 19.5,
	    "LR_MEAN_CORP_HEMO_CONC": 25.3,
	    "LR_RED_CELL_DISTRIBUTION_WIDTH_SD": 54.5,
	    "LR_RED_CELL_DISTRIBUTION_WIDTH_CV": 19.7,
	    "LR_PLATELET_DISTRIBUTION_WIDTH": 10.8,
	    "LR_MEAN_PLATELET_VOLUME": 10.2,
	    "LR_PLATELET_COUNT": 518.0,
	    "LR_PLATELET_TO_LARGE_CELL_RATIO": 25.6,
	    "LR_PLATELETCRIT": 0.53,
	    "LR_ARSENIC": 0.53,
	    "LR_CADMIUM": 0.53,
	    "LR_MERCURY": 0.53,
	    "LR_LEAD": 0.53,
	    "LR_CHROMIUM": 0.53,
	    "COBALT": 0.53,
			"LR_LR_BARIUM": 0.53,
	    "LR_CAESIUM": 0.53,
	    "LR_THALLIUM": 0.53,
	    "LR_URANIUM": 0.53,
	    "LR_STRONTIUM": 0.53,
	    "LR_ANTIMONY": 0.53,
	    "LR_TIN": 0.53,
	    "LR_MOLYBDENUM": 0.53,
	    "LR_SILVER": 0.53,
	    "LR_VANADIUM": 0.53,
	    "LR_BERYLLIUM": 0.53,
	    "LR_BISMUTH": 0.53,
	    "LR_SELENIUM": 0.53,
	    "LR_ALUMINIUM": 0.53,
	    "LR_NICKEL": 0.53,
	    "LR_MANGANESE": 0.53,
	    "LR_HOMOCYSTEINE": 0.53,
	    "LR_CYSTATIN C": 0.53,
	    "LR_LIPOPROTEIN": 0.53,
	    "LR_VITAMIN D (TOTAL)": 0.53,
	    "LR_VITAMIN B-12": 0.53,
	    "LR_APOLIPOPROTEIN - A1 (APO-A1)": 0.53,
	    "LR_APOLIPOPROTEIN - B (APO-B)": 0.53,
	    "LR_APO B / APO A1 RATIO (APO B/A1)": 0.53,
	    "LR_HIGH SENSITIVITY C-REACTIVE PROTEIN (HS-CRP)": 0.53,
	    "LR_SERUM COPPER": 0.53,
	    "LR_SERUM ZINC": 0.53,
	    "LR_TESTOSTERONE": 0.53,
	    "LR_IRON": null,
	    "LR_TOTAL_IRON_BINDING_CAPACITY": null,
	    "LR_TRANSFERRIN_SATURATION": null,
	    "LR_ALKALINE_PHOSPHATASE": 129.0,
	    "LR_BILIRUBIN_TOTAL": 0.32,
	    "LR_BILIRUBIN_DIRECT": 0.11,
	    "LR_BILIRUBIN_INDIRECT": 0.21,
	    "LR_GAMMA_GLUTAMYL_TRANSFERASE": null,
	    "LR_ASPARTATE_AMINOTRANSFERASE": null,
	    "LR_ALANINE_TRANSAMINASE": null,
	    "LR_PROTEIN_TOTAL": null,
	    "LR_ALBUMIN_SERUM": 4.1,
	    "LR_SERUM_ALB": -2.0,
	    "LR_SERUM_GLOBULIN": 3.3,
	    "LR_TOTAL_CHOLESTEROL": 153.0,
	    "LR_HDL_CHOLESTEROL_DIRECT": 44.0,
	    "LR_LDL_CHOLESTEROL_DIRECT": 90.0,
	    "LR_TRIGLYCERIDES": 179.0,
	    "LR_TC_HDL_CHOLESTEROL_RATIO": 3.5,
	    "LR_LDL_HDL_RATIO": 2.1,
	    "LR_VLDL_CHOLESTEROL": 35.8,
			"LR_HSCRP":36.8"
	    "LR_NON_HDL_CHOLESTEROL": 109.2,
	    "LR_TOTAL_TRIIODOTHYRONINE": 115.0,
	    "LR_TOTAL_THYROXINE": 11.9,
	    "LR_THYROID_STIMULATING_HORMONE": 1.57,
	    "LR_BLOOD_UREA_NITROGEN": 8.86,
	    "LR_CREATININE_SERUM": 0.72,
	    "LR_BUN_SR_CREATININE_RATIO": 12.31,
	    "LR_CALCIUM": 8.59,
	    "LR_URIC_ACID": 4.8,
	    "LR_EST_GLOMERULAR_FILTRATION_RATE": null
	}





# Lab Reports Upload (pdf upload)

	  POST : /labreportupload/<int:user_id>
	  DELETE : /labreportupload/<int:user_id>


Key: "inputFile"
Value: "File"




# Retina Upload (image upload)
	  GET : /retinaupload/<int:user_id>
	  POST : /retinaupload/<int:user_id>
	  DELETE : /retinaupload/<int:user_id>

Key: "inputFile"
Value: "File"

# Symptoms Checker
 	 GET : /symptomcheck/<int:SCA_qid>
	 POST /symptomcheck/<int:SCA_qid>

	 {
    "UI_SCA_qid" : 1,
    "UI_SCA_aid" : 3

}
