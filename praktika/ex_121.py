def test_calc(op,n1,n2):
    try:
        if op == '+':
            return n1+n2
        elif op == '-':
            return n1-n2
        elif op == '*':
            return n1*n2
        elif op == '/':
            if n2 == 0:
                raise ValueError('Деление на 0 нельзя')
            return n1/n2
        else:
            raise ValueError('Неверная операция')
    except ValueError as e:
        return  str(e)
   
   


print(test_calc('+',5,3)) #ожидаю увидеть 8
print(test_calc('-',5,3)) #ожидаю увидеть 2
print(test_calc('*',5,3)) #ожидаю увидеть 15
print(test_calc('/',10,0)) #ожидаю увидеть обработку
print(test_calc('?',5,3)) #ожидаю увидеть обработку неверная операция




