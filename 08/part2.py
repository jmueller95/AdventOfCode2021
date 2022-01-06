from collections import Counter

if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        data = [((linesplit := line.split())[:10], linesplit[11:]) for line in infile]
    result = 0
    for line in data:
        # Part 1: Figure out the mapping between wires and segments
        segments = set("abcdefg")
        possible_wirings = {wire: segments.copy() for wire in segments}
        for signal in line[0] + line[1]:
            signal = set(signal)
            # print(signal)
            if len(signal) == 2:
                # It's a 1, so c and f should be on.
                possible_wirings['c'] &= signal
                possible_wirings['f'] &= signal
            elif len(signal) == 3:
                # It's a 7, so it's a, c and f
                possible_wirings['a'] &= signal
                possible_wirings['c'] &= signal
                possible_wirings['f'] &= signal
            elif len(signal) == 4:
                # It's a 4, so it's b,c,d, and f
                possible_wirings['b'] &= signal
                possible_wirings['c'] &= signal
                possible_wirings['d'] &= signal
                possible_wirings['f'] &= signal
            elif len(signal) == 5:
                # It's either 2, 3, or 5, so it's anything... only info is that it cannot be b AND e at the same time
                pass
            elif len(signal) == 6:
                # It's a 0, a 6, or a 9, so it's anything.
                pass
            elif len(signal) == 7:
                # It's an 8, which yields no information
                pass

        # Now the dirty part:
        # a contains three values right now, which are for segments a, c, or f. So remove these three from all others
        possible_wirings['b'] -= possible_wirings['a']
        possible_wirings['d'] -= possible_wirings['a']
        possible_wirings['e'] -= possible_wirings['a']
        possible_wirings['g'] -= possible_wirings['a']

        # a gets subtracted by b (or f), which figures its value out (b+f=1, a+b+f=7)
        possible_wirings['a'] -= possible_wirings['b']

        # Consider the three signals of length 5. b and e should appear once, c and f twice, a, d and g thrice
        len_5_counter = Counter("".join({signal for signal in line[0] if len(signal) == 5}))
        b_or_e = {key for key, value in len_5_counter.items() if value == 1}
        possible_wirings['b'] &= b_or_e
        possible_wirings['e'] &= b_or_e

        c_or_f = {key for key, value in len_5_counter.items() if value == 2}
        possible_wirings['c'] &= c_or_f
        possible_wirings['f'] &= c_or_f

        a_or_d_or_g = {key for key, value in len_5_counter.items() if value == 3}
        possible_wirings['a'] &= a_or_d_or_g
        possible_wirings['d'] &= a_or_d_or_g
        possible_wirings['g'] &= a_or_d_or_g

        # Consider the three signals of length 6. c,d,e appear twice, a,b,f,g thrice
        len_6_counter = Counter("".join({signal for signal in line[0] if len(signal) == 6}))
        cde = {key for key, value in len_6_counter.items() if value == 2}
        possible_wirings['c'] &= cde
        possible_wirings['d'] &= cde
        possible_wirings['e'] &= cde

        abfg = {key for key, value in len_6_counter.items() if value == 3}
        possible_wirings['a'] &= abfg
        possible_wirings['b'] &= abfg
        possible_wirings['f'] &= abfg
        possible_wirings['g'] &= abfg

        mapping = str.maketrans({value.pop(): key for key, value in possible_wirings.items()})
        # Part 2: Translate the output value into the proper segments and decode it
        output_digits = ""
        for output_signal in line[1]:
            output_signal_translated = set(output_signal.translate(mapping))
            if output_signal_translated == {"a", "b", "c", "e", "f", "g"}:
                output_digits += "0"
            elif output_signal_translated == {"c", "f"}:
                output_digits += "1"
            elif output_signal_translated == {"a", "c", "d", "e", "g"}:
                output_digits += "2"
            elif output_signal_translated == {"a", "c", "d", "f", "g"}:
                output_digits += "3"
            elif output_signal_translated == {"b", "c", "d", "f"}:
                output_digits += "4"
            elif output_signal_translated == {"a", "b", "d", "f", "g"}:
                output_digits += "5"
            elif output_signal_translated == {"a", "b", "d", "e", "f", "g"}:
                output_digits += "6"
            elif output_signal_translated == {"a", "c", "f"}:
                output_digits += "7"
            elif output_signal_translated == {"a", "b", "c", "d", "e", "f", "g"}:
                output_digits += "8"
            elif output_signal_translated == {"a", "b", "c", "d", "f", "g"}:
                output_digits += "9"
        output_digits = int(output_digits)
        result += output_digits
    print(result)
