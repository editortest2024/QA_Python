import random
while input('Введите пустую строку для броска, или любой символ для выхода:') == '':
    if random.randrange(0, 2) == 0:
        print('Орел!')
    else:
        print('Решка!')
