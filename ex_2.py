from datetime import datetime
current_year = datetime.now().year

_car = {
  "brand": "Ford",
  "year": 2000,
  "mileage": 100000,
  "new": 0
}

param_prompts = {
    "brand": "марка",
    "year": "год выпуска",
    "mileage": "пробег",
    "new": "новый"
}

def brand_coef (s):
    brand_weights = {
        "ford": 1,
        "pontiac": 0.9,
        "lada": 0.5,
        "bmw": 3,
        "mercedes": 3
    }
    s = str(s).lower()
    if(s in brand_weights):
        return brand_weights[s]
    else:
        return 1

def year_coef (y):
    return max(0.1,1 - 0.05*(current_year-y))

def mileage_coef(m):
    if(type(m) is int):
        return max(0.1,1 - 0.000001*m)
    else:
        return 1
    
def new_coef(n):
    if(n):
        return 1
    else:
        return 0.9
    
def set_car_price(c):
    base_price = 20000
    c["brand_coef"] = brand_coef(c["brand"])
    c["year_coef"] = year_coef(c["year"])
    c["mileage_coef"] = mileage_coef(c["mileage"])
    c["new_coef"] = new_coef(c["new"])
    c["price"] = base_price * c["brand_coef"] * c["year_coef"] * c["mileage_coef"] * c["new_coef"]

def print_car_price(c, i):
    output = '''%r. Автомобиль: марка %r (коэф. %r), год выпуска %r (коэф. %r), 
        пробег %r (коэф. %r), новый %r (коэф. %r). Оценочная стоимость %r''' % (
            i,
            c["brand"], c["brand_coef"], 
            c["year"], c["year_coef"],
            c["mileage"], c["mileage_coef"],
            c["new"], c["new_coef"],
            c["price"])
    print(output)
        
def set_car_param (car, p_name):
    if(p_name in car):
        v = input(param_prompts[p_name] + ": ")
        if type(car[p_name]) is int:
            if v.isdigit():
                car[p_name] = int(v)
        else:
            car[p_name] = str(v)

print("Калькулятор стоимости авто")
l = [] 
while True:
    print("Введите данные автомобиля")
    c = _car.copy()
    for p in c:
        set_car_param (c, p)
    set_car_price(c)
    #print(c)
    #print(def_car)
    l.append(c)
    if (input("Добавить еще одно авто? [y,n] ").lower() not in {"y", "1"}):
        break

i = 0
for a in l:
    i += 1
    print_car_price(a, i)
