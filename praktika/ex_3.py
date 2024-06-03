import random


attemts = 5
secret_number = random.randint(1,100)
while attemts > 0:
    guess = int(input("Введи число:"))


    if guess == secret_number:
        print('Win')
        break
    elif guess>secret_number:
        print('Число больше')
    else:
        print('Число меньше')


    attemts-=1
    print(f'You have {attemts} attempts left')


    if attemts == 0:
        print('Game Over')
5