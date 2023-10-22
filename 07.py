list1 = [1, 2, [4, 5], [6, [7]], 8]

def flatten(lst, depth=None, current_depth=0):
    newList = []
    for x in lst:
        if isinstance(x, list) and (depth is None or current_depth < depth):
            newList.extend(flatten(x, depth, current_depth + 1))
        else:
            newList.append(x)
    return newList

flattened_list = flatten(list1, depth=1)
print(flattened_list)


