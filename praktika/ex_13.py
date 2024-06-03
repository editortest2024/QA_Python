def operate(x: int, y: int, o: str):
    if (len(o)):
        if (o[0] == '+'):
            print (f'{x} {o[0]} {y} = {x+y}')
        elif (o[0] == '-'):
            print (f'{x} {o[0]} {y} = {x-y}')
        elif (o[0] == '*'):
            print (f'{x} {o[0]} {y} = {x*y}')
        elif (o[0] == '/'):
            print (f'{x} {o[0]} {y} = {x/y}')
        else:
            print (f'Неизвестная операция: {o}')
    else:
        print (f'Операция не задана!')

x = int(input('Введите первый операнд: '))
y = int(input('Введите второй операнд: '))
o = input('Введите операцию (+,-,*,/): ')
operate (x, y, o)