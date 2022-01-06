if __name__ == '__main__':
    input = "input.txt"
    caves = dict()
    with open(input, 'r') as infile:
        for line in infile:
            sourceCave, targetCave = line.strip().split("-")
            if sourceCave not in caves:
                caves[sourceCave] = set()
            if targetCave not in caves:
                caves[targetCave] = set()
            caves[sourceCave].add(targetCave)
            caves[targetCave].add(sourceCave)
    #for key, value in caves.items():
    #    print("{}: {}".format(key, value))

    paths = [['start']]
    path_counter = 0
    while paths:
        path = paths.pop()
        if path[-1] == 'end':
            path_counter +=1
            print(",".join(path))
        else:
            for targetCave in caves[path[-1]]:
                if targetCave != targetCave.lower() or targetCave not in path \
                or targetCave not in {'start', 'end'} and \
                len((small_caves := [cave for cave in path if cave == cave.lower()])) == len(set(small_caves)):
                    paths.append(path.copy() + [targetCave])
    print(path_counter)