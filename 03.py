a = "1 2 | 3 4"

result_array = [[float(value) for value in element.split()] for element in a.split(" | ")]

print(result_array[0][1])
