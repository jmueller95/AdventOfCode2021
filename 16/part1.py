VERSION_SUM = 0


def decode_literal_value(val):
    res = ''
    for i in range(0, len(val), 5):
        res += val[i + 1:i + 5]
        if val[i] == '0':
            i += 5
            return res, i


def decode_packet(packet):
    if len(packet) == 0 or int(packet, 2) == 0:
        print("------------------------\nPacket ({}) is empty. Nothing to do.".format(packet))
        return len(packet)
    print("------------------------\nNow decoding packet: {}".format(packet))
    global VERSION_SUM
    packet_version = int(packet[:3], 2)
    VERSION_SUM += packet_version
    packet_type_id = int(packet[3:6], 2)
    print("Version: {}, Type_ID: {}".format(packet_version, packet_type_id))
    print("Running sum: {}".format(VERSION_SUM))
    if packet_type_id == 4:
        literal_number_string, packet_end_index = decode_literal_value(packet[6:])
        print("Literal Number: {}".format(int(literal_number_string, 2)))
        print("Remainder after literal: {}".format(packet[packet_end_index + 6:]))
        return packet_end_index + 6  # Add  6 for the header offset
    else:
        length_type_id = packet[6]
        if length_type_id == '0':
            length_of_subpackets = int(packet[7:22], 2)
            print("Length of subpackets: {}".format(length_of_subpackets))
            current_subpacket_start_index = 22
            while current_subpacket_start_index < (22 + length_of_subpackets):
                print("Length of subpackets: {}".format(length_of_subpackets))
                current_subpacket_start_index += decode_packet(
                    packet[current_subpacket_start_index:])
            print("Remainder after length mode: {}".format(packet[current_subpacket_start_index:]))
            return current_subpacket_start_index
        else:
            number_of_subpackets = int(packet[7:18], 2)
            print("Number of subpackets: {}".format(number_of_subpackets))
            current_subpacket_start_index = 18
            for i in range(number_of_subpackets):
                current_subpacket_start_index += decode_packet(packet[current_subpacket_start_index:])
            print("Remainder after number mode: {}".format(packet[current_subpacket_start_index:]))
            return current_subpacket_start_index


if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        input_binary = ''
        for hex_number in infile.readline().strip():
            # This first converts hex to integer, then integer to 4-bit padded binary
            input_binary += format(int(hex_number, 16), '04b')
    decode_packet(input_binary)
    print("------------------------\nVersion Sum: {}".format(VERSION_SUM))

    # print(input_binary)
