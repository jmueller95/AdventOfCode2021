from part1 import SnailNumber
from ast import literal_eval

if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        snailNumbers = [SnailNumber(literal_eval(line.strip())) for line in infile]
    pairwise_sums = [(a, b, a.add(b)) for a in snailNumbers for b in snailNumbers]
    pairwise_magnitudes = [(a, b, sum.calc_magnitude()) for a, b, sum in pairwise_sums]
    max_magnitude = max(pairwise_magnitudes, key=lambda x: x[2])
    print("First: {}\nSecond: {}\nMagnitude: {}\nPop Pop!".format(*max_magnitude))
