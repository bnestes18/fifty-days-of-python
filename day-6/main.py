# This function takes a user provided email as input and returns only the username as the output.
def user_name(email):
    # Validate email first. Does email have an @ symbol?
    if '@' not in email:
        return email + ' is not a valid email. Please provide a user principal address to continue.'
    else:
        at_symbol_position = email.find("@")
        username = email[:at_symbol_position]
        return username

print("user_name function:", user_name('someuser@test.com'))

# Extra Challenge!!!
# This function takes a list of numbers provided by the user, replaces the first and last digits with zeros
# and returns the updated list
def zeroed(list_of_nums):
    if list_of_nums[0] != 0 and list_of_nums != 0:
        list_of_nums[0] = 0
        list_of_nums[-1] = 0
    return list_of_nums

print("zeroed function:", zeroed([2,5,7,8,9]))