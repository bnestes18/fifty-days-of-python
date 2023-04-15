import math

def divide_or_square(num):
    if num % 5 == 0:
        return math.sqrt(num)
    else:
        return math.modf(math.sqrt(num))[0]
    
print("divide_or_square function:", divide_or_square(11))

def largest_value(dict):
    keys = dict.keys()
    # Need to make 'keys' iterable
    keys_list = list(keys)
    # Assign the first item in the dictionary as the 'max.' Need to initially 
    # compare the other key values to this value 
    max_key_value = dict[keys_list[0]]
    for key in keys_list:
        if len(dict[key]) > len(max_key_value):
            max_key_value = dict[key]
        else:
            return max_key_value

    return max_key_value

print("largest_value function:", largest_value({'fruit':'apple', 'color':'green'}))