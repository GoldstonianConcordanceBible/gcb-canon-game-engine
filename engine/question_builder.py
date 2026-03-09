def build_questions(verse):

    questions = []

    if "characters" in verse:
        for c in verse["characters"]:
            questions.append({
                "question": f"Which biblical figure appears in {verse['book']} {verse['chapter']}:{verse['verse']}?",
                "answer": c,
                "difficulty": verse.get("difficulty","medium")
            })

    if "events" in verse:
        for e in verse["events"]:
            questions.append({
                "question": f"What biblical event is described in {verse['book']} {verse['chapter']}:{verse['verse']}?",
                "answer": e
            })

    return questions