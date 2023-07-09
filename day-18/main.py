import numpy as np

def any_number(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum / len(numbers)

print("any_number function:", any_number(12, 90, 12, 34))

def add_reverse(list1, list2):
    reverse_list = []
    # Verify both lists have equal length first
    if len(list1) != len(list2):
        return "the lists are not of equal lengths. Cannot continue."
    
    # numpy library has simple addition method, but need to convert to Array type in order to use it!
    arr1 = np.array(list1)
    arr2 = np.array(list2)
    sum = np.add(arr1, arr2)
    
    # Convert back to list
    sum_list = list(sum)
    
    for i in range(len(sum_list)-1, -1, -1):
        reverse_list.append(sum_list[i])
    
    return reverse_list
        
    
print("add_reverse function", add_reverse([1,2,3], [4, 5, 6]))