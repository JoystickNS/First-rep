import os

field = []
cur_coure = "X"
message = "Сейчас ходит игрок " + cur_coure

def init_field():
    for i in range(9):
        field.append(" ")

def redraw():
    #os.system("clear")
    print(message)
    print("| ", field[0], " | ", field[1], " | ", field[2], " |")
    print("-------------------")
    print("| ", field[3], " | ", field[4], " | ", field[5], " |")
    print("-------------------")
    print("| ", field[6], " | ", field[7], " | ", field[8], " |")
    print("-------------------")

def change_player():
    global cur_coure
    if cur_coure == "X":
        cur_coure = "O"
    else:
        cur_coure = "X" 

def play():
    gameon = True
    while gameon:
        redraw()
        step = int(input("Введите номер клетки, в которую вы хохите сходить "))
        if field[step - 1] == " ":
            field[step - 1] = cur_coure
            change_player()

init_field()
play()