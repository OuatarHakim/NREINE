from tkinter import *

chessboard = []
queen_position = []
solution = []


def initChessboard(n):
    for i in range(0, n):
        queen_position.append(0)
        line = []
        for j in range(0, n):
            line.append(0)
        chessboard.append(line)


def checkCase(line, column):
    for i in range(0, column):
        # abs for a nigative value
        if queen_position[i] == line or abs(queen_position[i] - line) == abs(i - column):
            return False
    return True


def execute(n, r):
    global solution
    if r == n:
        solution = solution + queen_position
        print(queen_position)

    else:
        for i in range(0, n):
            if checkCase(i, r):
                queen_position[r] = i
                execute(n, r + 1)


def compute(n):
    global queen_position, solution
    solution = []
    initChessboard(n)
    execute(n, 0)


def show():
    for line in chessboard:
        for case in line:
            print(case, ",", end="")
        print("")


def poser(n):
    for i in range(0, n):
        for j in range(0, n):
            chessboard[i][j] = 0
    for i in range(0, n):
        chessboard[queen_position[i]] = 1
    show()


if __name__ == "__main__":
    compute(8)
  #  print(solution)
    poser(4)
    fenetre = Tk()

    label = Label(fenetre, text="Hello World")
    label.pack()

    fenetre.mainloop()
