def same_in_reverse(string):
    reverse = []
    for i in range(len(string)-1, -1, -1):
        reverse.append(string[i])
    reverse_str = ''.join(reverse)
    return string == reverse_str


print("same_in_reverse function:", same_in_reverse("dad"))

def your_age():
    names_age = {"jane":23, "kerry":45, "tim":34, "peter":27}
    name = input("What is your name? ")
    output = "Hi {}, you are {} years old."
    if name.lower() in names_age:
        return output.format(name, names_age[name.lower()])
    else:
        new_name = name
        new_age = input("Your name was NOT found in the database. Please enter your age and the database will be updated: ")
        return output.format(new_name, new_age)
   
print("your_age function:", your_age())