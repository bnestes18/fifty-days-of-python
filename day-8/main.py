# This function determines the maximum even digit and minimum odd digit and subtracts the two.
def odd_even(list_of_nums):
    odds_list = []
    evens_list = []
    for num in list_of_nums:
        if num % 2 == 0:
            evens_list.append(num)
        else:
            odds_list.append(num)
            
    evens_list.sort()
    odds_list.sort(reverse=True)
    
    max_even = evens_list[-1]
    min_odd = odds_list[-1]
    difference = max_even - min_odd

    text = "{} - {} = {}"
    
    return text.format(max_even, min_odd, difference)

print("odd_even function", odd_even([1,2,4,6]))


# List of Prime Numbers
# Could not figure this one out on my own!!!! Grrrr!!!
def prime_numbers(integer):
    primes = []
    
            
print("prime_numbers function:", prime_numbers(10))