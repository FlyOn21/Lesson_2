
def open_lib(id = 2105):
    with open('cities_lib.txt', 'r', encoding='utf-8') as lib:
        lib_file = [citi.strip('\n') for citi in lib]
        lib.close()
        dict_cities_lib = {}
        dict_cities_lib[id] = lib_file
        lib_city_1 = dict_cities_lib[id]
        lib_city = [lib_citys.title() for lib_citys in lib_city_1 ]
        # print(lib_city)
        return lib_city
m = open_lib()

def func_cities_move(counter = 10, lib_city = m,cities_out = []):
    print(cities_out)
    cities = (input('Твой город: ')).title()
    if cities == 'Я сдаюсь':
        print('Жаль, ну ладно получиться в следующйи раз')
        return
    if cities in lib_city :
        last_letter = (cities[-1]).upper()
        print(f'Такой город {cities}, мне на {last_letter}')
        del_index = lib_city.index(cities)
        cities_out.append(cities)
        del(lib_city[del_index])
        print(lib_city)
        for one_city in lib_city:
            if one_city[0]== last_letter:
                one_city_letter = one_city[-1]
                if one_city_letter == 'ы' or one_city_letter == 'й' or one_city_letter == 'ь' or one_city_letter == 'ъ':
                    one_city_letter = one_city[len(one_city) - 2]
                print(f'Мой город {one_city}, тебе на {one_city_letter.upper()}')
                del_index_2 = lib_city.index(one_city)
                cities_out.append(one_city)
                del (lib_city[del_index_2])
                # print(lib_city)
                func_cities_move(counter)
            elif one_city[0]!= last_letter:
                continue
            else:
                print('Ты крут,я проиграл')
                break
    else:
        if counter == 1:
            print('Увы ты проиграл')
        else:
            if cities in cities_out:
                counter = counter - 1
                print(f'Такой город уже был, у тебя осталось {counter} попыток ')
                func_cities_move(counter=counter)
            else:
                counter = counter - 1
                print(f'Поробуй еще у тебя {counter} попыток')
                func_cities_move (counter = counter)

c = func_cities_move()
