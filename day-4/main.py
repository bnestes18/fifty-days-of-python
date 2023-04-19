# This function takes 2 numbers and returns the number of floats between the two 
def only_floats(a, b):
    nums_list = [a, b]
    count = 0
    for num in nums_list:
        if type(num) == float:
            count += 1
    return count

print("only_floats function:", only_floats(1.0, 2.0))

# Extra Challenge!!!
# This function returns the index of the longest word in the list
def word_index(list):
    longest_word_index = 0
    position = 0
    while(position <= len(list) - 1):
        if len(list[position]) > len(list[longest_word_index]):
            longest_word_index = position
        position += 1
    return longest_word_index

print("word_index function", word_index(["Hate","remorse","vengeance"]))
print("word_index function", word_index(["Loves", "Cools"]))