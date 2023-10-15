
list1 =[1, 2, [4, 5], [6, [7]], 8]
newList =[]
def flatten(lst) :
    for x in lst:
        if isinstance(x, list):
            flatten(x)
        else:
            newList.append(x)
            
flatten(list1)
print(newList)













