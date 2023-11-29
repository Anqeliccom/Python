def cycle(iterable):
    while True:
        for i in iterable:
            yield i

def take(iterable, n):
    res = []
    for i in range(n):
        res.append(next(iterable))
    return res
    
def chain(*iterables):
    for iterable in iterables:
        for i in iterable:
            yield i

print(take(cycle([1, 2, 3]), 10))

my_list = [42, 13, 7]
print(list(chain([1, 2, 3], ['a', 'b'], my_list)))