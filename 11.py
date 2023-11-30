class Counter:
    def __init__(self, initial_count=0, step=1):
        self.count = initial_count
        self.step = step

    def increment(self):
        self.count += self.step
        
class Singleton: 
    _instances = {} # словарик: ключи - названия классов, значения - названия экземпляров

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances: # если экземпляр класса еще не создан
            instance = super().__new__(cls) # создаем его с помощью метода __new__
            cls._instances[cls] = instance # pаписываем созданный экземпляр в словарь _instances с ключом, равным текущему классу
            return instance # возвращаем созданный экземпляр класса
        else:
            return cls._instances[cls]

class GlobalCounter(Singleton, Counter):
    pass

gc1 = GlobalCounter()
gc2 = GlobalCounter()

assert id(gc1) == id(gc2) # True

