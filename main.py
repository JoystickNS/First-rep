import os

field = []
cur_coure = ""
message = ""

class Color:
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    purple = "\033[35m"
    turquoise = "\033[36m"
    gray = "\033[0m"

def init_field():
    global field
    field.clear()
    for i in range(9):
        field.append(" ")

def redraw(cur_coure):
    os.system("clear")
    print(message)
    print("-------------------")
    for i in range(3):
        print("| ", field[i * 3], " | ", field[i * 3 + 1], " | ", field[i * 3 + 2], " |")
        print("-------------------")

def change_player():
    global cur_coure
    if cur_coure == "X":
        cur_coure = "O"
    else:
        cur_coure = "X" 

def check_field(field):
    wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for win in wins:
        if field[win[0]] == cur_coure == field[win[1]] == field[win[2]]:
            return False
    return True

def player_msg(message, cur_coure):
    if cur_coure == "X":
        message = Color.turquoise + message + Color.red + cur_coure + Color.gray
    else:
        message = Color.turquoise + message + Color.blue + cur_coure + Color.gray
    return message

def play():
    global cur_coure, message
    gameon = True
    init_field()
    cur_coure = "X"
    step = 0
    while gameon:
        message = player_msg("Сейчас ходит игрок ", cur_coure)
        redraw(cur_coure)
        player_sel = 0
        while 1 > player_sel < 9:
            try:
                player_sel = int(input("Введите номер клетки, в которую вы хотите сходить "))
                if field[player_sel - 1] == " ":
                    field[player_sel - 1] = cur_coure
                    step += 1
                    if step > 4:
                        gameon = check_field(field)
                        if not gameon:
                            message = player_msg("Выйграл игрок ", cur_coure)
                            return
                        elif step >= 9:
                            message = Color.yellow + "Ничья" + Color.gray
                            return
                    change_player()
                else:
                    print("Эта клетка уже занята.")
            except (ValueError, IndexError):
                print("Такой клетки не существует.")
                player_sel = 0


while True:
    play()
    redraw(cur_coure)
    s = input(Color.green + "Сыграть ещё? (y/n) " + Color.gray)
    while s not in "yn":
        s = input(Color.green + "Сыграть ещё? (y/n) " + Color.gray)
    if s == "n":
        break
