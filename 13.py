def coroutine(func):
    def wrap(*args, **kwargs):
        coroutine_instance = func(*args, **kwargs)
        next(coroutine_instance)
        return coroutine_instance
    return wrap

@coroutine
def storage():
    values = set()
    was_there = False

    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)

st = storage()
print(st.send(42))  # False
print(st.send(42))  # True
