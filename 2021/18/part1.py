from ast import literal_eval
from math import floor, ceil
import functools
from copy import deepcopy


class SnailNumber:
    def __init__(self, pair):
        self.left = SnailNumber(pair[0]) if isinstance(pair[0], list) else pair[0]
        self.right = SnailNumber(pair[1]) if isinstance(pair[1], list) else pair[1]

    def getAllPathsDeeperThan(self, n):
        res = ['']
        if isinstance(self.left, SnailNumber):
            res += ['l' + p for p in self.left.getAllPathsDeeperThan(n - 1)]
        if isinstance(self.right, SnailNumber):
            res += ['r' + p for p in self.right.getAllPathsDeeperThan(n - 1)]
        return [p for p in res if len(p) >= n]

    def getAllPathsToNumbersGreaterThan10(self):
        res = []
        if isinstance(self.left, int) and self.left >= 10:
            res += ['l']
        if isinstance(self.right, int) and self.right >= 10:
            res += ['r']
        if isinstance(self.left, SnailNumber):
            res += ['l' + p for p in self.left.getAllPathsToNumbersGreaterThan10()]
        if isinstance(self.right, SnailNumber):
            res += ['r' + p for p in self.right.getAllPathsToNumbersGreaterThan10()]
        return res

    def add(self, other):
        res = SnailNumber([deepcopy(self), deepcopy(other)])
        res.reduce()
        return res

    def follow_path(self, path):
        current_number = self
        for letter in path:
            if isinstance(current_number, int):
                return None
            else:
                current_number = current_number.left if letter == 'l' else current_number.right
        return current_number

    def findRightNeighbor(self, path):
        # To obtain the path to a number's right neighbour,
        # swap the last 'l' in the number's path to an r, drop the rest of the path
        # then follow that path and from there, go to the leftmost 'leaf'
        # If there is no l in the number's path, it has no right neighbour.
        last_l = path.rfind('l')
        if last_l == -1:
            return None
        else:
            res = path[:last_l] + 'r'
            current_number = self.follow_path(res)
            while isinstance(current_number, SnailNumber):
                res += 'l'
                current_number = current_number.left
            return res

    def findLeftNeighbor(self, path):
        last_r = path.rfind('r')
        if last_r == -1:
            return None
        else:
            res = path[:last_r] + 'l'
            current_number = self.follow_path(res)
            while isinstance(current_number, SnailNumber):
                res += 'r'
                current_number = current_number.right
            return res

    def explode(self, path):
        numberToExplode = self.follow_path(path)
        # print("Exploding: {}".format(numberToExplode))
        pathToRightNeighbor = self.findRightNeighbor(path)
        if pathToRightNeighbor:
            parentOfRightNeighbor = self.follow_path(pathToRightNeighbor[:-1])
            # print("Parent of Right Neighbor is: {}".format(parentOfRightNeighbor))
            if pathToRightNeighbor[-1] == 'l':
                parentOfRightNeighbor.left += numberToExplode.right
            else:
                parentOfRightNeighbor.right += numberToExplode.right
            # print("Parent of Right Neighbor is: {}".format(parentOfRightNeighbor))
        pathToLeftNeighbor = self.findLeftNeighbor(path)
        if pathToLeftNeighbor:
            parentOfLeftNeighbor = self.follow_path(pathToLeftNeighbor[:-1])
            # print("Parent of left Neighbor is: {}".format(parentOfLeftNeighbor))
            if pathToLeftNeighbor[-1] == 'r':
                parentOfLeftNeighbor.right += numberToExplode.left
            else:
                parentOfLeftNeighbor.left += numberToExplode.left
            # print("Parent of left Neighbor is: {}".format(parentOfLeftNeighbor))
        parentOfExploder = self.follow_path(path[:-1])
        if path[-1] == 'r':
            parentOfExploder.right = 0
        else:
            parentOfExploder.left = 0

    def split(self, path):
        parentOfSplitter = self.follow_path(path[:-1])
        if path[-1] == 'l':
            parentOfSplitter.left = SnailNumber([floor(parentOfSplitter.left / 2), ceil(parentOfSplitter.left / 2)])
        else:
            parentOfSplitter.right = SnailNumber([floor(parentOfSplitter.right / 2), ceil(parentOfSplitter.right / 2)])

    def reduce(self):
        paths_to_explode = self.getAllPathsDeeperThan(4)
        if paths_to_explode:
            # To get the leftmost path of a list of path, just take the minimum because l < r
            leftmost_path_to_explode = min(paths_to_explode)
            self.explode(leftmost_path_to_explode)
            self.reduce()
        else:
            paths_to_greatness = self.getAllPathsToNumbersGreaterThan10()
            if paths_to_greatness:
                leftmost_path_to_greatness = min(paths_to_greatness)
                self.split(leftmost_path_to_greatness)
                self.reduce()

    def calc_magnitude(self):
        return 3 * (self.left.calc_magnitude() if isinstance(self.left, SnailNumber) else self.left) + \
               2 * (self.right.calc_magnitude() if isinstance(self.right, SnailNumber) else self.right)

    def __str__(self):
        return "[{},{}]".format(self.left, self.right)


if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        snailNumbers = [SnailNumber(literal_eval(line.strip())) for line in infile]
    sum = functools.reduce(lambda x, y: x.add(y), snailNumbers[1:], snailNumbers[0])
    print(sum)
    print(sum.calc_magnitude())
