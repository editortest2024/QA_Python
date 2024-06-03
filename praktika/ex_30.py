import random


joke_template = [
    'Почему {} катится вниз?',
    'Потому что {} смеятся над ним!',
    'Кто {} в книгах?',
    'Кто {}?',
    'Что сказал {} ему {} когда {} они {} встретились ?'
]
joke_elements = [
    'слон','заяц','бетмен','крокодил','чебурашка','студент','препод',
    'водитель','улитка'
]




def generate_joke(templates, elements):
    joke_template = random.choice(templates)
    joke = joke_template.format(*random.sample(elements,joke_template.count('{}')))
    return joke




for _ in range(5):
    joke = generate_joke(joke_template,joke_elements)
    print(joke)



