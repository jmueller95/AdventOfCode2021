import re
if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        data = [l.strip() for l in infile.readlines()]
    print(sum(int(re.search(r'\d', line).group() + re.search(r'\d', line[::-1]).group()) for line in data))