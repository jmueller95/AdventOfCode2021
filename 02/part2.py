if __name__ == '__main__':
    input = "input.txt"
    horiz, depth, aim = 0, 0, 0
    with open(input, 'r') as infile:
        for line in infile:
            direction, amount = line.strip().split()
            if direction == "forward":
                horiz += int(amount)
                depth += aim * int(amount)
            elif direction == "down":
                aim += int(amount)
            else:
                aim -= int(amount)
    print(horiz * depth)
