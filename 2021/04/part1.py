class BingoBoard:
    def __init__(self, board):
        self.board = board
        self.boardMarked = [[False
                             for _ in range(len(board[0]))]
                            for _ in range(len(board[0]))]

    def mark(self, bingoNumber):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == bingoNumber:
                    self.boardMarked[i][j] = True

    def hasWon(self):
        for row in self.boardMarked:
            if sum(row) == len(row):
                return True
        for j in range(len(self.boardMarked[0])):
            if sum(row[j] for row in self.boardMarked) == len(self.boardMarked):
                return True
        return False

    def calcScore(self, winningNumber):
        sum = 0
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if not self.boardMarked[i][j]:
                    sum += self.board[i][j]
        return winningNumber * sum


def main():
    input = "input.txt"
    with open(input, 'r') as infile:
        bingoSequence = [int(x) for x in infile.readline().split(",")]
        boards = []
        while infile.readline():
            boards.append(BingoBoard([[int(x) for x in infile.readline().split()] for _ in range(5)]))

    for num in bingoSequence:
        for board in boards:
            board.mark(num)
            if board.hasWon():
                print(board.calcScore(num))
                return


if __name__ == '__main__':
    main()

    # for b in boards:
    #     print(b.board)
    #     print(b.boardMarked)
