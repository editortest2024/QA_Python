#Ex. 3
def operate(x: int, y: int, o: str):
    if (len(o)):
        if (o[0] == '+'):
            print (f'{x} {o[0]} {y} = {x+y}')
        elif (o[0] == '-'):
            print (f'{x} {o[0]} {y} = {x-y}')
        elif (o[0] == '*'):
            print (f'{x} {o[0]} {y} = {x*y}')
        elif (o[0] == '/'):
            try:
                print (f'{x} {o[0]} {y} = {x/y}')
            except:
                print ('(Ошибка: деление на 0!')
        else:
            print (f'Неизвестная операция: {o}')
    else:
        print (f'Операция не задана!')

try:
    x = int(input('Введите первый операнд: '))
    y = int(input('Введите второй операнд: '))
except:
    0
o = input('Введите операцию (+,-,*,/): ')
operate (x, y, o)