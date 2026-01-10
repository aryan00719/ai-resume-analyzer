from utils.resume_parser import clean_text
from utils.skill_normalizer import normalize_skills

JD_SKILL_KEYWORDS = [
    "react", "reactjs",
    "javascript", "js",
    "machine learning", "ml",
    "deep learning", "dl",
    "python", "java", "sql", "flask"
]

def parse_job_description(jd_text):
    cleaned = clean_text(jd_text)
    found_skills = []

    for skill in JD_SKILL_KEYWORDS:
        if skill in cleaned:
            found_skills.append(skill)

    # normalize AFTER extraction
    return normalize_skills(found_skills)