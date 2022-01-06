from functools import reduce
if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        data = [line.strip() for line in infile]
    chunkmap = {"(": ")", "[": "]", "{": "}", "<": ">"}
    scoremap = {")": 1, "]": 2, "}": 3, ">": 4}
    score_list = []
    for line in data:
        expect_stack = []
        for char in line:
            if char in chunkmap:
                expect_stack.append(chunkmap[char])
            elif expect_stack.pop() != char:
                break
        else:
            score_list.append(reduce(lambda x, y: x*5+scoremap[y], expect_stack[::-1], 0))
    print(sorted(score_list)[len(score_list)//2])
