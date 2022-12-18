import json


def load_candidate_from_json(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
        return data


def get_candidate(candidate_id):
    for candidate in load_candidate_from_json(path="candidates.json"):
        if candidate['id'] == candidate_id:
            return candidate
    return 'Not Found'


def get_candidates_by_name(candidate_name):
    result = []
    for candidate in load_candidate_from_json(path="candidates.json"):
        if candidate_name.lower() in candidate['name'].lower():
            result.append(candidate_name)
    return result


def get_candidates_by_skill(skill_name):
    result = []
    for candidate in load_candidate_from_json(path="candidates.json"):
        skills = candidate['skills'].lower().split(', ')
        if skill_name in skills:
            result.append(candidate)
    return result

