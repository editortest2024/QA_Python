import random
start = 1
stop = 10
m = random.randrange(start, stop)
#print (m)
for i in range(1,6):
    n = input (f'Угадайте целое число, больше {start - 1} и меньше {stop}: ')
    if not n.isnumeric():
        print (f'{n} - это не число!')
        continue
    else:
        n = int(n)
    if m == n:
        print (f'Поздравляю, вы угадали с {i} попытки!')
        break
    
    if i == 5:
        print (f'К сожалению, Вы не угадали. Было задумано число {m}')
    else:
        if m < n: 
            print (f'Задаманное число меньше {n}!')
        else:
            print (f'Задаманное число больше {n}!')

