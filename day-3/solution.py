
## Part 1 

def parse_input():
    banks = []
    with open('./input.txt', 'r') as file:
        for line in file:
            banks.append([int(char) for char in line if char != '\n'])

    return banks

banks = parse_input()

def part_one(banks):
    total_joltage = 0

    for bank in banks:
        max_digit_and_index = [0,0]
        num_digits = len(bank)

        for idx in range(0,num_digits-1):
            digit = bank[idx]

            if digit > max_digit_and_index[0]:
                max_digit_and_index = [digit,idx]

        first_digit, first_digit_idx = max_digit_and_index
        second_digit = max(bank[first_digit_idx+1:])

        bank_max_joltage = int(str(first_digit)+str(second_digit))
        total_joltage += bank_max_joltage

    return total_joltage

test_cases = [
    [[[1,2,3,4]], 34],
    [[[4,3,2,1]], 43],
    [[[3,4,5],[5,4,1]], 99],
    [[[5,3,2,5,1]], 55],
    [[[5,3,2,5,9]], 59]
]

def run_part_one_tests(test_cases):
    num_passed = 0
    for case in test_cases:
        banks, expected = case

        actual = part_one(banks)
        result = expected == actual
        print(f"Test Case: {banks}, expected: {expected}, actual: {actual} -- {"PASSED" if result else "FAILED"}")

# run_part_one_tests(test_cases)

print(f"Part 1 - Total joltage is {part_one(banks)}")

    






