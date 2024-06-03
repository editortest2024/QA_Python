#Ex. 4
s = input('Введите строку: ')
if not s:
    s = 'Quick brown fox.'
w = input('Введите искомое слово: ')
if w.lower() in s.lower():
    print (f'Слово "{w}" в строке "{s}" есть!')
else:
    print (f'Слова "{w}" в строке "{s}" нет!')


