

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
    MAX_DIAL = 99
    curr_position = 50
    num_zeroes = 0

    for rotation in rotations:
        direction = rotation["direction"]
        distance = rotation["distance"]

        if direction == "L":
            distance *= -1

        aggregate_dist = curr_position + distance
        new_position = aggregate_dist if 0 <= aggregate_dist <= 99 else aggregate_dist % (MAX_DIAL+1)

        if new_position == 0:
            num_zeroes += 1
        
        curr_position = new_position

    print(f"Part 1 - Num times landed on zero: {num_zeroes}")

part_one(rotations)
import math

def part_two(rotations, curr_position=50):
    MAX_DIAL = 99
    total_zeroes = 0

    for rotation in rotations:
        direction = rotation["direction"]
        distance = rotation["distance"]
        distance_vector = distance * -1 if direction == "L" else distance

        aggregate_dist = curr_position + distance_vector 
        start = curr_position
        end = aggregate_dist % (MAX_DIAL+1) 

        num_zeroes = 0
        num_zeroes += (distance // 100)

        if distance // 100 == distance / 100:
            total_zeroes += num_zeroes
            curr_position = end
            continue

        if direction == "L" and ((start < end and start != 0) or end == 0):
            num_zeroes += 1
        if direction == "R" and start > end:
            num_zeroes += 1

        total_zeroes += num_zeroes
        curr_position = end


    return total_zeroes


part_two_test_cases = [
    [0,{"direction":"R","distance":35},0],
    [0,{"direction":"R","distance":100},1],
    [0,{"direction":"R","distance":135},1],
    [0,{"direction":"R","distance":300},3],
    [0,{"direction":"R","distance":335},3],
    [0,{"direction":"L","distance":35},0],
    [0,{"direction":"L","distance":100},1],
    [0,{"direction":"L","distance":135},1],
    [0,{"direction":"L","distance":300},3],
    [0,{"direction":"L","distance":335},3],
    [30,{"direction":"R","distance":35},0],
    [30,{"direction":"R","distance":70},1],
    [30,{"direction":"R","distance":100},1],
    [30,{"direction":"R","distance":135},1],
    [30,{"direction":"R","distance":300},3],
    [30,{"direction":"R","distance":335},3],
    [30,{"direction":"L","distance":35},1],
    [30,{"direction":"L","distance":30},1],
    [30,{"direction":"L","distance":100},1],
    [30,{"direction":"L","distance":130},2],
    [30,{"direction":"L","distance":135},2],
    [30,{"direction":"L","distance":300},3],
    [30,{"direction":"L","distance":335},4]
]

def run_part_two_tests(test_cases):
    total_tests = len(test_cases)
    failed_tests = 0

    for test in test_cases:
        print("-----------------------------------------------")
        expected = test[2]
        actual = part_two([test[1]],test[0])
        if actual != expected:
            print(f"[TEST FAILED] P{test[0]} + {test[1]["direction"]}{test[1]["distance"]}")
            failed_tests += 1
        else:
            print(f"[TEST SUCCESS] P{test[0]} + {test[1]["direction"]}{test[1]["distance"]}")
        print(f"num_zeroes -  expected:{expected} zeroes, actual:{actual} zeroes")
        print("-----------------------------------------------")

    print(f"{failed_tests}/{total_tests} tests failed")

# run_part_two_tests(part_two_test_cases)

print(f"Part 2 - Num zeroes clicked thru {part_two(rotations)}")


