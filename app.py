from flask import Flask, render_template, request, jsonify
import pdfplumber
import os
from utils.resume_parser import extract_skills, extract_sections, clean_text
from utils.jd_parser import parse_job_description
from utils.similarity import weighted_match_skills
from utils.skill_normalizer import normalize_skills, infer_high_level_skills
from utils.semantic_matcher import semantic_skill_match

app = Flask(__name__)

# Temporary global state to ensure resume_text passes correctly
session_data = {"resume_text": ""}

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
    session_data["resume_text"] = cleaned_text  # Store globally to ensure it's not lost
    raw_skills = extract_skills(cleaned_text)
    normalized_skills = normalize_skills(raw_skills)
    skills = infer_high_level_skills(extracted_text, normalized_skills)

    sections = extract_sections(extracted_text)
    session_data["resume_sections"] = sections

    return jsonify({
        "message": "Resume uploaded successfully",
        "skills": skills,
        "sections": sections,
        "resume_text": cleaned_text
    })

@app.route("/analyze", methods=["POST"])
def analyze_resume():
    data = request.json

    resume_skills = normalize_skills(data.get("resume_skills", []))
    # Use global state if frontend payload fails to securely deliver the full text
    resume_text = data.get("resume_text", "") or session_data.get("resume_text", "")
    jd_text = data.get("job_description", "")

    if not resume_text.strip():
        return jsonify({"error": "Resume text is empty. Please upload the resume again."}), 400
    
    if not jd_text.strip():
        return jsonify({"error": "Job description is empty. Please provide one."}), 400

    jd_skills = parse_job_description(jd_text)

    analysis = weighted_match_skills(resume_skills, jd_skills)
    
    # Construct semantic input exclusively from the projects section and skills
    sections = session_data.get("resume_sections", {})
    projects_text = " ".join(sections.get("projects", []))
    
    # Strictly bind only projects and generated skills (Drop experience, education, meta details)
    semantic_input = (projects_text + " " + " ".join(resume_skills)).strip()

    # Fallback to resume text only if projects are explicitly completely empty 
    if len(semantic_input) < 10:
        semantic_input = resume_text + " " + " ".join(resume_skills)

    # Compute a singular holistic score
    semantic_score = semantic_skill_match(semantic_input, jd_text)

    return jsonify({
        "jd_skills": jd_skills,
        "analysis": analysis,
        "semantic_score": semantic_score
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)