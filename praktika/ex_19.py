def count_letters(s: str):
    d = []
    for l in s:
        if l in d:
            d [l] = d[l] + 1
        else:
            d [l] = 1
    return d
    
s = input ('Введите строку: ')
print(count_letters(s))