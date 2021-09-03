import json  # --import json module
import os  # --import os module
from difflib import get_close_matches
from typing import Type  # import get close matches


# -- methods start

# -- Method takes an input from user and translate to lowerCase


def user_input():

    return input("Enter the word you are looking in dictionary or type \end to exit: ").lower()
# -- End of method

# -- gives meaning of an word


def give_meaning_word(input_word):
    close_match = get_close_matches(input_word, data.keys(), n=1, cutoff=0.8)

    keys = [key.lower() for key in data.keys()]

    if input_word in keys:
        if input_word in data:
            return data[input_word]
        elif input_word.upper() in data:
            return data[input_word.upper()]

        else:
            return data[input_word.capitalize()]

    elif len(close_match) != 0:
        ask_user = input(
            "Did you mean {} for \"yes\" y or for \"no\" press n: ".format(close_match[0]))
        if ask_user.lower() == "y":
            return data[close_match[0]]
    else:
        print("Word does not exist in dictionary please double check and try again!")


# -- end of method


# --Loading data  file (data.json)
if os.path.exists("D:/Programming/Phyton/Project1/data.json"):
    data = json.load(open("D:/Programming/Phyton/Project1/data.json"))
else:
    print("File not found")

# -- complete loading file and now have content into data

# -- asking user for an input

while True:
    input_word = user_input()
    if input_word != "\end":
        result = give_meaning_word(input_word)

        if type(result) is list:
            print("\n".join(result))
        else:
            print("Word does not exist in dictionary please double check and try again!")

    else:
        print("Program close! please visit again")
        break

# -- End of program!
