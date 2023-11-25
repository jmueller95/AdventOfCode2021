if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        data = [[int(bit) for bit in l.strip()] for l in infile.readlines()]
    # Transpose resulting matrix
    data_t = [[data[i][j] for i in range(len(data))] for j in range(len(data[0]))]
    gamma_rate_bin = "".join(["1" if sum(row) / len(row) > 0.5 else "0" for row in data_t])
    epsilon_rate_bin = "".join(["1" if gamma_rate_bin[i] == "0" else "0" for i in range(len(gamma_rate_bin))])
    print(int(gamma_rate_bin, 2) * int(epsilon_rate_bin, 2))
