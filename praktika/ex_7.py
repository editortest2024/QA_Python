import random
while True:
    i = input('Введите пробел, если хотите бросить кость:')
    if i == ' ':
        print(f'Выпало {random.randrange(1, 7)}')  
    else:
        break