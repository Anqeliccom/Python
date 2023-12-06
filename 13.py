def coroutine(func):
    def wrap(*args, **kwargs):
        coroutine_instance = func(*args, **kwargs) # создаем экземпляр корутины
        next(coroutine_instance) # готовимся к получению значения через yield
        return coroutine_instance
    return wrap

@coroutine
def storage():
    values = set()
    was_there = False

    while True:
        val = yield was_there
        was_there = val in values # True, если val уже есть в множестве и False в обратном
        if not was_there:
            values.add(val)

st = storage()
print(st.send(42))  # False
print(st.send(42))  # True


# когда первый раз вызвали send yield возвращает False, так как корутина только что была создана и еще не получала значений
# was_there все еще False, так как еще не добавляли значение в values
# добавляем значение в values
# вызываем второй раз send и yield сразу возвращает True