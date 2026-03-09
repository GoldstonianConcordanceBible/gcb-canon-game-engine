from engine.generator import generate_questions
import json

questions = generate_questions()

with open("exports/mobile_trivia.json","w") as f:
    json.dump(questions,f,indent=2)

print("Questions generated:",len(questions))