import json
import os

# Helper function to load JSON files
def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Main function
def rank_candidates():
    # Get file paths
    base_path = os.path.dirname(os.path.dirname(__file__))
    candidates_path = os.path.join(base_path, 'data', 'candidates.json')
    jobs_path = os.path.join(base_path, 'data', 'jobs.json')

    # Load data
    candidates = load_json(candidates_path)
    jobs = load_json(jobs_path)

    result = {}

    # Loop through each job
    for job in jobs:
        job_id = str(job["id"])
        required_skills = set(job["required_skills"])
        min_exp = job["min_experience"]

        scored_candidates = []

        for candidate in candidates:
            candidate_id = candidate["id"]
            skills = set(candidate["skills"])
            exp = candidate["experience"]

            # ❌ Hard constraint: must have all required skills
            if not required_skills.issubset(skills):
                continue

            score = 0

            # ✅ Skill match score
            score += len(required_skills.intersection(skills)) * 10

            # ✅ Experience score
            if exp >= min_exp:
                score += 5

            # Save (score, candidate_id)
            scored_candidates.append((score, candidate_id))

        # 🔽 Sort: highest score first, then smaller ID first (tie-breaker)
        ranked = sorted(scored_candidates, key=lambda x: (-x[0], x[1]))

        # Extract only candidate IDs
        result[job_id] = [cid for _, cid in ranked]

    return result
