def all_the_same(my_iterable):
    iterable = iter(my_iterable)
    outcome = []
    first = next(iterable)
    # Any non-empty item returns True
    outcome.append(first)   
    for i in iterable:
        if i != first:
            outcome.append(False)
        else:
            outcome.append(True)
    return all(outcome)

print("all_the_same function:", all_the_same(["Mary", "mary", "Mary"]))

def read_backwards(string):
    words = string.split(" ")
    for s in range((len(words) - 1), -1, -1):
        print(words[s])
        
print("read_backwards function:", read_backwards("the love is real"))