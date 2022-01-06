if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        data = [int(x) for x in infile.readline().split(",")]

    for day in range(80):
        # print(data)
        n_new_fish = sum([fish == 0 for fish in data])
        data = [fish - 1 if fish > 0 else 6 for fish in data]
        data += n_new_fish * [8]
    print(len(data))
