# utils/skill_normalizer.py

SKILL_SYNONYMS = {
    "machine learning": ["ml", "machine-learning"],
    "deep learning": ["dl", "deep-learning"],
    "javascript": ["js"],
    "python": ["py"],
    "sql": ["mysql", "sqlite", "postgresql"],
    "cloud": ["aws", "azure", "gcp"],
    "docker": ["containerization"],
    "react": ["reactjs"],
    "flask": ["flask framework"],
    "django": ["django framework"]
}

def normalize_skills(skills):
    normalized = set()

    for skill in skills:
        skill_lower = skill.lower()
        found = False

        for canonical, variants in SKILL_SYNONYMS.items():
            if skill_lower == canonical or skill_lower in variants:
                normalized.add(canonical)
                found = True
                break

        if not found:
            normalized.add(skill_lower)

    return list(normalized)

# Rule-based inference for higher-level skills
ML_INDICATORS = [
    "scikit-learn",
    "classification",
    "regression",
    "supervised",
    "unsupervised",
    "model training",
    "nlp",
    "computer vision"
]

def infer_high_level_skills(raw_text, skills):
    inferred = set(skills)
    text = raw_text.lower()

    # Infer Machine Learning
    for keyword in ML_INDICATORS:
        if keyword in text:
            inferred.add("machine learning")
            break

    return list(inferred)