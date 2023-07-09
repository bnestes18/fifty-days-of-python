import random
def user_name():
    name = input("Enter in your first name: ")
    randInt = random.randint(0,9)
    reverse = []
    for l in range(len(name)-1,-1,-1):
        reverse.append(name[l])
    return "".join(reverse) + str(randInt)
        
# print("user_name() function:", user_name())
        
# def sort_length(names):
#     for i in range(1, len(names)):
#             max = names[i]
#             j = i - 1
#             while j >= 0 and max < names[j]:
#                 names[j + 1] = names[j] 
#                 j -= 1 
#             names[j + 1] = max
#     return names

def selectionSort(array, size):
     
    for s in range(size):
        min_idx = s
         
        for i in range(s + 1, size):
             
            # For sorting in descending order
            # for minimum element in each loop
            if len(array[i]) < len(array[min_idx]):
                min_idx = i
 
        # Arranging min at the correct position
        (array[s], array[min_idx]) = (array[min_idx], array[s])
        return array
 
# Driver code
data = ["Peter", "Jon", "Andrew", "A"]
size = len(data)
print(selectionSort(data, size))
    
# print("sort_length() function:", sort_length(["Peter", "Jon", "Andrew", "A"]))
