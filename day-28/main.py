from itertools import chain
from itertools import permutations

def index_position(string):
    indices = []
    for s in range(0, len(string)):
        if string[s].islower():
            indices.append(s)
    return indices
        
print("index_position function:", index_position("LovE"))

# Extra Challenge!!!
def largest_number(numbers):
    # Return all possible combinations as a list of tuples
    list_combinations = list(set(permutations(numbers)))
    big_list = []
    for combo in list_combinations:
        l = list(combo)             # Convert each tuple to a list
        s = map(str, l)             # Convert integers to strings because they need to be joined
        a = ''.join(s)              # Join the string characters
        print(a)
        big_list.append(a)
    big_tuple = tuple(big_list)
    return max(big_tuple)           # This function returns 9876732, but the answer says '9877632' instead. 
                                    # I think my answer is right!
            
print("largest_number function:", largest_number([3, 67, 87, 9, 2]))



