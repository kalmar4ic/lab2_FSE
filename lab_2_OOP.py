from tabulate import tabulate


def to_file(data):
    string = ""
    for line in data:
        string += '_'.join(line)
        string += "\n"
    with open('1.txt', 'w', encoding="utf-8") as carsf:
        carsf.write(string)


spisok = open("1.txt", encoding="utf-8").readlines()
spisok = [line.strip().split("_") for line in spisok]
name_columns = spisok[0]
cars = spisok[1:]


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
        for name_column in name_columns:
            print(f"Добавьте {name_column}:")
            value = str(input())
            if value == "" or value == "\n":
                add_car.append("None")
            else:
                add_car.append(value)

        cars.append(add_car)
        to_file([name_columns] + cars)

    elif first_q == 2:
        data = [["Номер"] + name_columns]
        for i in range(len(cars)):
            data.append([str(i + 1)] + cars[i])
        table = tabulate(data, headers="firstrow", tablefmt="fancy_grid")
        print(table)


    elif first_q == 3:
        while True:
            print("Если хотите изменить характеристики нажмите 1")
            print("Если хотите удалить характеристику нажмите 2")
            print("Если хотите выйти, нажмите 0")
            second_q = str(input())

            if second_q == "1":
                data = [["Номер"] + name_columns]
                for i in range(len(cars)):
                    data.append([str(i + 1)] + cars[i])
                table = tabulate(data, headers="firstrow", tablefmt="fancy_grid")
                print(table)
                table = tabulate(data, headers="firstrow", tablefmt="fancy_grid")
                print(table)

                print("Выберите номер машины, характеристики которой хотите изменить:")
                search = int(input())
                if 0 < search <= len(cars):
                    care = cars[search]
                else:
                    print("Вы ввели не существующее значение, повторите попытку")

                print("Выберите, что хотите изменить:")
                for i in range(len(name_columns)):
                    print(f"{i + 1} - {name_columns[i]}")
                change = int(input())


                if 0 < change < len(name_columns):
                    print(f"Вы меняете {name_columns[change - 1]}:")
                    cars[search - 1][change - 1] = str(input())
                    print("Вы успешно изменили хар-ку")
                else:
                    print("Вы ввели неправильное значение, повторите попытку")
                to_file([name_columns] + cars)

            elif second_q == "2":
                data = [["Номер"] + name_columns]
                for i in range(len(cars)):
                    data.append([str(i + 1)] + cars[i])
                table = tabulate(data, headers="firstrow", tablefmt="fancy_grid")
                print(table)

                print("Выберите номер машины, характеристики которой хотите удалить:")
                search = int(input())
                if 0 < search <= len(cars):
                    care = cars[search]
                else:
                    print("Вы ввели не существующее значение, повторите попытку")

                print("Выберите, что хотите удалить:")
                for i in range(len(name_columns)):
                    print(f"{i + 1} - {name_columns[i]}")
                change = int(input())

                if 0 < change < len(name_columns):
                    print(f"Вы удаляете {name_columns[change - 1]}:")
                    cars[search - 1][change - 1] = "None"
                    print("Вы успешно изменили хар-ку")
                else:
                    print("Вы ввели неправильное значение, повторите попытку")
                to_file([name_columns] + cars)

    elif first_q == 4:
        data = [["Номер"] + name_columns]
        for i in range(len(cars)):
            data.append([str(i + 1)] + cars[i])
        table = tabulate(data, headers="firstrow", tablefmt="fancy_grid")
        print(table)

        print("Введите номер строки, машину которой вы хотите удалить:")
        change = int(input())
        if 0 < change <= len(cars):
            cars.pop(change - 1)
            print("Вы успешно удалили машину")
        else:
            print("Данной машины не существует, повторите попытку")
        to_file([name_columns] + cars)

    elif first_q == 5:
        data = [["Номер"] + name_columns]
        for i in range(len(cars)):
            data.append([str(i + 1)] + cars[i])
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
                            data = [name_columns, cars[i]]
                            table_search = tabulate(data, headers="firstrow", tablefmt="fancy_grid")
                            print(table_search)

    if first_q == 0:
        to_file([name_columns] + cars)
        break