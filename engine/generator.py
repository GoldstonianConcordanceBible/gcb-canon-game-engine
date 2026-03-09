import json
from engine.dataset_loader import load_canon
from engine.question_builder import build_questions

def generate_questions():

    verses = load_canon()

    questions = []

    for verse in verses:
        qs = build_questions(verse)
        questions.extend(qs)

    return questions