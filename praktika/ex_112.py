def summa (first,second):
    return first + second
 
def sub (first,second):
    return first - second
    
def mult (first,second):
    return first * second
 
def div (first,second): 
    return first / second
    
x = int (input("Введите первое число: "))
y = int (input("Введите второе число: "))
o = input('Введите операцию (+,-,*,/): ')
 
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