if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        data = [int(l) for l in infile.readlines()]
    print(sum([x < y for x, y in zip(data, data[1:])]))
