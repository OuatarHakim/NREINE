class Chessboard:
    chessboard = []
    queen_position = []
    n = 0

    def __init__(self, n):
        self.chessboard = []
        self.queen_position = []
        self.n = n

    def init(self):
        for i in range(0, self.n):
            self.queen_position.append(0)
            line = []
            for j in range(0, self.n):
                line.append(0)
            self.chessboard.append(line)

    def __show(self):
        for line in self.chessboard:
            for case in line:
                print(case, ",", end="")
            print("")

    def poser(self):
        for i in range(0, self.n):
            for j in range(0, self.n):
                self.chessboard[i][j] = 0
        for i in range(0, self.n):
            self.chessboard[self.queen_position[i]] = 1
        self.__show()

    def checkCase(self,line, column):
        for i in range(0, column):
            # abs for a nigative value
            if self.queen_position[i] == line or abs(self.queen_position[i] - line) == abs(i - column):
                return False
        return True

    def execute(self , r):
        if r == self.n:
            print(self.queen_position)

        else:
            for i in range(0, self.n):
                if self.checkCase(i, r):
                    self.queen_position[r] = i
                    self.execute(r + 1)

    def compute(self):
        self.execute(0)
