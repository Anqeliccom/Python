
class LRUCache:
    
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.key_value_mapping = {}  # отображение ключей в значения
        self.order_of_access = []  # порядок использования ключей ( от менее используемых в начале до более используемых в конце)

    def put(self, key, value):
        
        if key in self.key_value_mapping:
            # если ключ есть в кэше, обновляем порядок использования, удаляя его здесь и добавляя ниже в коде в конец order_of_access
            self.order_of_access.remove(key)
        elif len(self.order_of_access) >= self.capacity:
            # если кэш заполнен, удаляем самый давно неиспользуемый элемент (то есть самый первый)
            oldest_key = self.order_of_access.pop(0)
            del self.key_value_mapping[oldest_key]

        # добавляем новый элемент
        self.key_value_mapping[key] = value
        self.order_of_access.append(key)

    def get(self, key):
       
        if key in self.key_value_mapping:
            # если ключ есть в кэше, обновляем порядок использования и возвращаем значение
            self.order_of_access.remove(key)
            self.order_of_access.append(key)
            return self.key_value_mapping[key]
        else:
            return None
