

def count_set_bits(num):
    count = 0

    # Преобразуем отрицательное число в его дополнительный код
    if num < 0:
        num = (1 << 8) + num
        


    while num != 0:
        if num & 1:  # Проверка, является ли младший бит установленным
            count += 1
        num >>= 1  # Сдвиг числа вправо на 1 бит

    return count


# Пример использования
num = -123
bits_count = count_set_bits(num)
print(f"Количество выставленных битов в числе {num}: {bits_count}")