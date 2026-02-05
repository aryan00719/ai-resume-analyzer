def weighted_match_skills(resume_skills, jd_skills, required_weight=0.8, good_to_have_weight=0.2):
    resume_set = set(resume_skills)

    required = set(jd_skills.get("required", []))
    good_to_have = set(jd_skills.get("good_to_have", []))

    required_matched = resume_set.intersection(required)
    good_to_have_matched = resume_set.intersection(good_to_have)

    # Required skills dominate the score
    if required:
        required_score = len(required_matched) / len(required)
    else:
        required_score = 1.0

    # Optional skills contribute less
    if good_to_have:
        good_to_have_score = len(good_to_have_matched) / len(good_to_have)
    else:
        good_to_have_score = 0.0

    final_score = int(
        (required_weight * required_score + good_to_have_weight * good_to_have_score) * 100
    )

    missing_skills = (required - required_matched).union(good_to_have - good_to_have_matched)

    return {
        "score": final_score,
        "matched_skills": list(required_matched.union(good_to_have_matched)),
        "missing_skills": list(missing_skills)
    }