from tabulate import tabulate

with open('3.txt', "r+") as cars:
    lines = cars.readlines()

while True:
    print("Если хотите добаить машину, нажмите 1")
    print("Если хотите вывести список машин, нажмите 2")
    print("Если хотите изменить/удалить характеристики, нажмите 3")
    print("Если хотите удалить машину, нажмите 4")
    print("Если хотите найти машину, нажмите 5")
    print("Если хотите выйти, нажмите 0")
    first_q = str(input())

    if first_q == "1":
        with open("3.txt", "a+") as a:
            print("Добавьте марку машины:")
            marka = str(input())
            print("Добавьте модель машины:")
            model = str(input())
            print("Добавьте тип машины:")
            tip = str(input())
            print("Добавьте тип двигателя машины:")
            tip_d = str(input())
            print("Добавьте страну производителя машины:")
            county = str(input())
            print("Добавьте госномер авто")
            gosn = str(input())
            print("Введите цвет машины")
            colour = str(input())
            print("Введите кол-во дверей")
            doors = str(input())
            s = marka + " " + model + " " + tip + " " + tip_d + " " + county + " " + gosn + " " + colour + " " + doors + " "
            a.write(s + "\n")

    elif first_q == "2":
        with open("3.txt") as f:
            cars_line = f.readlines()
            stroka = []
            stroka_1 = []
            for i in range(len(cars_line)):
                mass = []
                dl = ""
                for j in range(len(cars_line[i])):
                    if cars_line[i][j] != " ":
                        dl += cars_line[i][j]
                    else:
                        mass = mass + [dl]
                        dl = ""
                stroka = stroka + [mass]
            data = [
                ["Номер", "Марка", "Модель", "Тип машины", "Тип двигателя", "Страна производителя", "Госномер авто",
                 "Цвет машины",
                 "Кол-во дверей"]]
            for q in range(len(stroka)):
                stroka_1 = stroka_1 + [stroka[q]]
                stroka[q] = [q + 1] + stroka[q]
                data = data + [stroka[q]]
            table = tabulate(data, headers="firstrow", tablefmt="fancy_grid")
            print(table)

    elif first_q == "3":
        while True:
            print("Если хотите изменить характеристики нажмите 1")
            print("Если хотите удалить характеристику нажмите 2")
            print("Если хотите выйти, нажмите 0")
            second_q = str(input())
            if second_q == "1":
                with open("3.txt") as f:
                    cars_line = f.readlines()
                    stroka = []
                    stroka_1 = []
                    for i in range(len(cars_line)):
                        mass = []
                        dl = ""
                        for j in range(len(cars_line[i])):
                            if cars_line[i][j] != " ":
                                dl += cars_line[i][j]
                            else:
                                mass = mass + [dl]
                                dl = ""
                        stroka = stroka + [mass]
                    data = [
                        ["Номер", "Марка", "Модель", "Тип машины", "Тип двигателя", "Страна производителя",
                         "Госномер авто",
                         "Цвет машины",
                         "Кол-во дверей"]]
                    for q in range(len(stroka)):
                        stroka_1 = stroka_1 + [stroka[q]]
                        stroka[q] = [q + 1] + stroka[q]
                        data = data + [stroka[q]]
                    table = tabulate(data, headers="firstrow", tablefmt="fancy_grid")
                    print(table)
                new_stroka = stroka_1
                print("Введите строку, которую хотите изменить")
                izmena = int(input())
                zamena = new_stroka[izmena - 1]
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
                    s1 = str(input())
                    zamena[vvod - 1] = s1
                    print("Вы успешно изменили хар-ку")
                elif vvod == 2:
                    print("Вы меняете модель, напишите модель:")
                    s2 = str(input())
                    zamena[vvod - 1] = s2
                    print("Вы успешно изменили хар-ку")
                elif vvod == 3:
                    print("Вы меняете тип машины, напишите тип машины:")
                    s3 = str(input())
                    zamena[vvod - 1] = s3
                    print("Вы успешно изменили хар-ку")
                elif vvod == 4:
                    print("Вы меняете тип двигателя, напишите тип двигателя:")
                    s4 = str(input())
                    zamena[vvod - 1] = s4
                    print("Вы успешно изменили хар-ку")
                elif vvod == 5:
                    print("Вы меняете страну производителя, напишите страну производителя:")
                    s5 = str(input())
                    zamena[vvod - 1] = s5
                    print("Вы успешно изменили хар-ку")
                elif vvod == 6:
                    print("Вы меняете госномер авто, напишите госномер авто:")
                    s6 = str(input())
                    zamena[vvod - 1] = s6
                    print("Вы успешно изменили хар-ку")
                elif vvod == 7:
                    print("Вы меняете цвет машины, напишите цвет машины:")
                    s7 = str(input())
                    zamena[vvod - 1] = s7
                    print("Вы успешно изменили хар-ку")
                elif vvod == 8:
                    print("Вы меняете кол-во дверей, напишите кол-во дверей:")
                    s8 = str(input()) + " "
                    zamena[vvod - 1] = s8
                    print("Вы успешно изменили хар-ку")
                else:
                    print("Вы ввели неправильное значение, повторите попытку")
                st = ""
                for tt in range(len(zamena)):
                    st = st + zamena[tt] + " "
                if second_q == "1" and vvod == 8:
                    st = st[:-1] + "\n"
                else:
                    st += "\n"
                lines[izmena - 1] = st
                with open('3.txt', "w+") as ca:
                    for baa in lines:
                        ca.write(baa)

            elif second_q == "2":
                with open("3.txt") as f:
                    cars_line = f.readlines()
                    stroka = []
                    stroka_1 = []
                    for i in range(len(cars_line)):
                        mass = []
                        dl = ""
                        for j in range(len(cars_line[i])):
                            if cars_line[i][j] != " ":
                                dl += cars_line[i][j]
                            else:
                                mass = mass + [dl]
                                dl = ""
                        stroka = stroka + [mass]
                    data = [
                        ["Номер", "Марка", "Модель", "Тип машины", "Тип двигателя", "Страна производителя",
                         "Госномер авто",
                         "Цвет машины",
                         "Кол-во дверей"]]
                    for q in range(len(stroka)):
                        stroka_1 = stroka_1 + [stroka[q]]
                        stroka[q] = [q + 1] + stroka[q]
                        data = data + [stroka[q]]
                    table = tabulate(data, headers="firstrow", tablefmt="fancy_grid")
                    print(table)
                new_stroka = stroka_1
                print("Введите строку, параметр который, вы хотите удалить")
                izmena = int(input())
                ydalenie = new_stroka[izmena - 1]
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
                    ydalenie[vvod - 1] = "NI"
                elif vvod == 2:
                    print("Вы успешно удалили подель модель:")
                    ydalenie[vvod - 1] = "NI"
                elif vvod == 3:
                    print("Вы успешно удалили тип машины")
                    ydalenie[vvod - 1] = "NI"
                elif vvod == 4:
                    print("Вы успешно удалили тип двигателя")
                    ydalenie[vvod - 1] = "NI"
                elif vvod == 5:
                    print("Вы успешно удалили страну производителя")
                    ydalenie[vvod - 1] = "NI"
                elif vvod == 6:
                    print("Вы успешно удалили госномер авто")
                    ydalenie[vvod - 1] = "NI"
                elif vvod == 7:
                    print("Вы успешно удалили цвет машины")
                    ydalenie[vvod - 1] = "NI"
                elif vvod == 8:
                    print("Вы успешно удалили кол-во дверей")
                    ydalenie[vvod - 1] = "NI"
                st = ""
                for tt in range(len(ydalenie)):
                    st = st + ydalenie[tt] + " "
                if second_q == "1" and vvod == 8:
                    st = st[:-1] + "\n"
                else:
                    st += "\n"
                lines[izmena - 1] = st
                with open('3.txt', "w+") as ca:
                    for baa in lines:
                        ca.write(baa)
            elif second_q == "0":
                break
            else:
                print("Вы ввели неправильное значение")

    elif first_q == "4":
        with open("3.txt") as f:
            cars_line = f.readlines()
            stroka = []
            stroka_1 = []
            for i in range(len(cars_line)):
                mass = []
                dl = ""
                for j in range(len(cars_line[i])):
                    if cars_line[i][j] != " ":
                        dl += cars_line[i][j]
                    else:
                        mass = mass + [dl]
                        dl = ""
                stroka = stroka + [mass]
            data = [
                ["Номер", "Марка", "Модель", "Тип машины", "Тип двигателя", "Страна производителя", "Госномер авто",
                 "Цвет машины",
                 "Кол-во дверей"]]
            for q in range(len(stroka)):
                stroka_1 = stroka_1 + [stroka[q]]
                stroka[q] = [q + 1] + stroka[q]
                data = data + [stroka[q]]
            table = tabulate(data, headers="firstrow", tablefmt="fancy_grid")
            print(table)
        print("Введите номер строки машину которой вы хотите удалить")
        ch = str(input())
        lines[int(ch) - 1] = ""
        with open('3.txt', "w+") as c:
            for b in lines:
                c.write(b)
        print("Вы успешно удалили машину")

    elif first_q == "5":
        with open("3.txt") as f:
            cars_line = f.readlines()
            stroka = []
            stroka_1 = []
            for i in range(len(cars_line)):
                mass = []
                dl = ""
                for j in range(len(cars_line[i])):
                    if cars_line[i][j] != " ":
                        dl += cars_line[i][j]
                    else:
                        mass = mass + [dl]
                        dl = ""
                stroka = stroka + [mass]
            data = [
                ["Номер", "Марка", "Модель", "Тип машины", "Тип двигателя", "Страна производителя", "Госномер авто",
                 "Цвет машины",
                 "Кол-во дверей"]]
            for q in range(len(stroka)):
                stroka_1 = stroka_1 + [stroka[q]]
                stroka[q] = [q + 1] + stroka[q]
                data = data + [stroka[q]]
            table = tabulate(data, headers="firstrow", tablefmt="fancy_grid")
            print(table)
        poisk_1 = stroka_1
        print("Введите что хотите найти:")
        poisk = str(input()) + " "
        da = ""
        maass = []
        for z in range(len(poisk)):
            if poisk[z] != " ":
                da += poisk[z]
            else:
                maass = maass + [da]
                da = ""
        for p in range(len(poisk_1)):
            b = []
            for m in range(len(poisk_1[p])):
                for y in range(len(maass)):
                    if maass[y] == poisk_1[p][m]:
                        b = b + [poisk_1[p][p]]
                        if len(maass) == len(b):
                            data_1 = [["Марка", "Модель", "Тип машины", "Тип двигателя", "Страна производителя",
                                       "Госномер авто",
                                       "Цвет машины", "Кол-во дверей"]]
                            data_1 = data_1 + [poisk_1[p]]
                            table_search = tabulate(data_1, headers="firstrow", tablefmt="fancy_grid")
                            print(table_search)

    elif first_q == "0":
        break

    else:
        print("Вы ввели не правильное значение, повторите попытку")
