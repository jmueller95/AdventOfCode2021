"""Inspired by https://github.com/AllanTaylor314/AdventOfCode/blob/main/2021/23.py
Using a cache, my original solution can be obtained in a few seconds. The only thing I needed to do for that was make
a 'situation' hashable, so I threw out the count dictionary (storing the full cost is enough) and converted hallway
and rooms to tuples (bc lists and dicts are not hashable, but tuples are). This solution now also returns the sequence
of situations that leads to the optimal solution.
Really fascinating how caching makes this so much faster.
"""
from functools import cache


def print_board(hallway, rooms):
    print('#' * 13)
    print('#{}#'.format("".join(amphipod if amphipod else '.' for amphipod in hallway)))
    for i in range(4):
        print('###{}#{}#{}#{}###'.format(*[room[i] if room[i] else '.' for room in rooms]))
    print('#' * 13)


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


@cache
def steps_to_final(situation):
    hallway, rooms = situation
    if is_solved(hallway, rooms):
        return 0, [situation]
    possible_costs = [(float('inf'), [situation])]

    # Check hallway for possible moves
    for starting_position, amphipod in enumerate(hallway):
        if amphipod and is_move_from_hallway_legit(hallway, rooms, starting_position,
                                                   (room_destination := amphipod_type_to_room[amphipod])):
            # Check which position in the room the amphipod would end up in
            position_in_room = max(
                j for j, amphipod in enumerate(rooms[room_destination]) if not amphipod)

            # Create a new situation
            new_hallway = hallway[:starting_position] + (None,) + hallway[starting_position + 1:]
            new_rooms = rooms[:room_destination] + \
                        tuple((rooms[room_destination][:position_in_room] + (amphipod,)
                               + rooms[room_destination][position_in_room + 1:],)) + \
                        rooms[room_destination + 1:]
            # Calculate the cost
            distance = position_in_room + 1 + abs((room_destination + 1) * 2 - starting_position)
            cost = distance * (10 ** amphipod_type_to_room[amphipod])

            remaining_cost, remaining_path = steps_to_final((new_hallway, new_rooms))
            possible_costs.append((cost + remaining_cost, [situation] + remaining_path))

    for room_index, room in enumerate(rooms):
        # A room that has once been emptied can only be filled, nothing can exit it again
        # This prevents amphipods from endlessly jumping in and out of a room
        if all(amphipod in [None, room_to_amphipod_type[room_index]] for amphipod in rooms[room_index]):
            continue
        # Get the uppermost amphipod in the room, if any
        if all(not amphipod for amphipod in room):
            continue
        starting_position = min(j for j, amphipod in enumerate(room) if amphipod)
        for hallway_destination in [0, 1, 3, 5, 7, 9, 10]:
            if is_move_from_room_legit(hallway, room_index, hallway_destination):
                # Create a new situation
                new_hallway = hallway[:hallway_destination] + \
                              (rooms[room_index][starting_position],) + \
                              hallway[hallway_destination + 1:]
                new_rooms = rooms[:room_index] + \
                            tuple((rooms[room_index][:starting_position] + (None,)
                                   + rooms[room_index][starting_position + 1:],)) + \
                            rooms[room_index + 1:]
                distance = starting_position + 1 + abs((room_index + 1) * 2 - hallway_destination)
                cost = distance * (10 ** amphipod_type_to_room[room[starting_position]])

                # possible_costs.append(cost + steps_to_final((new_hallway, new_rooms)))
                remaining_cost, remaining_path = steps_to_final((new_hallway, new_rooms))
                possible_costs.append((cost + remaining_cost, [situation] + remaining_path))

    return min(possible_costs, key=lambda t: t[0])


if __name__ == '__main__':
    input = "input2.txt"
    # The hallway always looks the same initially
    hallway = tuple(None for _ in range(11))
    rooms = tuple()
    roomA, roomB, roomC, roomD = tuple(), tuple(), tuple(), tuple()
    amphipod_type_to_room = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    room_to_amphipod_type = {value: key for key, value in amphipod_type_to_room.items()}
    with open(input, 'r') as infile:
        # Discard first two lines
        infile.readline()
        infile.readline()
        for _ in range(4):
            line = infile.readline()
            # Now only characters 3,5,7,9 are interesting
            roomA += (line[3],)
            roomB += (line[5],)
            roomC += (line[7],)
            roomD += (line[9],)
    rooms += tuple((roomA,))
    rooms += tuple((roomB,))
    rooms += tuple((roomC,))
    rooms += tuple((roomD,))

    situation0 = (tuple(hallway), tuple(tuple(room) for room in rooms))
    cost, path = steps_to_final(situation0)
    for hallway, rooms in path:
        if hallway and rooms:
            print_board(hallway, rooms)
            print("------------------------")
    print("Total Cost: {}".format(cost))
