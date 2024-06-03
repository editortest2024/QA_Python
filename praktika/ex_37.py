def pas_val(pw):
    if len(pw) < 8:
        return False
    h_d = any(char.isdigit() for char in pw)


    h_l = any(char.isalpha() for char in pw)


    h_plus  = pw.startswith('+') or pw.endswith('+')


    return h_d and h_l and h_plus


print(pas_val('+Password13'))
print(pas_val('Password13+'))
print(pas_val('Password13'))
print(pas_val('+asdasdasada'))
print(pas_val('+12312321321'))

