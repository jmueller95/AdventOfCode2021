def do_cuboids_intersect(x_range1, y_range1, z_range1, x_range2, y_range2, z_range2):
    return ((x_range1[0] <= x_range2[0] <= x_range1[1]) or (x_range2[0] <= x_range1[0] <= x_range2[1])) and \
           ((y_range1[0] <= y_range2[0] <= y_range1[1]) or (y_range2[0] <= y_range1[0] <= y_range2[1])) and \
           ((z_range1[0] <= z_range2[0] <= z_range1[1]) or (z_range2[0] <= z_range1[0] <= z_range2[1]))


def cuboid_intersection(x_range1, y_range1, z_range1, x_range2, y_range2, z_range2):
    return [(max(x_range1[0], x_range2[0]), min(x_range1[1], x_range2[1])),
            (max(y_range1[0], y_range2[0]), min(y_range1[1], y_range2[1])),
            (max(z_range1[0], z_range2[0]), min(z_range1[1], z_range2[1]))]


def cuboid_volume(x_range, y_range, z_range):
    return (x_range[1] + 1 - x_range[0]) * (y_range[1] + 1 - y_range[0]) * (z_range[1] + 1 - z_range[0])


if __name__ == '__main__':
    input = "input.txt"
    positive_cuboids, negative_cuboids = [], []
    with open(input, 'r') as infile:
        for lineno, line in enumerate(infile):
            # print("Processing line {}".format(lineno + 1))
            command, ranges = line.split()
            is_on_command = command == "on"
            x_range, y_range, z_range = [
                (int((rangesplit := r[2:].split(".."))[0]), int(rangesplit[1]))
                for r in ranges.split(",")]
            # print(x_range, y_range, z_range)

            # No matter whether it's an on or an off command: We first add all intersections with positive cuboids
            # as negative cuboids, and all intersections with negative cuboids as positive cuboids.
            # If it is an on command, we then add the entire cube to the list of positive cuboids
            new_positives, new_negatives = [], []
            for other_x_range, other_y_range, other_z_range in positive_cuboids:
                if do_cuboids_intersect(x_range, y_range, z_range, other_x_range, other_y_range, other_z_range):
                    new_negatives.append(cuboid_intersection(
                        x_range, y_range, z_range,
                        other_x_range, other_y_range, other_z_range))
            # Go through list of negative cuboids and add any intersection as a balancing positive cuboid
            for other_x_range, other_y_range, other_z_range in negative_cuboids:
                if do_cuboids_intersect(x_range, y_range, z_range,
                                        other_x_range, other_y_range, other_z_range):
                    new_positives.append(cuboid_intersection(
                        x_range, y_range, z_range,
                        other_x_range, other_y_range, other_z_range))
            if is_on_command:
                new_positives.append([x_range, y_range, z_range])
            positive_cuboids += new_positives
            negative_cuboids += new_negatives

            # print("Positive cuboids: {}".format(positive_cuboids))
            # print("Negative cuboids: {}".format(negative_cuboids))
            # print("{} cubes are turned on".format(sum(cuboid_volume(*cuboid) for cuboid in positive_cuboids) -
            #                                      sum(cuboid_volume(*cuboid) for cuboid in negative_cuboids)))
    # print("----------------------------------")
    print("{} cubes are turned on".format(sum(cuboid_volume(*cuboid) for cuboid in positive_cuboids) -
                                          sum(cuboid_volume(*cuboid) for cuboid in negative_cuboids)))
