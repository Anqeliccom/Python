class Counter:
    _instance_count = 0

    def increment_instance_count(cls):
        cls._instance_count += 1

    def get_instance_count(cls):
        return cls._instance_count

    increment_instance_count = classmethod(increment_instance_count)
    get_instance_count = classmethod(get_instance_count)

class Singleton(Counter): 
    _instances = {} # словарик: ключи - названия классов, значения - названия экземпляров

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls) # переопределяем метод __new__ для базового класса
            cls._instances[cls] = instance
            cls.increment_instance_count()
            return instance
        else:
            return cls._instances[cls]

class GlobalCounter(Singleton, Counter):
    pass

gc1 = GlobalCounter()
gc2 = GlobalCounter()

print(id(gc1) == id(gc2))  # True
print(GlobalCounter.get_instance_count())
