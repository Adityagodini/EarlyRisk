import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, render_template, request
import joblib
from src.predict import predict_academic_risk
from src.career_engine import generate_career_roadmap

app = Flask(__name__)

# Load feature importance
feature_importance = joblib.load("../model/feature_importance.pkl")
top_features = feature_importance.head(5)


# -------------------------
# HOME PAGE
# -------------------------
@app.route("/")
def home():
    return render_template("home.html")


# -------------------------
# ACADEMIC RISK PAGE
# -------------------------
@app.route("/academic", methods=["GET", "POST"])
def academic():

    if request.method == "POST":

        student_data = {
        "Average attendance on class": int(request.form.get("attendance")),
        "How many hour do you study daily?": int(request.form.get("study_hours")),
        "How many hour do you spent daily in social media?": int(request.form.get("social_media")),
        "How many Credit did you have completed?": int(request.form.get("credits")),
        "Did you ever fall in probation?": request.form.get("probation", "No"),

        # 🔥 New fields
        "Assignment Average": int(request.form.get("assignment_marks")),
        "Internal Marks": int(request.form.get("internal_marks")),
        "Mid Exam Marks": int(request.form.get("mid_marks")),
        "Backlogs": int(request.form.get("backlogs")),
        "Late Submissions": int(request.form.get("late_submissions")),
        "Participation": int(request.form.get("participation")),
        }


        result, confidence, reasons = predict_academic_risk(student_data)

        return render_template(
            "academic.html",
            prediction=result,
            confidence=confidence,
            reasons=reasons,
            top_features=top_features.to_dict(orient="records")
        )

    return render_template("academic.html")

# -------------------------
# CAREER PAGE
# -------------------------
@app.route("/career", methods=["GET", "POST"])
def career():

    career_data = None

    if request.method == "POST":

        interest = request.form.get("interest")
        skills_input = request.form.get("skills")

        if interest and skills_input:

            skills_list = [s.strip() for s in skills_input.split(",") if s.strip()]

            career_data = generate_career_roadmap(interest, skills_list)

    return render_template("career.html", career=career_data)
if __name__ == "__main__":
    app.run(debug=True)


    
    