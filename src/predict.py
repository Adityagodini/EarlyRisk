# import pandas as pd
# import joblib

# MODEL_PATH = "model/earlyrisk_model.pkl"
# FEATURES_PATH = "model/feature_columns.pkl"


# def load_model():
#     model = joblib.load(MODEL_PATH)
#     feature_columns = joblib.load(FEATURES_PATH)
#     return model, feature_columns


# def predict_academic_risk(input_data: dict):
#     """
#     Predict academic risk using probability threshold tuning.
#     """

#     model, feature_columns = load_model()

#     # Convert input to DataFrame
#     df_new = pd.DataFrame([input_data])

#     # One-hot encode
#     df_new = pd.get_dummies(df_new)

#     # Align with training feature columns
#     df_new = df_new.reindex(columns=feature_columns, fill_value=0)

#     # Get probabilities for both classes
#     probabilities = model.predict_proba(df_new)[0]

#     prob_not_risk = probabilities[0]
#     prob_risk = probabilities[1]

#     # 🔥 THRESHOLD TUNING (adjustable)
#     threshold = 0.40  # Lower than 0.5 to improve recall

#     if prob_risk >= threshold:
#         prediction = 1
#         confidence = prob_risk
#     else:
#         prediction = 0
#         confidence = prob_not_risk

#     result = "At Risk" if prediction == 1 else "Not At Risk"
#     # Personalized Reasons
#     reasons = []

#     if input_data.get("Average attendance on class", 100) < 60:
#         reasons.append("Low Attendance")

#     if input_data.get("How many Credit did you have completed?", 999) < 60:
#         reasons.append("Low Completed Credits")

#     if input_data.get("Did you ever fall in probation?", "No") == "Yes":
#         reasons.append("History of Probation")

#     if input_data.get("How many hour do you study daily?", 10) < 2:
#         reasons.append("Low Study Hours")

#     if input_data.get("How many hour do you spent daily in social media?", 0) > 6:
#         reasons.append("High Social Media Usage")

#     return result, round(confidence * 100, 2), reasons


# # -----------------------------------
# # TEST BLOCK (FOR VS CODE TERMINAL)
# # -----------------------------------
# if __name__ == "__main__":

#     sample_student = {
#         "University Admission year": 2023,
#         "Gender": "Female",
#         "Age": 23,
#         "H.S.C passing year": 2018,
#         "Program": "BCA",
#         "Current Semester": 8,
#         "Do you have meritorious scholarship ?": "No",
#         "Do you use University transportation?": "No",
#         "How many hour do you study daily?": 0,
#         "How many times do you seat for study in a day?": 1,
#         "What is your preferable learning mode?": "Offline",
#         "Do you use smart phone?": "Yes",
#         "Do you have personal Computer?": "No",
#         "How many hour do you spent daily in social media?": 8,
#         "Status of your English language proficiency": "Poor",
#         "Average attendance on class": 55,
#         "Did you ever fall in probation?": "Yes",
#         "Did you ever got suspension?": "No",
#         "Do you attend in teacher consultancy for any kind of academical problems?": "No",
#         "What are the skills do you have ?": "None",
#         "How many hour do you spent daily on your skill development?": 0,
#         "What is you interested area?": "None",
#         "What is your relationship status?": "Single",
#         "Are you engaged with any co-curriculum activities?": "No",
#         "With whom you are living with?": "Hostel",
#         "Do you have any health issues?": "No",
#         "Do you have any physical disabilities?": "No",
#         "How many Credit did you have completed?": 40,
#         "What is your monthly family income?": 15000
#     }

#     # prediction, confidence = predict_academic_risk(sample_student)

#     # print("Prediction:", prediction)
#     # print("Confidence:", confidence, "%")

import pandas as pd
import joblib

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))

MODEL_PATH = os.path.join(PROJECT_ROOT, "model", "earlyrisk_model.pkl")

MODEL_PATH = "../model/earlyrisk_model.pkl"
FEATURES_PATH = os.path.join(PROJECT_ROOT, "model", "feature_columns.pkl")


def load_model():
    model = joblib.load(MODEL_PATH)
    feature_columns = joblib.load(FEATURES_PATH)
    return model, feature_columns


def predict_academic_risk(input_data: dict):

    model, feature_columns = load_model()

    df_new = pd.DataFrame([input_data])
    df_new = pd.get_dummies(df_new)
    df_new = df_new.reindex(columns=feature_columns, fill_value=0)

    probabilities = model.predict_proba(df_new)[0]

    prob_not_risk = probabilities[0]
    prob_risk = probabilities[1]

    threshold = 0.45

    if prob_risk >= threshold:
        prediction = 1
        confidence = prob_risk
    else:
        prediction = 0
        confidence = prob_not_risk

    result = "At Risk" if prediction == 1 else "Not At Risk"

    # ---------------------------------
    # 🔥 EXTENDED PERSONALIZED LOGIC
    # ---------------------------------
    reasons = []

    attendance = input_data.get("Average attendance on class", 100)
    study_hours = input_data.get("How many hour do you study daily?", 10)
    social_media = input_data.get("How many hour do you spent daily in social media?", 0)
    credits = input_data.get("How many Credit did you have completed?", 999)
    probation = input_data.get("Did you ever fall in probation?", "No")

    assignment = input_data.get("Assignment Average", 100)
    internal = input_data.get("Internal Marks", 100)
    mid = input_data.get("Mid Exam Marks", 100)
    backlogs = input_data.get("Backlogs", 0)
    late = input_data.get("Late Submissions", 0)
    participation = input_data.get("Participation", 10)

    # Core academic indicators
    if attendance < 60:
        reasons.append("Low Attendance")

    if study_hours < 2:
        reasons.append("Low Study Hours")

    if social_media > 6:
        reasons.append("High Social Media Usage")

    if credits < 60:
        reasons.append("Low Completed Credits")

    if probation == "Yes":
        reasons.append("History of Probation")

    # Extended academic performance
    if assignment < 50:
        reasons.append("Low Assignment Performance")

    if internal < 50:
        reasons.append("Low Internal Marks")

    if mid < 50:
        reasons.append("Poor Mid Exam Performance")

    if backlogs > 2:
        reasons.append("Multiple Academic Backlogs")

    if late > 3:
        reasons.append("Frequent Late Submissions")

    if participation < 4:
        reasons.append("Low Classroom Participation")

    return result, round(confidence * 100, 2), reasons
