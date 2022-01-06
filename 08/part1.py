if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        data = [((linesplit := line.split())[:10], linesplit[11:]) for line in infile]
    print(sum(len(output_digit) in [2, 4, 3, 7] for line in data for output_digit in line[1]))
