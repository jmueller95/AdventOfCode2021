if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        data = [int(x) for x in infile.readline().split(",")]

    fish_per_phase = {phase: data.count(phase) for phase in range(9)}
    for day in range(256):
        # print("Days: {}, fish: {}".format(day, sum(fish_per_phase.values())))
        # print(fish_per_phase)
        for i in range(-1, 8):
            fish_per_phase[i] = fish_per_phase[i + 1]
        fish_per_phase[6] += fish_per_phase[-1]
        fish_per_phase[8] = fish_per_phase[-1]
        fish_per_phase[-1] = 0
    print(sum(fish_per_phase.values()))
