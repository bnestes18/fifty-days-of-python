def repeated_name(names):
    names = tuple(names)
    names_dict = {}
    max_val = 0
    repeated = ""
    for name in names:
        names_dict[name] = names.count(name)
    for key, val in names_dict.items():
        if val > max_val:
            max_val = val
            repeated = key
    return repeated

print("repeated_name function:", repeated_name(["John", "Peter", "John", "Peter", "Jones", "Peter"]))

# Extra Challenge!!!
def sorted_names(names):
    sorted = []
    # Swap each name so that Last Name appears before First Name
    for n in names:
        name_split = n.split(" ")
        name_split[0], name_split[1] = name_split[1], name_split[0]
        sorted.append(" ".join(name_split))
        sorted.sort()
    return sorted
    
print("sorted_names function:", sorted_names(["Beyonce Knowles", "Alicia Keys", "Katie Perry", "Chris Brown", "Tom Cruise"]))
