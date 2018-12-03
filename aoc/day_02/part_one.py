from aoc.utils import load
from collections import Counter
from itertools import permutations


def counts(box_id: str):
    counts = Counter(box_id)
    return 2 in counts.values(), 3 in counts.values()


def part_one(infile):
    box_ids = load(infile)
    twos = 0
    threes = 0
    for box_id in box_ids:
        two, three = counts(box_id)
        twos += two
        threes += three

    print(f'checksum is {twos * threes}')


def hamming(str1, str2):
    """Compute the hamming distance between two inputs."""
    retval = 0
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))


def part_two(infile):
    box_ids = load(infile)
    for a, b in permutations(box_ids, 2):
        distance = hamming(a, b)
        if distance == 1:
            print(''.join([x for x, y in zip(a, b) if x == y]))
            exit()

