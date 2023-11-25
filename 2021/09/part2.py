from collections import Counter

if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        data = [[int(n) for n in line.strip()] for line in infile]
    basin_map = [[None for _ in range(len(data[0]))] for _ in range(len(data))]

    basin_counter = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 9:
                basin_map[i][j] = -1
            elif i > 0 and data[i - 1][j] < 9 and j > 0 and data[i][j - 1] < 9 and basin_map[i - 1][j] != basin_map[i][
                j - 1]:
                basin_map[i][j] = basin_map[i - 1][j]
                basin_to_merge = basin_map[i][j - 1]
                # I know this is O(n^4) but I'm lazy and it works
                for k in range(len(data)):
                    for l in range(len(data[k])):
                        if basin_map[k][l] == basin_to_merge:
                            basin_map[k][l] = basin_map[i - 1][j]
            elif i > 0 and data[i - 1][j] < 9:
                basin_map[i][j] = basin_map[i - 1][j]
            elif j > 0 and data[i][j - 1] < 9:
                basin_map[i][j] = basin_map[i][j - 1]
            else:
                basin_counter += 1
                basin_map[i][j] = basin_counter
    basin_sizes = Counter([basin_id for row in basin_map for basin_id in row if basin_id != -1])
    # print(basin_sizes)
    # for row in basin_map:
    #     print(row)
    basin_sizes_sorted = sorted(basin_sizes.values(), reverse=True)
    print(basin_sizes_sorted[0] * basin_sizes_sorted[1] * basin_sizes_sorted[2])
