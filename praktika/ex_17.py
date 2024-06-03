try:
    with open('test_2.txt', 'r',encoding='utf-8') as file:
        print(file.read)
except FileNotFoundError:
    print('ошибка')
