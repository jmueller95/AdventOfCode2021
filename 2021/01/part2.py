if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        data = [int(l) for l in infile.readlines()]
    print(sum([data[i] < data[i + 3] for i in range(len(data) - 3)]))
