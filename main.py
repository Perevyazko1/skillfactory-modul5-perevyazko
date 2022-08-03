#___________________________________________________________________________________________________________
import random
import numpy as np

def check_free(field):
    idx = np.where(np.array(field) ==" ")
    res = list(zip(idx[0], idx[1]))
    res = random.choice(res)
    x = res[0]
    y = res[1]
    return x,y


def greet():
    print("-----------------------\n"
    "    Приветсвуем вас  \n"
    "        в игре       \n"
    "крестики-нолики c БОТом \n"
    "-----------------------\n"
    " формат ввода: x , y \n"
    " x - номер строки  \n"
    " y - номер столбца \n")
    global name
    name = input('Введите ваше имя:')



def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")


def ask():
    while True:
        cords = input(f"Ваш ход {name} : ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")

            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


def check_win():

    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            show()
            print(f"Выиграл {name}!!!")

            return True
        if symbols == ["0", "0", "0"]:
            show()
            print("Выиграл БОТ!!!")

            return True
    return False

global name
greet()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        x, y = ask()
        print(f" Ходит {name}!")
    else:
        print(" БОТ сделал ход!")
        x, y = check_free(field)

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break


#_____________________________________________________________________________________________
