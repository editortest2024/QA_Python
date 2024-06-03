students = [
    {'name': "Ivanov", 'grades':[5,3,4,4]},
    {'name': "Petrov", 'grades':[2,2,3]},
    {'name': "Sidorov", 'grades':[4,4,4,5]},
    {'name': "Sinev", 'grades':[]}
    ]


def filter_students(st):
   
    filtred_students  = []
    for i in st:
        grades = i['grades']
        average_grade = sum(grades) / len(grades) if grades else 0
        if average_grade > 4:
            filtred_students.append(i['name'])
    return filtred_students


print(filter_students(students))


