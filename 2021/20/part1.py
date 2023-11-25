if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        enhancement_algorithm = infile.readline().strip()
        infile.readline()
        input_image = [[pixel for pixel in line.strip()] for line in infile]
    for row in input_image:
        print("".join(row))
    print("\n------------------------------------------------------------------------------------------------------\n")

    for iteration in range(2):
        print("Input has dimension {}x{}".format(len(input_image), len(input_image[0])))
        output_image = []
        for i in range(-1, len(input_image) + 1):
            output_row = []
            for j in range(-1, len(input_image[0]) + 1):
                output_pixel = ""
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if 0 <= k < len(input_image) and 0 <= l < len(input_image[k]):
                            output_pixel += input_image[k][l]
                        else:
                            # Son of a b*tch, this one was tough.
                            # https://preview.redd.it/aq491f9nqp681.png?width=960&crop=smart&auto=webp&s=f95bdb40fdc359cc7b6cf9c988434d6c5fe499fd
                            output_pixel += '.' if iteration % 2 == 0 else '#'
                output_row.append(
                    enhancement_algorithm[int(output_pixel.replace('.', '0').replace('#', '1'), 2)])
            output_image.append(output_row)
        for row in output_image:
            print("".join(row))
        print("Output has dimension {}x{}".format(len(output_image), len(output_image[0])))
        print("{} pixels are lit".format(sum(pixel == '#' for row in output_image for pixel in row)))
        print(
            "\n------------------------------------------------------------------------------------------------------\n")
        input_image = output_image
