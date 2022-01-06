if __name__ == '__main__':
    input = "input.txt"
    horiz, depth = 0, 0
    with open(input, 'r') as infile:
        for line in infile:
            direction, amount = line.strip().split()
            if direction == "forward":
                horiz += int(amount)
            elif direction == "down":
                depth += int(amount)
            else:
                depth -= int(amount)
    print(horiz * depth)
