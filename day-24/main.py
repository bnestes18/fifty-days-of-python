import numpy as np

def average_calories():
    calories = []
    sum = 0
    while True: 
        amount = input("Enter calories: ")
        if amount != "done":
            calories.append(amount)
        else:
            break
    for cal in calories:
        sum += int(cal)
    return sum / len(calories)
    
print("average_calories function:", average_calories())

def nested_lists(*lists):
    return np.array(lists, ndmin=2)
    
print("nested_lists function:", nested_lists([1,2,3,5],[1,2,3,4],[1,3,4,5]))
    


    