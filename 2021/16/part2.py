from math import prod


def decode_literal_value(val):
    res = ''
    for i in range(0, len(val), 5):
        res += val[i + 1:i + 5]
        if val[i] == '0':
            i += 5
            return res, i


def evaluate_subpackets(values, type_id):
    print(values)
    print(type_id)
    if type_id == 0:
        return sum(values)
    elif type_id == 1:
        return prod(values)
    elif type_id == 2:
        return min(values)
    elif type_id == 3:
        return max(values)
    elif type_id == 5:
        return int(values[0] > values[1])
    elif type_id == 6:
        return int(values[0] < values[1])
    elif type_id == 7:
        return int(values[0] == values[1])


def decode_packet(packet):
    if len(packet) == 0 or int(packet, 2) == 0:
        return 0, len(packet)
    packet_type_id = int(packet[3:6], 2)
    if packet_type_id == 4:
        literal_number_string, packet_end_index = decode_literal_value(packet[6:])
        return int(literal_number_string, 2), packet_end_index + 6  # Add  6 for the header offset
    else:
        subpacket_values = []
        length_type_id = packet[6]
        if length_type_id == '0':
            length_of_subpackets = int(packet[7:22], 2)
            current_subpacket_start_index = 22
            while current_subpacket_start_index < (22 + length_of_subpackets):
                subpacket_value, start_index_offset = decode_packet(packet[current_subpacket_start_index:])
                subpacket_values.append(subpacket_value)
                current_subpacket_start_index += start_index_offset
            return evaluate_subpackets(subpacket_values, packet_type_id), current_subpacket_start_index
        else:
            number_of_subpackets = int(packet[7:18], 2)
            current_subpacket_start_index = 18
            for i in range(number_of_subpackets):
                subpacket_value, start_index_offset = decode_packet(packet[current_subpacket_start_index:])
                subpacket_values.append(subpacket_value)
                current_subpacket_start_index += start_index_offset
            return evaluate_subpackets(subpacket_values, packet_type_id), current_subpacket_start_index


if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        input_binary = ''
        input_hex = infile.readline().strip()
    for hex_number in input_hex:
        # This first converts hex to integer, then integer to 4-bit padded binary
        input_binary += format(int(hex_number, 16), '04b')
    packet_value, _ = decode_packet(input_binary)
    print("Value of the packet: {}".format(packet_value))

    # print(input_binary)
