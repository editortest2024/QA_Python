import re


user_database = {
    "user1@example.com": {'name':'User', 'password': 'Qwe12343r'},
    "user2@example.com": {'name':'Vasya', 'password': 'Qwe12343r'},
    "user3@example.com": {'name':'Petya', 'password': 'Qwe12343r'},
    "user4@example.com": {'name':'Sereja', 'password': 'Qwe12343r'},
}






def reg_user():
    while True:
        name = input('Введите имя:')
        email = input('Введите почту: ')
        password = input('Введите пароль: ')




        #проверка корректности имени
        if not re.match(r'[a-zA-Z-]',name):
            print('Недопустимое имя')
            continue


        if len(name) <2:
            print('короткий имя')
            continue


        if not re.match(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            print('Недопустимая почта!')
            continue
        if len(password) < 8:
            print('Пароль короткий')
            continue
        if not any(char.isupper() for char in password):
            print('Введите заглавную букву')
            continue
        if not any(char.islower() for char in password):
            print('Введите строчную букву')
            continue
        if not any(char.isdigit() for char in password):
            print('Введите цифру')
            continue
        if not any(char in '!@#$%^&*()-_=+[{]};;\",<>/>`~' for char in password):
            print('В пароле нет символа')
            continue
        if email in user_database:
            print('Существует')
            continue


        user_database[email] = {'name': name, 'password': password}


        print('Новый пользователь создан')
        view_database = input('смотрим базу? y/n')
        if view_database.lower() == 'y':
            print(user_database)
            break
reg_user()




