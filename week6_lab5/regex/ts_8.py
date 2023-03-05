import re

text = "GodOfSuffering"
print(re.findall('[A-Z][^A-Z]*', text))