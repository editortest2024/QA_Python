month = input("январь,февраль,март,апрель,май,июнь,июль,август,сентябрь,октябрь:")
if month.isdigit():
    month = int(month)
else:
    month = month.lower()
if month in {"январь","февраль","декабрь", 1, 2, 12}:
    print("зима")
elif month in {"март","апрель","май", 3, 4, 5}:
    print("весна")
elif month in {"июнь","июль","август", 6, 7, 8}:
    print("лето")
elif month in {"сентябрь","октябрь","ноябрь", 9, 10, 11}:
    print("осень")
else:
    print("Месяц не определен")