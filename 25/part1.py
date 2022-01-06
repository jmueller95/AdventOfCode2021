def simulate_step(cucumber_map):
    any_change = False
    res = [row.copy() for row in cucumber_map]
    # First iteration: East-facing cucumbers
    for i in range(len(cucumber_map)):
        for j in range(len(cucumber_map[i])):
            if cucumber_map[i][j] == '>':
                next_position = j + 1 if j + 1 < len(cucumber_map[i]) else 0
                if cucumber_map[i][next_position] == '.':
                    any_change = True
                    res[i][j] = '.'
                    res[i][next_position] = '>'
    # Update cucumber map because the south-facing cucumbers move after the east ones
    cucumber_map = [row.copy() for row in res]
    res = [row.copy() for row in cucumber_map]
    # Second iteration: South-facing cucumbers
    for i in range(len(cucumber_map)):
        for j in range(len(cucumber_map[i])):
            if cucumber_map[i][j] == 'v':
                next_position = i + 1 if i + 1 < len(cucumber_map) else 0
                if cucumber_map[next_position][j] == '.':
                    any_change = True
                    res[i][j] = '.'
                    res[next_position][j] = 'v'
    return res, any_change


if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        cucumber_map = [[cell for cell in row.strip()] for row in infile]

    any_change = True
    steps = 0
    while any_change:
        steps += 1
        cucumber_map, any_change = simulate_step(cucumber_map)

    print("Terminated after {} steps.".format(steps))

    # for row in cucumber_map:
    #    print("".join(row))
