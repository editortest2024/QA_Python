def is_reverse(s1,s2):
    a = str(s2)[::-1]
    if str(s1)==a:
        return True
    else:
        return False
    
def half_anagram(s1,s2):
    a = str(s1).upper()
    b = str(s2).upper()
    for x in a:
        b = b.replace(x, "", 1)
    l = len(b)
    return l==0

def is_anagram(s1,s2):
    return half_anagram(s1,s2) and half_anagram(s2,s1) 

s = input("Напечатай приветствие Кота:")
print(len(s))
print(s[16:])
print(s.replace("Кот", "кот"))

s1 = "listen"
s2 = "netsil"
s3 = "silent"
s4 = "silention"
print("Is " + s1 + " reverse of " + s2 + "?")
print(is_reverse(s1, s2))
print("Is " + s1 + " reverse of " + s3 + "?")
print(is_reverse(s1, s3))
print("Is " + s1 + " anagram of " + s3 + "?")
print(is_anagram(s1, s3))
print("Is " + s1 + " anagram of " + s4 + "?")
print(is_anagram(s1, s4))
print("Is " + s1 + " half anagram of " + s4 + "?")
print(half_anagram(s4, s1))

a, j =  "что-нибудь", "гедеон"
k = s +" " + a + j
print(k.upper())
print(k.lower())
print(k.replace(j, " диппер"))
print(k[0])
print(k[1:5])
print(k[-1])
print(k[-5:-1])
s, a, j = 4, 5, 6
k = s + a + j
print(k)
s = "10"
print(int(s)*3+5)
print(s*3+str(5))

print(len(str(int(s)*3+5)))
print(len(s*3+str(5)))