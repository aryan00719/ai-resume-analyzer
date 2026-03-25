from utils.resume_parser import clean_text, extract_skills
from utils.skill_normalizer import normalize_skills

def parse_job_description(jd_text):
    cleaned = clean_text(jd_text)
    
    req_idx = cleaned.find("required")
    good_idx = cleaned.find("good to have")
    
    if good_idx != -1:
        if req_idx != -1 and req_idx < good_idx:
            req_text = cleaned[req_idx:good_idx]
        else:
            req_text = cleaned[:good_idx]
        good_text = cleaned[good_idx:]
    else:
        req_text = cleaned
        good_text = ""

    return {
        "required": normalize_skills(extract_skills(req_text)),
        "good_to_have": normalize_skills(extract_skills(good_text)) if good_text else []
    }