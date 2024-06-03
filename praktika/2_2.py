income = int(input())
credit_rating = int(input())

if income >= 5000:
    if credit_rating >=7:
        print('Кредит одобрен')
    else:
        print("рейтиг ниже 7")
else:
    print('В кредите отказано')