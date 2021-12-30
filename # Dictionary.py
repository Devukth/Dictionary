# Dictionary

import json
from difflib import get_close_matches

data = json.load(open("dictionary.json"))

def fetch_value(w):
    w = w.lower()
    if (w in data):
        return data[w]

    elif (len(get_close_matches(w, data.keys())) > 0):
        yn = input("Did you mean % s instead? (Y/N)" %get_close_matches(w, data.keys())[0])
        yn = yn.lower()
        if (yn == "y"):
            return data[get_close_matches(w, data.keys())[0]]
        elif (yn == "n"):
            return "Your word isn't in this dictionary"
        else:
            "What did you say? I didn't understand"
    else:
        "This dictionary doesn't have the word"

word = input("word: ")
print(fetch_value(word))
