import re
txt = 'Woman is very strong, and very smart and very attractive.'
x = re.sub("[ ,.]" , ":", txt)
print(x)
