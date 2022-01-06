def isInTarget(initial_x, initial_y, target_x, target_y):
    position_x, position_y = 0, 0
    trajectory = [(position_x, position_y)]
    velocity_x, velocity_y = initial_x, initial_y
    while position_x <= target_x[1] and position_y >= target_y[0]:
        position_x += velocity_x
        position_y += velocity_y
        trajectory.append((position_x, position_y))
        if target_x[1] >= position_x >= target_x[0] and target_y[0] <= position_y <= target_y[1]:
            return True, trajectory
        velocity_x -= 1 if velocity_x > 0 else (-1 if velocity_x < 0 else 0)
        velocity_y -= 1
    return False, trajectory


if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        line = infile.readline().strip()
        target_x_string, target_y_string = line[13:].split(", ")
        target_x = [int(x) for x in target_x_string[2:].split("..")]
        target_y = [int(y) for y in target_y_string[2:].split("..")]
    print("Target Area: x={}, y={}".format(target_x, target_y))
    viable_initials = set()
    #Hahaha
    for i in range(-300, 300):
        for j in range(-300, 300):
            it_is, _ = isInTarget(i, j, target_x, target_y)
            if it_is:
                viable_initials.add((i, j))
    #print(viable_initials)
    print(len(viable_initials))
