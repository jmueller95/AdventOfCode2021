"""I wrote this after some hours of trying to solve this manually and getting frustrated.
It's not very performant (takes 10-15 mins to complete),
and since it's brute force there's probably a more efficient way, but it works.
"""


def print_board(hallway, rooms, counter):
    print('#' * 13)
    print('#{}#'.format("".join(amphipod if amphipod else '.' for amphipod in hallway)))
    for i in range(4):
        print('###{}#{}#{}#{}###'.format(*[room[i] if room[i] else '.' for room in rooms]))
    print('#' * 13)
    for key, value in counter.items():
        print("{}: {}".format(key, value))


def is_move_from_hallway_legit(hallway, rooms, starting_position, room_destination):
    room_destination_relative_to_hallway = (room_destination + 1) * 2
    # It has already been checked that the amphipod at starting_position belongs into that room
    # There must be no wrong amphipods in that room and the way must be free
    return all(amphipod in [None, hallway[starting_position]] for amphipod in rooms[room_destination]) and (
            (room_destination_relative_to_hallway > starting_position
             and all(not amphipod for amphipod in
                     hallway[starting_position + 1:room_destination_relative_to_hallway + 1])) or
            (room_destination_relative_to_hallway < starting_position
             and all(not amphipod for amphipod in hallway[room_destination_relative_to_hallway:starting_position])))


def is_move_from_room_legit(hallway, starting_room, hallway_destination):
    starting_room_relative_to_hallway = (starting_room + 1) * 2
    if hallway_destination > starting_room_relative_to_hallway:
        return all(
            not amphipod for amphipod in hallway[starting_room_relative_to_hallway:hallway_destination + 1])
    else:
        return all(
            not amphipod for amphipod in hallway[hallway_destination:starting_room_relative_to_hallway + 1])


def is_solved(hallway, rooms):
    return all(not amphipod for amphipod in hallway) and \
           all(sum(amphipod == expected_type for amphipod in rooms[i]) == 4
               for i, expected_type in zip(range(4), ['A', 'B', 'C', 'D']))


