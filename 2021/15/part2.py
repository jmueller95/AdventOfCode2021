if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        data = [[int(n) for n in line.strip()] for line in infile]
    data = [[((val + i + j - 1) % 9) + 1 for i in range(5) for val in row] for j in range(5) for row in data]
    # for row in data:
    #     print(row)
    # Dijkstra again
    distances = [[float('inf') for _ in range(len(data[0]))] for _ in range(len(data))]
    visited = [[False for _ in range(len(data[0]))] for _ in range(len(data))]
    distances[0][0] = 0
    i, j = 0, 0
    node_queue = {(0, 0): 0}
    while (i, j) != (len(data) - 1, len(data[i]) - 1):
        i, j = min(node_queue.keys(), key=lambda tup: node_queue[tup])
        # print("i={}, j={}".format(i, j))
        del node_queue[(i, j)]
        visited[i][j] = True
        if j + 1 < len(data[i]) and not visited[i][j + 1]:
            distances[i][j + 1] = min(distances[i][j + 1], distances[i][j] + data[i][j + 1])
            node_queue[(i, j + 1)] = distances[i][j + 1]
        if i + 1 < len(data) and not visited[i + 1][j]:
            distances[i + 1][j] = min(distances[i + 1][j], distances[i][j] + data[i + 1][j])
            node_queue[(i + 1, j)] = distances[i + 1][j]
        if j > 0 and not visited[i][j - 1]:
            distances[i][j - 1] = min(distances[i][j - 1], distances[i][j] + data[i][j - 1])
            node_queue[(i, j - 1)] = distances[i][j - 1]
        if i > 0 and not visited[i - 1][j]:
            distances[i - 1][j] = min(distances[i - 1][j], distances[i][j] + data[i - 1][j])
            node_queue[(i - 1, j)] = distances[i - 1][j]

    # for row in distances:
    #     print(row)

    print(distances[-1][-1])
