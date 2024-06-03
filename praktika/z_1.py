
def divisible (l: list, d = 3):
    r = []
    for x in l:
        try:
            if x % d == 0:
                r.append(x)
        except:
            0 
    return r
#Ex. 1
t = [10, 6, 9, 'aaa']
print (divisible(t))

