def unique_numbers(numbers):
    unique = []
    for n in numbers:
        if n not in unique:
            unique.append(n)
    result = sum(numbers) - sum(unique)
    if result % 2 == 0:
        return numbers
    else:
        return unique

print("unique_numbers function", unique_numbers([1,2,4,5,6,7,8,8]))

# Extra Challenge!!!

# newlist = [expression for item in iterable if condition == True]
    
def difference(a, b):
    diff_a = [num for num in a if num not in b]
    diff_b = [num for num in b if num not in a]
    # Concatenate the lists
    diff = diff_a + (diff_b)
    
    print(diff)
    
print("difference function", difference([1,2,4,5,6], [1,2,5,7,9]))