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
    if (input("Чтобы добавить контакт введите любой символ и нажмите [Enter]. Для вывода списка контактов просто нажмите [Enter]: ") != ''):
        add_contact()
    else:
        for i in pb:
            print (f'Имя: {i['name']}, телефон: {i['phone']}')
        break