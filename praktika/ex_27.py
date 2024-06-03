import random
import string


def generate_pass():
    length = random.randint(8,32)
    upp = True
    dig = True
    spec = True


    chars = string.ascii_lowercase
    if upp:
        chars += string.ascii_uppercase
    if dig:
        chars += string.digits
    if spec:
        chars += string.punctuation
   
    passw = ''.join(random.choice(chars) for _ in range(length))
    return passw


print(generate_pass())

passw = ''.join(random.choice(chars) for _ in range(length))