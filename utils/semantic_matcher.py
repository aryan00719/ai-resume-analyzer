from sentence_transformers import SentenceTransformer, util

# Lazy load model (important for memory management on free tiers)
model = None

def get_model():
    global model
    if model is None:
        model = SentenceTransformer("all-MiniLM-L6-v2")
    return model

def semantic_skill_match(resume_text, jd_text):
    m = get_model()
    resume_embedding = m.encode(resume_text, convert_to_tensor=True)
    jd_embedding = m.encode(jd_text, convert_to_tensor=True)

    similarity = util.cos_sim(resume_embedding, jd_embedding).item()

    return round(similarity * 100, 2)