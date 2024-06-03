def  validate_text_length (text):
    if len(text) > 15 or num[0] != "+":
        return False
   
    for i in num[1:]:
        if not i.isdigit():
            return False
    return True


txt = input()
 
 



