def divisible (l: list, d = 3):
    r = []
    for x in l:
        try:
            if x % d == 0:
                r.append(x)
        except:
            0 
    return r
#Ex. 1
t = [10, 6, 9, 'aaa']
print (divisible(t))

#Ex. 2
#import phonenumbers
#from phonenumbers import carrier
#from phonenumbers.phonenumberutil import number_type

pb = []
def add_contact():
    c = input('Contact name: ')
    if (len(c) < 3):
        print ("Too short name!")
        return
    n = input('Phone number: ')
    #if (!carrier._is_mobile(number_type(phonenumbers.parse(n)))
    #    print ("Incorrect phone number!")
    #    return
    for x in pb:
        if x['name'] == c:
            x['phone'] == n
            return
    pb.append({'name': c, 'phone': n})

while (True):
    if (input("Добавить контакт?") != ''):
        add_contact()
    else:
        for i in pb:
            print (f'Имя: {i['name']}, телефон: {i['phone']}')
        break

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
            print (f'{x} {o[0]} {y} = {x/y}')
        else:
            print (f'Неизвестная операция: {o}')
    else:
        print (f'Операция не задана!')

x = int(input('Введите первый операнд: '))
y = int(input('Введите второй операнд: '))
o = input('Введите операцию (+,-,*,/): ')
operate (x, y, o)

#Ex. 4
s = input('Введите строку: ')
if not s:
    s = 'Quick brown fox.'
w = input('Введите искомое слово: ')
if w.lower() in s.lower():
    print (f'Слово "{w}" в строке "{s}" есть!')
else:
    print (f'Слова "{w}" в строке "{s}" нет!')