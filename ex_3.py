income = int (input("Введите сумму доходов: "))
if income >= 5000:
    print ("Размер доходов достаточный.")
    rate = int (input("Введите кредитный рейтинг: "))
    if rate < 7:
        print("Низкий кредитный рейтинг. В кредите отказано!")
    else:
        print("Рейтинг достаточный. Кредит одобрен!")
else:
    print("Доходы слишком низкие. В кредите отказано!")