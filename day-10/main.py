# This function takes user input (password) and returns a hidden password with text that returns the hidden
# password and password length
def hide_password():
    password = input("Enter in a secure password: ")
    hidden = ""
    for x in password:
        x = "*"
        hidden += x
    text = "The password {} is {} characters long."
    return text.format(hidden, len(hidden))

print("hide_password function:", hide_password())

# Extra Challenge!!!
# This function converts each of the numbers in the list, into a string. Each string will include commas
# in the thousandths place. Example, 1000000 -> 1,000,000
def convert_numbers(list_of_ints):
    string_nums = []
    # Thousand Separator formatting time
    thousand_separator = "{:,}"
    # For each int, apply thousand separator, and convert the int into a string. Then append the string to string_nums.
    for integer in list_of_ints:
        formatted = thousand_separator.format(integer)
        string_nums.append(str(formatted))
    return string_nums

print("convert_numbers function:", convert_numbers([1000000,2356989,2354672,9878098]))