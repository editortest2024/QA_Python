import random


def generate_random_bla(file):
    try:
        with open(file,'r',encoding='utf-8') as file:
            lines = file.readlines()


            lines = [line.strip() for line in lines if line.strip()]
            random_line = random.choice(lines)
            return random_line
    except FileNotFoundError:
        return 'файл не найден ошибка!'
   
print(generate_random_bla('example.txt'))

