def check_unique (l):
    return len(l) == len(set(l))

l1 = [0,1,3,5,7]
print(l1, check_unique (l1))
l2 = [0,1,3,5,7, 'aaa', 'aaa']
print(l2, check_unique (l2))