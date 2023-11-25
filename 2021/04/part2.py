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
            if all(row):
                return True
        for j in range(len(self.boardMarked[0])):
            if all(row[j] for row in self.boardMarked):
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
        boardsWon = []
        while infile.readline():
            boards.append(BingoBoard([[int(x) for x in infile.readline().split()] for _ in range(5)]))
            boardsWon.append(False)

    for num in bingoSequence:
        for i in range(len(boards)):
            boards[i].mark(num)
            if boards[i].hasWon():
                boardsWon[i] = True
                if all(boardsWon):
                    print(boards[i].calcScore(num))
                    return


if __name__ == '__main__':
    main()

    # for b in boards:
    #     print(b.board)
    #     print(b.boardMarked)
