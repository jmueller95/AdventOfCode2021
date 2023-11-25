if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        position1 = int(infile.readline().strip()[-1])
        position2 = int(infile.readline().strip()[-1])
    score1, score2 = 0, 0
    # Initial -3 because the first roll should give 6 and we always add 9
    deterministic_die_sum = -3
    n_rolls = 0
    while score2 < 1000:
        deterministic_die_sum = ((deterministic_die_sum + 8) % 10) + 1
        n_rolls += 3
        position1 = ((position1 + deterministic_die_sum - 1) % 10) + 1
        score1 += position1
        if score1 >= 1000:
            break
        deterministic_die_sum = ((deterministic_die_sum + 8) % 10) + 1
        n_rolls += 3
        position2 = ((position2 + deterministic_die_sum - 1) % 10) + 1
        score2 += position2

    print("A player has won."
          "\nThe losing player has {} points."
          "\nThe die was rolled {} times"
          "\nSolution: {}".format(min(score1, score2), n_rolls, min(score1, score2) * n_rolls))
