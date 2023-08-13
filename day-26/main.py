def sort_words(string):
    dictionary = {}
    reversed_no_dupes = []
    no_spaces = string.replace(" ", "")
    print(no_spaces)
    for c in range(len(no_spaces) - 1, -1, -1):
        dictionary[no_spaces[c]] = ""
    
    for k in dictionary.keys():
        reversed_no_dupes.append(k)
    return reversed_no_dupes
    
print("sort_words function:", sort_words("love life"))

def string_length(words):
    words_dict = {}
    words = words.split(" ")
    for w in words:
        words_dict[w] = len(w)
    return words_dict
    
print("string_length function:", string_length("Hi my name is Richard"))