try:
    x = int (input("Введите первое число"))
    y = int (input("Введите второе число"))
    try:    
        a = x / y
    except:
        print('Ошибка! Деление на 0') 
except:    
    print('Введено не число') 
