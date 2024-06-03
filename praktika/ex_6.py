import random
a = int(input('Введите нижнуюю границу диапазона: '))
b = int(input('Введите верхнюю границу диапазона: ')) + 1
m = random.randrange(a, b)
print(f'Случайное число {m} из диапазона [{a}, {b-1}]')