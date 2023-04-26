# This function compares two strings and determines whether they are equal or not
def equal_strings(string_one, string_two):    
    first_pass = True
    second_pass = True
    set_string_one = set(string_one) 
    set_string_two = set(string_two)
    # Return unique items from both sets. 
    unique = set_string_one.symmetric_difference(set_string_two)
    if len(unique) > 0:
        first_pass = False
    if len(string_one) != len(string_two):
        second_pass = False

    return first_pass and second_pass

print("equal_strings function:", equal_strings("cool", "love"))

# Extra Challenge!!!
# This function takes a list of values, swaps the first and last elements, and returns the updated list
def swap_values(values):
    first = values[0]
    last = values[-1]
    values[0] = last
    values[-1] = first
    return values

print("swap_values function:", swap_values([7,4,67,2]))
    