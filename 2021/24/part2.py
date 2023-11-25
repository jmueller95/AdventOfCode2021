if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        input = [line.split() for line in infile]
    # The input is organized in chunks of 18
    model_number = [None for _ in range(14)]
    y_stack = []
    for position, i in enumerate(range(0, len(input), 18)):
        chunk = input[i:i + 18]
        # Test if we have a div1 or a div26 operation
        if chunk[4][2] == '1':
            # Push the 'y addition' onto the stack
            y_stack.append((position, int(chunk[15][2])))
        else:
            # Pop the 'y addition' from the stack and combine it with the 'x addition' of this chunk
            y_pos, y = y_stack.pop()
            x = int(chunk[5][2])
            # Using the two, we can obtain 2 of the 14 digits of the model number
            if x + y > 0:
                model_number[y_pos] = 1
                model_number[position] = 1 + (x + y)
            else:
                model_number[position] = 1
                model_number[y_pos] = 1 - (x + y)
    print("".join(str(x) for x in model_number))
