import re
text = "GodOfSuffering"
x = re.sub(r"(\w)([A-Z])", r"\1 \2", text)
print(x)