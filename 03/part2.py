def mcb(data, i):
    return sum(row[i] for row in data) / len(data) >= 0.5


if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        data = [[int(bit) for bit in l.strip()] for l in infile.readlines()]

    # OxyGen Rating
    oxy_data = data.copy()
    i = 0
    while len(oxy_data) > 1:
        i_mcb = mcb(oxy_data, i)
        oxy_data = [row for row in oxy_data if row[i] == i_mcb]
        i += 1

    # CO2 Rating
    co2_data = data.copy()
    i = 0
    while len(co2_data) > 1:
        i_mcb = mcb(co2_data, i)
        co2_data = [row for row in co2_data if row[i] != i_mcb]
        i += 1

    print(int("".join([str(x) for x in oxy_data[0]]), 2) *
          int("".join([str(x) for x in co2_data[0]]), 2))
