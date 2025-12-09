
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

    return first_half == second_half

# print(f"{is_invalid(123123)} = True")
# print(f"{is_invalid(11122)} = False")
# print(f"{is_invalid(1)} = False")
# print(f"{is_invalid(11)} = True")
# print(f"{is_invalid(12)} = False")

def part_one():
    ranges = parse_input()

    invalid_id_sum = 0

    for rang in ranges:
        for id in range(rang[0],rang[1]+1):
            if is_invalid(id):
                invalid_id_sum += id

    return invalid_id_sum

print(f"Part 1 - The sum of the invalid ids is {part_one()}")

# Part 2

def part_two():
    ranges = parse_input()
    invalid_id_sum = 0

    for rang in ranges:
        for id in range(rang[0],rang[1]+1):
            if is_invalid(id):
                invalid_id_sum += id

    return invalid_id_sum


def can_be_divided_into_n_equal_chunks(id, length, n):
    str_id = str(id)

    chunk_size, remainder = divmod(length, n)
    if remainder != 0:
        return False

    chunks_idx = [[x,x+chunk_size] for x in range(0,length,chunk_size)]
    unique_chunks = set()
    for left,right in chunks_idx:
        chunk = str_id[left:right]
        unique_chunks.add(chunk)

    return False if len(unique_chunks) > 1 else True


def is_invalid(id):
    str_id = str(id)
    num_digits = len(str_id)

    for divisions in range(2,num_digits+1):
        if can_be_divided_into_n_equal_chunks(id, num_digits, divisions):
            return True

    return False


print(f"Part 2 - The sum of the invalid ids is {part_two()}")

# print(f"{is_invalid(123123)} = True")
# print(f"{is_invalid(11122)} = False")
# print(f"{is_invalid(1)} = False")
# print(f"{is_invalid(11)} = True")
# print(f"{is_invalid(12121212)} = True")
# print(f"{is_invalid(77777)} = True")
# print(f"{is_invalid(123123123)} = True")