if __name__ == '__main__':
    input = "input2.txt"
    # The hallway always looks the same initially
    hallway = [None for _ in range(11)]
    rooms = [[], [], [], []]
    amphipod_type_to_room = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    room_to_amphipod_type = {value: key for key, value in amphipod_type_to_room.items()}
    with open(input, 'r') as infile:
        # Discard first two lines
        infile.readline()
        infile.readline()
        for _ in range(4):
            line = infile.readline()
            # Now only characters 3,5,7,9 are interesting
            rooms[0].append(line[3])
            rooms[1].append(line[5])
            rooms[2].append(line[7])
            rooms[3].append(line[9])
        move_counter = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'Total': 0, 'Turns': 0}
        rooms_emptied = [False, False, False, False]
    # A 'situation' consists in the configuration of hallway and room, the count of moves of each amphipod type
    # and the information which rooms have already been emptied at some point (because from those rooms it is not possible
    # to move out)
    possible_situations = [(hallway, rooms, move_counter, rooms_emptied)]
    solutions = []
    iteration = 0
    while possible_situations:
        new_possible_situations = []
        for hallway, rooms, move_counter, rooms_emptied in possible_situations:
            if is_solved(hallway, rooms):
                solutions.append(move_counter)
                print("Solution found: {}".format(move_counter))
                continue
            # Get all possible moves and check which are allowed
            for starting_position, amphipod in enumerate(hallway):
                if amphipod and is_move_from_hallway_legit(hallway, rooms, starting_position,
                                                           (room_destination := amphipod_type_to_room[amphipod])):
                    # Create a new situation
                    new_hallway = hallway.copy()
                    new_rooms = [room.copy() for room in rooms]
                    new_move_counter = move_counter.copy()
                    new_rooms_emptied = rooms_emptied.copy()
                    # Check which position in the room the amphipod would end up in
                    position_in_room = max(
                        j for j, amphipod in enumerate(new_rooms[room_destination]) if not amphipod)
                    # Calculate the distance and increase the respective counters
                    distance = position_in_room + 1 + abs((room_destination + 1) * 2 - starting_position)
                    new_move_counter[amphipod] += distance
                    new_move_counter['Total'] += distance * (10 ** amphipod_type_to_room[amphipod])
                    new_move_counter['Turns'] += 1
                    # Actually move the amphipod
                    new_rooms[room_destination][position_in_room] = amphipod
                    new_hallway[starting_position] = None
                    # Check if the situation already exists - will increase runtime a lot, but maybe avoid a RAM explosion
                    for i in range(len(new_possible_situations)):
                        existing_hallway, existing_rooms, existing_move_counter, existing_rooms_emptied = \
                            new_possible_situations[i]
                        if new_hallway == existing_hallway and new_rooms == existing_rooms:
                            if existing_move_counter['Total'] > new_move_counter['Total']:
                                new_possible_situations[i] = (existing_hallway, existing_rooms,
                                                              new_move_counter, existing_rooms_emptied)
                            break
                    else:
                        new_possible_situations.append((new_hallway, new_rooms, new_move_counter, new_rooms_emptied))
            # Now do the same thing for the four rooms... need to check every possible destination!
            for room_index, room in enumerate(rooms):
                # A room that has once been emptied can only be filled, nothing can exit it again
                # This prevents amphipods from endlessly jumping in and out of a room
                if rooms_emptied[room_index]:
                    continue
                # Get the uppermost amphipod in the room, if any
                if all(not amphipod for amphipod in room):
                    continue
                starting_position = min(j for j, amphipod in enumerate(room) if amphipod)
                for hallway_destination in [0, 1, 3, 5, 7, 9, 10]:
                    if is_move_from_room_legit(hallway, room_index, hallway_destination):
                        # Create a new situation
                        new_hallway = hallway.copy()
                        new_rooms = [room.copy() for room in rooms]
                        new_move_counter = move_counter.copy()
                        new_rooms_emptied = rooms_emptied.copy()
                        # Calculate the distance and increase the respective counters
                        distance = starting_position + 1 + abs((room_index + 1) * 2 - hallway_destination)
                        new_move_counter[room[starting_position]] += distance
                        new_move_counter['Total'] += distance * (10 ** amphipod_type_to_room[room[starting_position]])
                        new_move_counter['Turns'] += 1
                        # Actually move the amphipod
                        new_hallway[hallway_destination] = new_rooms[room_index][starting_position]
                        new_rooms[room_index][starting_position] = None
                        if all(amphipod in [None, room_to_amphipod_type[room_index]]
                               for amphipod in new_rooms[room_index]):
                            new_rooms_emptied[room_index] = True
                        # Check if the situation already exists - will increase runtime a lot, but maybe avoid a RAM explosion
                        for i in range(len(new_possible_situations)):
                            existing_hallway, existing_rooms, existing_move_counter, existing_rooms_emptied = \
                                new_possible_situations[i]
                            if new_hallway == existing_hallway and new_rooms == existing_rooms:
                                if existing_move_counter['Total'] > new_move_counter['Total']:
                                    new_possible_situations[i] = (existing_hallway, existing_rooms,
                                                                  new_move_counter, existing_rooms_emptied)
                                break
                        else:
                            new_possible_situations.append(
                                (new_hallway, new_rooms, new_move_counter, new_rooms_emptied))
        possible_situations = new_possible_situations
        iteration += 1
        # print("{} possible situations, {} solutions.".format(len(possible_situations), len(solutions)))
        print("{}: {} possible situations, {} solutions.".format(iteration, len(possible_situations), len(solutions)))
    print("\n-------------------------\n")
    for counter in solutions:
        for key, value in counter.items():
            print("{}: {}".format(key, value))
        print("\n-------------------------\n")
    # for hallway, rooms, move_counter in possible_situations:
    # print_board(hallway, rooms, move_counter)
    # print("-------------------------------------")
