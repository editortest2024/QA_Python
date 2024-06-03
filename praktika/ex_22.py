import re
from email.utils import parseaddr

def check_mail_addr (addr: str):
    email_regex = re.compile((r"(^[a-zA-Z0-9_.+-]{6,}+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}+$)"))
    return email_regex.fullmatch(addr) is not None 

address = "user01@example.com"
parsed_email = parseaddr(address)[1] 
print(parsed_email, check_mail_addr(parsed_email))

#print(is_valid is not None and parsed_email == address)  # Возвращает True, если адрес полностью соответствует шаблону