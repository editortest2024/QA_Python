def check_password(password):
    if (len(password)) <8:
        return False
    
    has_low = False
    has_up = False
    has_dig = False


    for i in password:
        if i.islower():
            has_low = True
        elif i.isupper():
            has_up = True
        elif i.isdigit():
            has_dig = True
   
    return has_low and has_up and has_dig
print(check_password('Abcd1234')) #True
print(check_password('qwerty')) #False
print(check_password('abcD')) #False
print(check_password('ABCD1234')) #False


