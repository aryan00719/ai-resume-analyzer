from sentence_transformers import SentenceTransformer, util

# Load model once (important for performance)
model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_skill_match(resume_text, jd_text):
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)

    similarity = util.cos_sim(resume_embedding, jd_embedding).item()

    return round(similarity * 100, 2)