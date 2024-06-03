import requests

def check_url (url: str):
    try:
        response = requests.get(url)
        status_code = response.status_code
        res = False
        msg = ""
        if status_code == 200:
            msg = 'запрос выполнен'
            res = True
        elif status_code == 404:
            msg = 'ресурс не найден'
        elif status_code == 500:
            msg = 'внутренняя ошибка сервера'
        else:
            msg = (f'код результата {status_code}')
    except Exception as e:
        res = False
        if hasattr(e, 'message'):
            msg = e.message
        else:
            msg = str(e)
    return {res, msg}

s = input("Введите url: ")
if "https://" not in s:
    s = "https://" + s
r, m = check_url(s)
if r:
    print ('Успех!')
else:
    print (f'Ошибка: {m}')
