import unittest


def zapis(marka_1, model_1, tip_1, tip_d_1, county_1, gosn_1, colour_1, doors_1):
    cars = []
    add_car = []
    print("Добавьте марку машины:")
    marka = marka_1
    add_car.append(marka)
    print("Добавьте модель машины:")
    model = model_1
    add_car.append(model)
    print("Добавьте тип машины:")
    tip = tip_1
    add_car.append(tip)
    print("Добавьте тип двигателя машины:")
    tip_d = tip_d_1
    add_car.append(tip_d)
    print("Добавьте страну производителя машины:")
    county = county_1
    add_car.append(county)
    print("Добавьте госномер авто")
    gosn = gosn_1
    add_car.append(gosn)
    print("Введите цвет машины")
    colour = colour_1
    add_car.append(colour)
    print("Введите кол-во дверей")
    doors = doors_1
    add_car.append(doors)
    cars.append(add_car)
    return cars


def zamena_xarki(cars, search_1, vvod, strzamena):
    cars_vivod = []
    for i in range(len(cars)):
        cars_vivod.append(cars[i])
    for q in range(len(cars_vivod)):
        cars_vivod[q] = [q + 1] + cars_vivod[q]
    carszam = []
    search = search_1
    for c in range(len(cars_vivod)):
        if search == cars_vivod[c][0]:
            carszam = cars[c]
    if search > len(cars_vivod):
        print("Вы ввели не существующее значение, повторите попытку")
        return 0

    if vvod == 1:
        print("Вы меняете марку, напишите марку:")
        carszam[0] = strzamena
        print("Вы успешно изменили хар-ку")
    elif vvod == 2:
        print("Вы меняете модель, напишите модель:")
        carszam[vvod - 1] = strzamena
        print("Вы успешно изменили хар-ку")
    elif vvod == 3:
        print("Вы меняете тип машины, напишите тип машины:")
        carszam[vvod - 1] = strzamena
        print("Вы успешно изменили хар-ку")
    elif vvod == 4:
        print("Вы меняете тип двигателя, напишите тип двигателя:")
        carszam[vvod - 1] = strzamena
        print("Вы успешно изменили хар-ку")
    elif vvod == 5:
        print("Вы меняете страну производителя, напишите страну производителя:")
        carszam[vvod - 1] = strzamena
        print("Вы успешно изменили хар-ку")
    elif vvod == 6:
        print("Вы меняете госномер авто, напишите госномер авто:")
        carszam[vvod - 1] = strzamena
        print("Вы успешно изменили хар-ку")
    elif vvod == 7:
        print("Вы меняете цвет машины, напишите цвет машины:")
        carszam[vvod - 1] = strzamena
        print("Вы успешно изменили хар-ку")
    elif vvod == 8:
        print("Вы меняете кол-во дверей, напишите кол-во дверей:")
        carszam[vvod - 1] = strzamena
        print("Вы успешно изменили хар-ку")
    else:
        print("Вы ввели неправильное значение, повторите попытку")
        return 0
    return cars


def ydalenie_xarki(cars, search_1, vvod):
    cars_vivod = []
    for i in range(len(cars)):
        cars_vivod.append(cars[i])
    for q in range(len(cars_vivod)):
        cars_vivod[q] = [q + 1] + cars_vivod[q]
    cardelete = []

    print("Напишите номер скроки машины, которую Вы хотели бы удалить:")
    search = search_1
    for c in range(len(cars_vivod)):
        if search == cars_vivod[c][0]:
            cardelete = cars[c]
    if search > len(cars_vivod):
        print("Вы ввели не существующее значение, повторите попытку")
        return 0
    print("Выберите, что хотите удалить:")
    print("1 - Марка")
    print("2 - Модель")
    print("3 - Тип")
    print("4 - Тип двигателя")
    print("5 - Страну производителя")
    print("6 - Гос номер авто")
    print("7 - Цвет машины")
    print("8 - Кол-во дверей")
    if vvod == 1:
        print("Вы успешно удалили марку")
        cardelete[0] = "NI"
    elif vvod == 2:
        print("Вы успешно удалили подель модель:")
        cardelete[vvod - 1] = "NI "
    elif vvod == 3:
        print("Вы успешно удалили тип машины")
        cardelete[vvod - 1] = "NI"
    elif vvod == 4:
        print("Вы успешно удалили тип двигателя")
        cardelete[vvod - 1] = "NI"
    elif vvod == 5:
        print("Вы успешно удалили страну производителя")
        cardelete[vvod - 1] = "NI"
    elif vvod == 6:
        print("Вы успешно удалили госномер авто")
        cardelete[vvod - 1] = "NI"
    elif vvod == 7:
        print("Вы успешно удалили цвет машины")
        cardelete[vvod - 1] = "NI"
    elif vvod == 8:
        print("Вы успешно удалили кол-во дверей")
        cardelete[vvod - 1] = "NI"
    else:
        print("Вы ввели не существующее значение, повторите попытку")
        return 0
    return cars


