import json
import os

def load_canon():

    verses = []

    folder = "data/canon"

    for file in os.listdir(folder):
        with open(os.path.join(folder,file)) as f:
            verses.extend(json.load(f))

    return verses