"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
school_class = [{'school_class': '4a', 'scores': [3,4,4,5,2]},{'school_class': '4b', 'scores': [2,2,5,4,3]},{'school_class': '4c', 'scores': [4,4,5,4,5]}]
def main(school_class):

    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    all_school = []
    for class_ball in school_class:
        middle_ball = sum(class_ball['scores'])/len(class_ball['scores'])
        print('Class {},middle ball {}'.format(class_ball['school_class'], middle_ball) )
        for ball in class_ball['scores']:
            all_school.append(ball)
    print(f'Middle ball school: {round((sum(all_school)/len(all_school)),2)}')

if __name__ == "__main__":
    main(school_class)