def ydaleine_car(cars, vvod):
    cars_vivod = []
    for i in range(len(cars)):
        cars_vivod.append(cars[i])
    for q in range(len(cars_vivod)):
        cars_vivod[q] = [q + 1] + cars_vivod[q]
    delete_car = cars
    dl_c_p = 0
    count = 0
    print("Введите номер строки, машину которой вы хотите удалить:")
    dl_c_ch = vvod
    for j in range(len(cars_vivod)):
        if dl_c_ch == cars_vivod[j][0]:
            dl_c_p = j
            count += 1
    if delete_car[dl_c_p] in delete_car and count != 0:
        delete_car.remove(delete_car[dl_c_p])
        print("Вы успешно удалили машину")
        return cars
    else:
        print("Данной машины не существует, повторите попытку")
        return 0


def poisk(cars, vvod):
    s = vvod
    s = s.split(" ")
    count = 0
    for i in range(len(cars)):
        b = []
        for j in range(len(cars[i])):
            for q in range(len(s)):
                if s[q] == cars[i][j]:
                    b.append(cars[i][j])
                    count += 1
                    if len(b) == len(s) and count != 0:
                        return cars[i]


class CarZapis(unittest.TestCase):
    def test_zapis_positive(self):
        result = zapis("mazda", "CX5", "Sport", "Turbo", "USA", "BA235H", "White", "8")
        self.assertEqual(result, [["mazda", "CX5", "Sport", "Turbo", "USA", "BA235H", "White", "8"]])

    def test_zapis_positive_1(self):
        result = zapis("Ford", "Focus", "Sedan", "Turbo", "France", "HA780K", "Black", "8")
        self.assertEqual(result, [["Ford", "Focus", "Sedan", "Turbo", "France", "HA780K", "Black", "8"]])

    def test_zapis_positive_2(self):
        result = zapis("Tesla", "Model SSS", "SSSport", "Electro", "USA", "CA456K", "Black", "8")
        self.assertEqual(result, [["Tesla", "Model SSS", "SSSport", "Electro", "USA", "CA456K", "Black", "8"]])


class Carsvivod(unittest.TestCase):
    def test_zamena(self):
        result = zapis("Tesla", "Model SSS", "SSSport", "Electro", "USA", "CA456K", "Black", "8")
        result_1 = zamena_xarki(result, 1, 8, "20")
        self.assertEqual(result_1, [["Tesla", "Model SSS", "SSSport", "Electro", "USA", "CA456K", "Black", "20"]])

    def test_zamena_1(self):
        result = zapis("Ford", "Focus", "Sedan", "Turbo", "France", "HA780K", "Black", "8")
        result_1 = zamena_xarki(result, 1, 6, "BO040K")
        self.assertEqual(result_1, [["Ford", "Focus", "Sedan", "Turbo", "France", "BO040K", "Black", "8"]])

    def test_ydalenie(self):
        result = zapis("Mazda", "CX5", "Sport", "Turbo", "USA", "BA235H", "White", "8")
        result_1 = ydalenie_xarki(result, 1, 3)
        self.assertEqual(result_1, [["Mazda", "CX5", "NI", "Turbo", "USA", "BA235H", "White", "8"]])


if __name__ == "__main__":
    unittest.main()
