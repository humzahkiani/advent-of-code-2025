

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

        aggregate_sum = curr_position + distance
        new_position = aggregate_sum if 0 <= aggregate_sum <= 99 else aggregate_sum % (MAX_DIAL+1)
        
        # print(f"P{curr_position} + {distance} -> {new_position} {'YES' if new_position == 0 else '' }")

        if new_position == 0:
            num_zeroes += 1
        
        curr_position = new_position

    print(f"Part 1 - Num times landed on zero: {num_zeroes}")

part_one(rotations)
import math

class LinkedListNode():
    def __init__(self, val=None):
        self.next = None
        self.prev = None
        self.val = val


class DoublyLinkedList():
    def __init__(self):
        self.root = LinkedListNode()


def part_two(rotations):
    MAX_DIAL = 99
    curr_position = 50
    num_zeroes = 0

    linked_list = DoublyLinkedList()
    linked_list.root.val = 0
    curr = linked_list.root
    prev = None
    for i in range(100):
        curr.val = i
        curr.prev = prev
        if i == 99:
            curr.next = linked_list.root
        else:
            curr.next = LinkedListNode()
        prev = curr
        curr = curr.next

    linked_list.root.prev = prev

    curr = linked_list.root
    while curr.val != 50:
        curr = curr.next
    
    for rotation in rotations:
        direction = rotation["direction"]
        distance = rotation["distance"]

        start = curr.val
        zeroes = 0

        for i in range(abs(distance)):
            if direction == "L":
                curr = curr.prev
            else:
                curr = curr.next

            if curr.val == 0:
                zeroes += 1

        num_zeroes += zeroes
        end = curr.val

        # print(f"P{start} + {direction}{distance} -> P{end}")

    print(f"Part 2 - Num times clicked on zero: {num_zeroes}")

part_two(rotations)

