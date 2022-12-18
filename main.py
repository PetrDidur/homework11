from flask import Flask, request, render_template, app
from jinja2 import Template

import utils
from utils import load_candidate_from_json, get_candidates_by_name
path = "candidates.json"

app = Flask(__name__)


@app.route("/")
def index():
    candidates = load_candidate_from_json(path)
    return render_template('list.html', candidates=candidates)


@app.route("/candidates/<int:pk>")
def get_candidates(pk):
    candidate = utils.get_candidate(pk)
    return render_template('card.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def get_candidate_by_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates, count_candidates=len(candidates))


@app.route("/skill/<skill>")
def get_candidates_by_skills(skill):
    candidates = utils.get_candidates_by_skill(skill.lower())
    return render_template('skill.html', candidates=candidates, count_candidates=len(candidates))





app.run(debug=True)



