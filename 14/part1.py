from collections import Counter

if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        template = infile.readline().strip()
        infile.readline()
        rules = {(rule := line.strip().split(" -> "))[0]: rule[1] for line in infile}
    for n in range(10):
        print(template)
        new_template = ""
        for i in range(len(template) - 1):
            new_template += template[i] + rules[template[i:i + 2]] if template[i:i + 2] in rules else template[i]
        template = new_template + template[-1]
    elem_counter = Counter(template)
    # max_elem = max(elem_counter, key=lambda elem: elem_counter[elem])
    # min_elem = min(elem_counter, key=lambda elem: elem_counter[elem])
    print(max(elem_counter.values()) - min(elem_counter.values()))
