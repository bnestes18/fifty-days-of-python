def string_range(range_num):
    current_num = 0
    string = ""
    if range_num == 0:
        return "Cannot return a range of 0. Please provide a non-zero number."
    else:
        while (current_num < range_num):
            string += str(current_num)
            current_num += 1
        formatted = '.'.join(string)
        return formatted

print("string_range function:", string_range(6))

# Extra Challenge!!! - Dictionary of Names
# This function takes a list of names, iterates through the list and extracts only the s names. 
# This function also counts the number of occurrences of each s name
def count_s_names(list_of_names):
    s_names = {}
    i = 0
    for name in list_of_names:
        if name.startswith("S"):
            s_names.update({name: 0})
    while (i < len(list_of_names)):
        # Get's the key's value if the key (name) exists in the dictionary, otherwise, 'None' type is returned
        current_name_value = s_names.get(list_of_names[i])
        # If the key's (or name) value is not equal to None, that means that the key (or name) DOES exist and 
        # we want to increment the key's (or name's) count if the name is found in the list.
        if current_name_value != None:
            current_name_value += 1
            s_names.update({list_of_names[i]: current_name_value})
        i += 1
    return s_names

print("count_s_names function:", count_s_names(["Joseph", "Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]))