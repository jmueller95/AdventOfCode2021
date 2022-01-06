from collections import Counter

if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        scanners = []
        current_beacons = set()
        for line in infile:
            if line.strip() == '':
                scanners.append(current_beacons)
                current_beacons = set()
            elif line.startswith('---'):
                continue
            else:
                current_beacons.add(tuple(int(x) for x in line.strip().split(',')))
        scanners.append(current_beacons)
    # Put beacons from scanners[0] into set of beacons
    all_beacons = scanners[0]
    # By definition, the first scanner sits at the origin
    scanner_positions = [(0, 0, 0)]
    # Iterate scanners[1:] until list is empty

    while len(scanners) > 1:
        # print("{} scanners left".format(len(scanners) - 1))
        for scanner in scanners[1:]:
            # print(scanner)
            # Iterate 24 orientations of scanner i (use sample_input3 for testing)
            scanner_all_orientations = [[[x, y, z],
                                         [x, -y, -z],
                                         [x, z, -y],
                                         [x, -z, y],
                                         [y, x, -z],
                                         [y, -x, z],
                                         [y, z, x],
                                         [y, -z, -x],
                                         [z, x, y],
                                         [z, -x, -y],
                                         [z, y, -x],
                                         [z, -y, x],
                                         [-x, y, -z],
                                         [-x, -y, z],
                                         [-x, z, y],
                                         [-x, -z, -y],
                                         [-y, x, z],
                                         [-y, -x, -z],
                                         [-y, z, -x],
                                         [-y, -z, x],
                                         [-z, x, -y],
                                         [-z, -x, y],
                                         [-z, y, x],
                                         [-z, -y, -x]] for x, y, z in scanner]
            # We need to transpose the matrix that we just got
            scanner_all_orientations = [[scanner_all_orientations[i][j] for i in range(len(scanner_all_orientations))]
                                        for j in range(len(scanner_all_orientations[0]))]
            for reoriented_scanner in scanner_all_orientations:
                # Check if re-oriented beacons of this scanner can be moved so that >=12 overlap with the existing set of beacons
                # To do this, create a list of pairwise distances, check if a difference appears >=12 times
                pairwise_distances = [(x1 - x2, y1 - y2, z1 - z2) for x1, y1, z1 in all_beacons for x2, y2, z2 in
                                      reoriented_scanner]
                # print(pairwise_distances)
                most_common_distance = Counter(pairwise_distances).most_common(1)[0]
                if most_common_distance[1] >= 12:
                    # If that succeeds, add re-oriented beacons to set of beacons
                    all_beacons |= {(x + most_common_distance[0][0],
                                     y + most_common_distance[0][1],
                                     z + most_common_distance[0][2]) for x, y, z in reoriented_scanner}
                    # The position of the scanner is the most common distance itself
                    scanner_positions.append(most_common_distance[0])
                    # Remove scanner from the list
                    scanners.remove(scanner)
    # print(all_beacons)
    # print(len(all_beacons))
    manhattan_distances = [abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)
                           for x1, y1, z1 in scanner_positions
                           for x2, y2, z2 in scanner_positions]
    #print(scanner_positions)
    print(max(manhattan_distances))
