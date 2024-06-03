students = [
    {'name': "Alice", 'grades':[5,3,4,4]},
    {'name': "Bill", 'grades':[2,2,3]},
    {'name': "Bob", 'grades':[4,4,4,5]},
    {'name': "David", 'grades':[]}
    ]


def filter_students(st):
    #создал пустой список который будет использоваться для хранения студентов с баллом выше 4
    filtred_students  = []


    #начало цикла for который будет перебирать каждый элемент(каждого студента) из списка students
    for i in st:
        #извлекаю список оценок текущего студента(i) - это словарь, и обращение i['grades'] позволяет мне обратится по ключу grades
        grades = i['grades']
        #считаю средний балл для текущего студента
        if grades:
            average_grade = sum(grades) / len(grades)
        else:
            average_grade = 0
           
        if average_grade > 4:
            filtred_students.append(i['name'])
    return filtred_students


print(filter_students(students))




