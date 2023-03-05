import re
def find():
    patterns = "^[A-Z]+[a-z]+$"
    text = input()
    if re.search(patterns, text):
        print("T")
    else:
        print("F")
find()

