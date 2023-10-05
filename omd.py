import csv


def deps_from_table(table):
    """Getting departments from table"""
    departments = set()
    for i in range(1, len(table)):
        departments.add(table[i][1])
    list_dep = list(departments)
    return list_dep


def func1(table):
    """compliting first option"""
    l_d = deps_from_table(table)
    for i in range(len(l_d)):
        cmd = set()
        for j in range(len(table)):
            if table[j][1] == l_d[i]:
                cmd.add(table[j][2])
        cmd_l = list(cmd)
        print(l_d[i], ":", *cmd_l)


def svod_table(table):
    """Getting pivot table for option 2"""
    l_d = deps_from_table(table)
    new_table = []
    for i in range(len(l_d)):
        a = list()
        a.append(l_d[i])
        counter = 0
        summ = 0
        minn = 100000000
        maxx = 0
        for j in range(len(table)):
            if table[j][1] == l_d[i]:
                zp = int(table[j][5])
                counter += 1
                summ += zp
                if zp > maxx:
                    maxx = zp
                if zp < minn:
                    minn = zp
        a.append(counter)
        a.append(minn)
        a.append(maxx)
        a.append(summ/counter)
        new_table.append(a)
    return new_table


def func2(table):
    """compliting second option"""
    new_table = svod_table(table)
    for cur in new_table:
        print('{}: {}, {}-{}, {}'.format(*cur))


def func3(table):
    """compliting third option"""
    new_table = svod_table(table)
    with open("1234.csv", "w+") as res_file:
        file_write = csv.writer(res_file, delimiter=';')
        file_write.writerows(new_table)


def options():
    """Printing of options and input of switched option"""
    print("Выберите:\n"
          "1. Вывести в понятном виде иерархию команд, "
          "т.е. департамент и все команды, которые входят в него\n"
          "2. Вывести сводный отчёт по департаментам: название, численность, "
          "вилка зарплат в виде мин – макс, среднюю зарплату\n"
          "3. Сохранить сводный отчёт из предыдущего пункта в виде csv-файла."
          "При этом необязательно вызывать сначала команду из п.2")
    opt = ''
    opts = {'1': 1, '2': 2, '3': 3}
    while opt not in opts:
        print('Выберите: {}/{}/{}'.format(*opts))
        opt = input()
    return opt, opts


def file_read():
    """Reading of file"""
    with open("Corp_Summary.csv") as file_name:
        file_r = csv.reader(file_name, delimiter=';')
        rep = list(file_r)
        return rep


if __name__ == '__main__':
    option, options = options()
    report = file_read()
    if options[option] == 1:
        func1(report)
    elif options[option] == 2:
        func2(report)
    else:
        func3(report)
