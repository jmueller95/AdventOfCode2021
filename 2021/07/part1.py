if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        data = [int(x) for x in infile.readline().split(",")]
    position2fuel = {n: sum(abs(n - i) for i in data) for n in range(max(data))}
    print(min(position2fuel.values()))

