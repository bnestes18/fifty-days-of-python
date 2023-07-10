import re

def count_words(words):
    words_array = re.split("\s", words)
    return len(words_array)

print("count_words function:", count_words("my name is brittney"))

def count_elements(string):
    clean = re.findall(r'\S', string)
    return len(clean)
    
print("count_elements function:", count_elements("my name is brittney"))