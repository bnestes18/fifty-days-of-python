import re

def add_hash(string):
    regex = "\s"
    return re.sub(regex, "#", string)

def add_underscore(string):
    regex = "\W"
    return re.sub(regex, "_", string)

def remove_underscore(string):
    regex = "[_]"
    return re.sub(regex, " ", string)

print(remove_underscore(add_underscore(add_hash("Python"))))
