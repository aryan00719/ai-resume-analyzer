import re

# Very small but effective skill set (we'll expand later)
SKILLS_DB = [
    "python", "java", "c++", "javascript", "html", "css",
    "react", "flask", "django", "node", "sql", "mysql",
    "mongodb", "machine learning", "deep learning",
    "nlp", "computer vision", "git", "docker", "aws"
]

def clean_text(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def extract_skills(text):
    text = clean_text(text)
    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))

def extract_sections(text):
    sections = {
        "education": [],
        "experience": [],
        "projects": []
    }

    lines = text.split("\n")

    current_section = None

    for line in lines:
        l = line.lower()

        if "education" in l:
            current_section = "education"
            continue
        elif "experience" in l:
            current_section = "experience"
            continue
        elif "project" in l:
            current_section = "projects"
            continue

        if current_section:
            sections[current_section].append(line.strip())

    return sections