def make_tuples(l1, l2):
    tuples_list = []
    if len(l1) != len(l2):
        return "The provided lists do not have equal lengths. Will not continue."
    i = 0
    while(i <= len(l1) - 1 and i <= len(l2) - 1):
        new_tuple = (l1[i],)
        new_tuple += (l2[i],)
        tuples_list.append(new_tuple)
        i += 1
    print(tuples_list)
print("make_tuples function:", make_tuples([1,2,3,4],[5,6,7,8]))

def even_or_average(*numbers):
    max_num = numbers[0]
    evens = []
    sum = 0
    if len(numbers) < 5:
        raise Exception("Please provide at least 5 numbers in order to continue.")
    
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    
    if len(evens) == 0:
        for n in numbers:
            sum += n
        return sum / len(numbers)
    else:
        for even in evens:
            if even > max_num:
                max_num = even
        return max_num


print("even_or_average function:", even_or_average(1,7,3,9,5))
    