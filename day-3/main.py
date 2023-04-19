# Takes in a dictionary of students and return the number of REGISTERED students
def register_check(students):
    registered = {}
    count = 0
    for key, value in students.items():
        if value == 'yes':
            registered[key] = value
            count = count + 1
    return count


print("register_check function", register_check({'Michael':'yes','John':'no','Peter':'yes','Mary':'yes'}))

# Takes a list of upper and lowercase names (list data structure) and returns only lowercase names,
# sorted in descending order (tuple data structure)
def return_lowercase(list_of_names):
    lowercase_names = []
    for name in list_of_names:
        if name.islower():
            lowercase_names.append(name)
            lowercase_names.sort(reverse=True)
    return tuple(lowercase_names)

print("return_lowercase function:", return_lowercase(["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]))
