from flask import Flask, render_template, request, jsonify
import pdfplumber
import os
from utils.resume_parser import extract_skills, extract_sections, clean_text
from utils.jd_parser import parse_job_description
from utils.similarity import weighted_match_skills
from utils.skill_normalizer import normalize_skills, infer_high_level_skills
from utils.semantic_matcher import semantic_skill_match

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_resume():
    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["resume"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if not file.filename.endswith(".pdf"):
        return jsonify({"error": "Only PDF files allowed"}), 400

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    extracted_text = ""

    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    extracted_text += text + "\n"
    except Exception as e:
        return jsonify({"error": "Failed to read PDF"}), 500

    cleaned_text = clean_text(extracted_text)
    raw_skills = extract_skills(cleaned_text)
    normalized_skills = normalize_skills(raw_skills)
    skills = infer_high_level_skills(extracted_text, normalized_skills)

    sections = extract_sections(extracted_text)

    return jsonify({
        "message": "Resume uploaded successfully",
        "skills": skills,
        "sections": sections
    })

@app.route("/analyze", methods=["POST"])
def analyze_resume():
    data = request.json

    resume_skills = normalize_skills(data.get("resume_skills", []))
    jd_text = data.get("job_description", "")

    jd_skills = parse_job_description(jd_text)

    analysis = weighted_match_skills(resume_skills, jd_skills)
    semantic_score = semantic_skill_match(" ".join(resume_skills), jd_text)

    return jsonify({
        "jd_skills": jd_skills,
        "analysis": analysis,
        "semantic_score": semantic_score
    })

if __name__ == "__main__":
    app.run(debug=True)