import re


def valid_num(num):


    phone_pattern = r'^\+\d{11}$'


    if re.match(phone_pattern, num):
        return True
    else:
        return False
   
print(valid_num('+79956247294'))
print(valid_num('79956247294'))
print(valid_num('+7995624'))
print(valid_num('+asdjsadhsua'))



 
  
 
 



