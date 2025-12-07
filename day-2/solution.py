
## Part 1 

def parse_input():
    rotations = []

    with open('./input.txt', 'r') as file:
        ranges = []
        for line in file:
            substrings = line.split(",")
            for substr in substrings:
                left_boundary,right_boundary = map(lambda x: int(x), substr.split("-"))
                ranges.append([left_boundary,right_boundary])

    return ranges

def is_invalid(id):
    str_id = str(id)
    num_digits = len(str_id)
    if num_digits % 2 != 0:
        return False

    first_half = str_id[0:num_digits//2]
    second_half = str_id[num_digits//2:]

    if first_half == second_half:
        return True

    return False


print(f"{is_invalid(123123)} = True")
print(f"{is_invalid(11122)} = False")
print(f"{is_invalid(1)} = False")
print(f"{is_invalid(11)} = True")
print(f"{is_invalid(12)} = False")

def part_one():
    ranges = parse_input()

    invalid_id_sum = 0

    for rang in ranges:
        for id in range(rang[0],rang[1]+1):
            if is_invalid(id):
                invalid_id_sum += id

    return invalid_id_sum

print(f"Part 1 - The sum of the invalid ids is {part_one()}")


