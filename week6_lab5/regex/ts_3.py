import re
def find():
    patterns = "^[a-z]+_[a-z]+$"
    text = input()
    if re.search(patterns, text):
        print("T")
    else:
        print("F")
find()

