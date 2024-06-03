def st_filter (sl):
    r = []
    for s in sl:
        ag = 0
        if len(s['grades']) > 0:
            ag = sum(s['grades'])/len(s['grades'])
        if (ag > 4 ):
            r.append ({s['name'], ag})
    return r

s = []
s.append({'name': 'Smith', 'grades': [ 3, 5, 4, 2, 5]})
s.append({'name': 'Bond', 'grades': [ 3, 3, 4, 2, 3]})
s.append({'name': 'Kent', 'grades': [ 3, 5, 4, 5, 5]})
s.append({'name': 'Jackson', 'grades': [ 5, 5, 4, 5, 5]})
s.append({'name': 'X', 'grades': []})

r = st_filter(s)
print(r)

