from random import shuffle

x = [input('Введите элемент: ') for i in range(5)]
print ("Исходный порядок: ")
print(x)
shuffle(x)
print ("Порядок после перемешивания: ")
print(x)