import random

questions = [{'question':"Сто одежек и все без застежек?", 'answer': 'Капуста'},
             {'question':"Два кольца, два конца, посередине гвоздик?", 'answer': 'Ножницы'},
             {'question':"По горам, по долам, ходят шуба да кафтан?", 'answer': 'Баран'}]

def run_quiz():
    score = 0

    random.shuffle(questions)

    n = 1
    for i in questions:
        print(f"Вопрос {n}: {i['question']}")

        user_answer = input("Ваш ответ: ")

        if user_answer.lower() == i['answer'].lower():
            print("Правильно!")
            score += 1
        else:
            print("Неправильно!")
        n = n + 1

    print(f"Вы набрали {score} из {len(questions)} баллов.")

run_quiz()