import numpy as np
def sum_list(nested):
    flatten = np.hstack(nested)
    return np.sum(flatten)

print("sum_list() function:", sum_list([[2,4,5,6],[2,3,5,6]]))

def unpack(nested):
    flatten = np.hstack(nested)
    indices = [1,3,6]
    return np.take(flatten, indices)

print("unpack() function:", unpack([[12,34,56,67],[34,68,78]]))