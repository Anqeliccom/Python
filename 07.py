
list1 = [1, 2, [4, 5], [6, [7]], 8]
newList = []

def flatten(lst, depth=None, current_depth=0):
    for x in lst:
        if isinstance(x, list) and (depth is None or current_depth < depth):
            flatten(x, depth, current_depth + 1)
        else:
            newList.append(x)

flatten(list1, depth=1)
print(newList)










