from collections import defaultdict

if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        template = infile.readline().strip()
        first, last = template[0], template[-1]
        tuple_dict = defaultdict(int)
        for i in range(len(template) - 1):
            tuple_dict[template[i:i + 2]] += 1

        infile.readline()
        rules = {(rule := line.strip().split(" -> "))[0]:
                     (rule[0][0] + rule[1], rule[1] + rule[0][1]) for line in infile}
        # print(rules)

    for n in range(40):
        # print(tuple_dict)
        new_tuple_dict = defaultdict(int)
        for tuple in tuple_dict.keys():
            if tuple in rules:
                new_tuple_dict[rules[tuple][0]] += tuple_dict[tuple]
                new_tuple_dict[rules[tuple][1]] += tuple_dict[tuple]
        tuple_dict = new_tuple_dict

    elem_counter = defaultdict(int)
    elem_counter[first] += 1
    elem_counter[last] += 1
    for tuple, count in tuple_dict.items():
        elem_counter[tuple[0]] += count
        elem_counter[tuple[1]] += count
    elem_counter = {key: int(value / 2) for key, value in elem_counter.items()}

    for elem, count in elem_counter.items():
        print("{}: {}".format(elem, count))
    print(max(elem_counter.values()) - min(elem_counter.values()))
