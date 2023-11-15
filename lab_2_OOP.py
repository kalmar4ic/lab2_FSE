from tabulate import tabulate

spisok = open("1.txt", encoding="utf-8").read()
lspisok = len(spisok)
cars = []
if lspisok > 0:
    count = int((spisok.count("_") + 1) / 8)
    drspisok = spisok
    drspisok = drspisok.split("_")
    massiv = int(len(drspisok) / count)
    cars = [drspisok[i:i + massiv] for i in range(0, len(drspisok), massiv)]

while True:
    print("Если хотите добаить машину, нажмите 1")
    print("Если хотите вывести список машин, нажмите 2")
    print("Если хотите изменить/удалить характеристики, нажмите 3")
    print("Если хотите удалить машину, нажмите 4")
    print("Если хотите найти машину, нажмите 5")
    print("Если хотите выйти, нажмите 0")
    first_q = int(input())

    if first_q == 1:
        add_car = []
        print("Добавьте марку машины:")
        marka = str(input())
        add_car.append(marka)
        print("Добавьте модель машины:")
        model = str(input())
        add_car.append(model)
        print("Добавьте тип машины:")
        tip = str(input())
        add_car.append(tip)
        print("Добавьте тип двигателя машины:")
        tip_d = str(input())
        add_car.append(tip_d)
        print("Добавьте страну производителя машины:")
        county = str(input())
        add_car.append(county)
        print("Добавьте госномер авто")
        gosn = str(input())
        add_car.append(gosn)
        print("Введите цвет машины")
        colour = str(input())
        add_car.append(colour)
        print("Введите кол-во дверей")
        doors = str(input())
        add_car.append(doors)
        cars.append(add_car)

    elif first_q == 2:
        cars_vivod = []
        for i in range(len(cars)):
            cars_vivod.append(cars[i])
        data = [
            ["Номер", "Марка", "Модель", "Тип машины", "Тип двигателя", "Страна производителя", "Госномер авто",
             "Цвет машины",
             "Кол-во дверей"]]
        for q in range(len(cars_vivod)):
            cars_vivod[q] = [q + 1] + cars_vivod[q]
            data.append(cars_vivod[q])
        table = tabulate(data, headers="firstrow", tablefmt="fancy_grid")
        print(table)

    elif first_q == 3:
        while True:
            print("Если хотите изменить характеристики нажмите 1")
            print("Если хотите удалить характеристику нажмите 2")
            print("Если хотите выйти, нажмите 0")
            second_q = str(input())

            if second_q == "1":
                cars_vivod = []
                for i in range(len(cars)):
                    cars_vivod.append(cars[i])
                data = [
                    ["Номер", "Марка", "Модель", "Тип машины", "Тип двигателя", "Страна производителя", "Госномер авто",
                     "Цвет машины",
                     "Кол-во дверей"]]
                for q in range(len(cars_vivod)):
                    cars_vivod[q] = [q + 1] + cars_vivod[q]
                    data.append(cars_vivod[q])
                table = tabulate(data, headers="firstrow", tablefmt="fancy_grid")
                print(table)

                carszam = []
                print("Напишите номер строки машины, которую Вы хотели бы изменить:")
                search = int(input())
                for c in range(len(cars_vivod)):
                    if search == cars_vivod[c][0]:
                        carszam = cars[c]
                if search > len(cars_vivod):
                    print("Вы ввели не существующее значение, повторите попытку")

                print("Выберите, что хотите изменить:")
                print("1 - Марка")
                print("2 - Модель")
                print("3 - Тип")
                print("4 - Тип двигателя")
                print("5 - Страну производителя")
                print("6 - Гос номер авто")
                print("7 - Цвет машины")
                print("8 - Кол-во дверей")
                vvod = int(input())
                if vvod == 1:
                    print("Вы меняете марку, напишите марку:")
                    carszam[0] = str(input())
                    print("Вы успешно изменили хар-ку")
                elif vvod == 2:
                    print("Вы меняете модель, напишите модель:")
                    carszam[vvod - 1] = str(input())
                    print("Вы успешно изменили хар-ку")
                elif vvod == 3:
                    print("Вы меняете тип машины, напишите тип машины:")
                    carszam[vvod - 1] = str(input())
                    print("Вы успешно изменили хар-ку")
                elif vvod == 4:
                    print("Вы меняете тип двигателя, напишите тип двигателя:")
                    carszam[vvod - 1] = str(input())
                    print("Вы успешно изменили хар-ку")
                elif vvod == 5:
                    print("Вы меняете страну производителя, напишите страну производителя:")
                    carszam[vvod - 1] = str(input())
                    print("Вы успешно изменили хар-ку")
                elif vvod == 6:
                    print("Вы меняете госномер авто, напишите госномер авто:")
                    carszam[vvod - 1] = str(input())
                    print("Вы успешно изменили хар-ку")
                elif vvod == 7:
                    print("Вы меняете цвет машины, напишите цвет машины:")
                    carszam[vvod - 1] = str(input())
                    print("Вы успешно изменили хар-ку")
                elif vvod == 8:
                    print("Вы меняете кол-во дверей, напишите кол-во дверей:")
                    carszam[vvod - 1] = str(input())
                    print("Вы успешно изменили хар-ку")
                else:
                    print("Вы ввели неправильное значение, повторите попытку")

            elif second_q == "2":
                cars_vivod = []
                for i in range(len(cars)):
                    cars_vivod.append(cars[i])
                data = [
                    ["Номер", "Марка", "Модель", "Тип машины", "Тип двигателя", "Страна производителя", "Госномер авто",
                     "Цвет машины",
                     "Кол-во дверей"]]
                for q in range(len(cars_vivod)):
                    cars_vivod[q] = [q + 1] + cars_vivod[q]
                    data.append(cars_vivod[q])
                table = tabulate(data, headers="firstrow", tablefmt="fancy_grid")
                print(table)

                cardelete = []

                print("Напишите номер скроки машины, которую Вы хотели бы удалить:")
                search = int(input())
                for c in range(len(cars_vivod)):
                    if search == cars_vivod[c][0]:
                        cardelete = cars[c]
                print("Выберите, что хотите удалить:")
                print("1 - Марка")
                print("2 - Модель")
                print("3 - Тип")
                print("4 - Тип двигателя")
                print("5 - Страну производителя")
                print("6 - Гос номер авто")
                print("7 - Цвет машины")
                print("8 - Кол-во дверей")
                vvod = int(input())
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
            elif second_q == "0":
                break
            else:
                print("Вы ввели неправильное значение, попробуйте снова")
    elif first_q == 4:
        cars_vivod = []
        for i in range(len(cars)):
            cars_vivod.append(cars[i])
        data = [
            ["Номер", "Марка", "Модель", "Тип машины", "Тип двигателя", "Страна производителя", "Госномер авто",
             "Цвет машины",
             "Кол-во дверей"]]
        for q in range(len(cars_vivod)):
            cars_vivod[q] = [q + 1] + cars_vivod[q]
            data.append(cars_vivod[q])
        table = tabulate(data, headers="firstrow", tablefmt="fancy_grid")
        print(table)

        delete_car = cars
        dl_c_p = 0
        count = 0
        print("Введите номер строки, машину которой вы хотите удалить:")
        dl_c_ch = int(input())
        for j in range(len(cars_vivod)):
            if dl_c_ch == cars_vivod[j][0]:
                dl_c_p = j
                count += 1
        if delete_car[dl_c_p] in delete_car and count != 0:
            delete_car.remove(delete_car[dl_c_p])
            print("Вы успешно удалили машину")
        else:
            print("Данной машины не существует, повторите попытку")

    elif first_q == 5:
        data = [["Марка", "Модель", "Тип машины", "Тип двигателя", "Страна производителя", "Госномер авто",
                 "Цвет машины", "Кол-во дверей"]]
        for q in range(len(cars)):
            data.append(cars[q])
        table = tabulate(data, headers="firstrow", tablefmt="fancy_grid")
        print(table)
        print("Введите что хотите найти:")
        s = str(input())
        s = s.split(" ")
        print(s)
        for i in range(len(cars)):
            b = []
            for j in range(len(cars[i])):
                for q in range(len(s)):
                    if s[q] == cars[i][j]:
                        b.append(cars[i][j])
                        if len(b) == len(s):
                            data = [["Марка", "Модель", "Тип машины", "Тип двигателя", "Страна производителя",
                                     "Госномер авто",
                                     "Цвет машины", "Кол-во дверей"], cars[i]]
                            table_search = tabulate(data, headers="firstrow", tablefmt="fancy_grid")
                            print(table_search)

    if first_q == 0:
        s = ""
        for i in range(len(cars)):
            for j in range(len(cars[i])):
                s = s + cars[i][j] + "_"
        s = s[:-1]
        with open('1.txt', 'w', encoding="utf-8") as carsf:
            carsf.write(s)
        break
