list1 = [1, 2, [4, 5], [6, [7]], 8]

def flatten(lst):
    newList = []

    for x in lst:
        if isinstance(x, list):
            newList.extend(flatten(x))
        else:
            newList.append(x)

    return newList

flattened_list = flatten(list1) 
print(flattened_list)
