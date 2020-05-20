"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    lib_question ={"Как дела": "Хорошо!", "Что делаешь?": "Программирую",'Что кушаеш?':'Шоколадку', 'На работу хочеш':'Нет','Ты мне надоел':'Пока'}
    while True:
        question = input('Что хотел?\n - ')
        if question.capitalize() in lib_question.keys():
            print(lib_question[question.capitalize()])
            if lib_question[question.capitalize()] =='Пока':
                break
        else:
            print('Я не знаю')


    
if __name__ == "__main__":
    ask_user()