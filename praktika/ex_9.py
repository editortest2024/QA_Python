import random
m = random.randrange(0, 8)
print(f'Монета №{m} - фальшивая')
x = []
for i in range(8):
    if i == m:
        x.append(1)
    else:
        x.append(2)
print (m, x)
d1, d3 = 0, 8
i = 0
while True:
    d2 = int((d3 - d1)/2)
    if not d2:
        break
    i = i + 1    
    print(i, d1, d2, d3)
    print ( x[d1:d1+d2], sum([n for n in x[d1:d1+d2]]), x[d1+d2:d3], sum([n for n in x[d1+d2:d3]]))
    if sum([n for n in x[d1:d1+d2]]) > sum([n for n in x[d1+d2:d3]]):
        d1 = d1 + d2
    else:
        d3 = d1 + d2
    

print(f'Фальшивая монета №{d1} найдена за {i} взвешивания!')
    



