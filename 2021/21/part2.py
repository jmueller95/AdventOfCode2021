from collections import defaultdict

if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        position1 = int(infile.readline().strip()[-1])
        position2 = int(infile.readline().strip()[-1])
    """
    Three dice rolls can be anything between 3 and 9, but how often?
    1,1,1 -> 3
    2,1,1, 1,2,1, 1,1,2 -> 4
    2,2,1, 2,1,2, 1,2,2, 1,1,3, 1,3,1, 3,1,1 -> 5
    1,2,3, 1,3,2, 2,1,3, 2,3,1, 3,2,1, 3,1,2, 2,2,2 -> 6
    3,2,2, 2,3,2, 2,2,3, 1,3,3, 3,1,3, 3,3,1 -> 7
    2,3,3, 3,2,3, 3,3,2 -> 8
    3,3,3 -> 9
    """
    # Build a dict with the number of universes in which each player has x points at position y
    points2universes = [defaultdict(int), defaultdict(int)]
    # Initially there is but one universe for each player
    points2universes[0][(0, position1)] = 1
    points2universes[1][(0, position2)] = 1
    # The calculation ends when either player has over 21 points in all of their universes
    wins_one, wins_two = 0, 0
    while sum(points2universes[0].values()) > 0 and sum(points2universes[1].values()) > 0:
        # A turn consists in the addition of 27 new universes for each existing universe
        def take_turn(points2universes):
            res = defaultdict(int)
            wins = 0
            for (score, position), value in points2universes.items():
                for die_sum, n_options in [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]:
                    new_score = (position + die_sum - 1) % 10 + 1
                    if (total_score := score + new_score) < 21:
                        res[(total_score, new_score)] += value * n_options
                    else:
                        wins += value * n_options
            return res, wins


        points2universes[0], new_wins_one = take_turn(points2universes[0])
        # The player has now won new_wins_one times for every universe where the other player has not won yet
        wins_one += new_wins_one * sum(points2universes[1].values())
        points2universes[1], new_wins_two = take_turn(points2universes[1])
        wins_two += new_wins_two * sum(points2universes[0].values())

        print(points2universes[0])
        print(points2universes[1])
        print("Player 1 wins in {} universes.\nPlayer 2 wins in {} universes.".format(wins_one, wins_two))
        print("----------------")
