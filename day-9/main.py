# This function takes a string of numbers (both odd and even), and returns the biggest odd number.
def biggest_odd(string_of_nums):
    odds = []
    for string in string_of_nums:
        integer = int(string)
        if integer % 2 != 0:
            odds.append(integer)
    odds.sort(reverse=True)
    return odds[0]

print("biggest_odd function", biggest_odd("23569"))

# Extra Challenge
# If a list has zeros, it this function will move them to the end of the list and maintain the order of the other
# numbers in the list. If there are no zeros in the list, the function should return the original list sorted in 
# ascending order.
def zeros_last(nums_list):
    zeros = []
    for num in nums_list:
        if 0 not in nums_list:
            nums_list.sort()
        else:
            if num == 0:
                nums_list.remove(num)
                zeros.append(num)
    nums_list.extend(zeros)
    return nums_list

print("zeros_last function", zeros_last([2,1,4,7,6]))
