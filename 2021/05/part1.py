from collections import defaultdict

if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        ventlines = [(
            tuple(int(x) for x in line.split()[0].split(',')),
            tuple(int(x) for x in line.split()[2].split(','))
        ) for line in infile]
    coverage = defaultdict(int)
    for (start, stop) in ventlines:
        if start[0] == stop[0]:
            for y in range(min(start[1], stop[1]), max(start[1], stop[1]) + 1):
                coverage[start[0], y] += 1
        elif start[1] == stop[1]:
            for x in range(min(start[0], stop[0]), max(start[0], stop[0]) + 1):
                coverage[x, start[1]] += 1
    # for key, value in coverage.items():
    #    if value > 1:
    #        print(key)
    print(sum([value > 1 for key, value in coverage.items()]))
