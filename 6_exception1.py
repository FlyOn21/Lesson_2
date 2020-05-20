"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    lib_question = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую", 'Что кушаеш?': 'Шоколадку',
                    'На работу хочеш': 'Нет', 'Ты мне надоел': 'Пока'}
    try:
        while True:
            question = input('Что хотел?\n - ')
            if question.capitalize() in lib_question.keys():
                print(lib_question[question.capitalize()])
            else:
                print('Я не знаю')
    except KeyboardInterrupt:
        print('Пока')
    
if __name__ == "__main__":
    ask_user()
