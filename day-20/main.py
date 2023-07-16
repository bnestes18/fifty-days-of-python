import re

def capitalize(string):
    words = string.split(" ")
    caps = []
    for s in words:
        capitalize = s.capitalize()
        caps.append(capitalize)
    return caps

print("capitalize function:", capitalize("this is a test"))

    
def reverse_list(string):
    regex = re.compile(r"[A-Z]+")
    uppers = []
    reverse = []
    string_list = string.split(" ")
    for s in string_list:
        # remove newline characters in multiline strings
        s = s.rstrip('\n')
        if regex.search(s):
            uppers.append(s)
    for u in uppers:
        reverse.append(u[::-1])
    return reverse  
    
multi_line = """leArning is hard bUt if You appLy youRself
                you can acheiVe success"""
print("reverse_list function:", reverse_list(multi_line))
