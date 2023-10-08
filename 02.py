newList = []
a = [1, 2, 3]
b = ["a", "b"]

def f(a, b):
        e = min(len(a), len(b))
        for i in range(e):
            newList.append((a[i],b[i]))

f(a, b)
print(newList)