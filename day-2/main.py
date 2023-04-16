import numpy as np

# convert_add takes a list of strings, converts them into integers, and sums up each value in the list
def convert_add(list_of_strings):
    # Need to convert the list into an array to become iterable
    arr_of_strings = np.array(list_of_strings)
    # Convert to array of integers
    arr_of_ints = arr_of_strings.astype('int')
    sum = 0
    for element in arr_of_ints.flat:
        sum += element
        
    return arr_of_ints, sum
    
print(convert_add(["4", "5", "6"]))