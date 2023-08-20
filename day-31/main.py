def longest_word(words):
    max_word = ""
    max_length = 0
    for w in words:
        if len(w) > max_length:
            max_length = len(w)
            max_word = w
    return [max_length, max_word]
        
print("longest_word function:", longest_word(["Java", "JavaScript", "Python"]))

# Extra Challenge!!!
def create_user():
    user = {}
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    password = input("Please enter your password: ")
    user["name"] = name
    user["age"] = age
    user["password"] = password
    print("User saved. Please login.\n")
    print(user)
    
    name_reenter = ""
    password_reenter = ""
    while (name_reenter != user["name"]) or (password_reenter != user["password"]):
        name_reenter = input("Enter your full name: ")
        password_reenter = input("Enter your password: ")
        
        if (name_reenter == user["name"]) and (password_reenter == user["password"]):
            return "Logged in successfully!"
        else:
            print("Wrong password or username. Please try again!")
    
print("create_user function", create_user())