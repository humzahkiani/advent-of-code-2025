

## Part 1 

def parse_input():
    rotations = []

    with open('./input.txt', 'r') as file:
        for line in file:
            direction = line[0]
            distance = int(line[1:])
            rotations.append({
                "direction": direction,
                "distance": distance,
            })

    return rotations

rotations = parse_input()

def part_one(rotations):
    curr_position = 50
    MAX_DIAL = 99

    num_zeroes = 0

    for rotation in rotations:
        direction = rotation["direction"]
        distance = rotation["distance"]

        if direction == "L":
            distance *= -1

        aggregate_sum = curr_position + distance
        new_position = aggregate_sum if 0 <= aggregate_sum <= 99 else aggregate_sum % 100
        
        print(f"P{curr_position} + {distance} -> {new_position} {'YES' if new_position == 0 else '' }")

        if new_position == 0:
            num_zeroes += 1
        
        curr_position = new_position

    print(f"Part 1 - Num times dial on zero: {num_zeroes}")

part_one(rotations)
