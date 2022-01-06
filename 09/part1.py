if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        data = [[int(n) for n in line.strip()] for line in infile]
    res = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (i == 0 or data[i - 1][j] > data[i][j]) and (i == len(data) - 1 or data[i + 1][j] > data[i][j]) and (
                    j == 0 or data[i][j - 1] > data[i][j]) and (j == len(data[i]) - 1 or data[i][j + 1] > data[i][j]):
                res += data[i][j] + 1

    print(res)
