if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        data = [line.strip() for line in infile]
    chunkmap = {"(": ")", "[": "]", "{": "}", "<": ">"}
    scoremap = {")": 3, "]": 57, "}": 1197, ">": 25137}
    score = 0
    for line in data:
        expect_stack = []
        for char in line:
            if char in chunkmap:
                expect_stack.append(chunkmap[char])
            else:
                expected_closing_char = expect_stack.pop()
                if char != expected_closing_char:
                    score += scoremap[char]
    print(score)
