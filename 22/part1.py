if __name__ == '__main__':
    input = "input.txt"
    cubes_on = set()
    with open(input, 'r') as infile:
        for lineno, line in enumerate(infile):
            print("Processing line {}".format(lineno + 1))
            command, ranges = line.split()
            is_on_command = command == "on"
            x_range, y_range, z_range = [
                range(max(int((rangesplit := r[2:].split(".."))[0]), -50), min(int(rangesplit[1]) + 1, 51))
                for r in ranges.split(",")]
            # print("Turning on: {}".format(is_on_command))
            # print("X: {}".format(x_range))
            # print("Y: {}".format(y_range))
            # print("Z: {}".format(z_range))
            if is_on_command:
                cubes_on |= {(x, y, z) for x in x_range for y in y_range for z in z_range}
            else:
                cubes_on -= {(x, y, z) for x in x_range for y in y_range for z in z_range}
    print(len(cubes_on))
