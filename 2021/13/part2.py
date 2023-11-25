if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        dots = set()
        dot_line = infile.readline().strip()
        while dot_line:
            x, y = int((linesplit := dot_line.split(","))[0]), int(linesplit[1])
            dots.add((x, y))
            dot_line = infile.readline().strip()
        fold_line = infile.readline().strip()
        while fold_line:
            isFoldHorizontal = (linesplit := fold_line.split("="))[0][-1] == 'y'
            foldAxis = int(linesplit[1])
            new_dots = set()
            for x, y in dots:
                new_dots.add((x if isFoldHorizontal or x < foldAxis else x - 2 * (x - foldAxis),
                              y if not isFoldHorizontal or y < foldAxis else y - 2 * (y - foldAxis)))
            dots = new_dots
            fold_line = infile.readline().strip()
        max_x = max(x for x, y in dots)
        max_y = max(y for x, y in dots)
        for j in range(max_y + 1):
            print("".join(['#' if (i, j) in dots else '-' for i in range(max_x + 1)]))
