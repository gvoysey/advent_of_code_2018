import operator
from collections import Counter


def get_operation(line: str):
    """Return the operator designated by the first character of the input string."""
    return {
        '+': operator.add
        , '-': operator.sub
    }.get(line[0])


def process_line(curr_line: str, running_value: int):
    """Process the current line and tally with the running sum."""
    return get_operation(curr_line)(running_value, int(curr_line[1:]))

def most_common_frequency(frequency_counts):
    return frequency_counts.most_common(1)[0]

def main(filename):
    """Parse the entire file of frequency changes."""
    freq = 0
    # initialize counter; we've seen zero frequency once already.
    frequency_counts = Counter([0])

    # part one
    with open(filename, 'r') as f:
        for delta_frequency in f:
            freq = process_line(delta_frequency.strip(), freq)
    print(f'The resulting frequency after all changes is {freq}')

    freq = 0
    while True:
        with open(filename, 'r') as f:
            for delta_frequency in f:
                freq = process_line(delta_frequency.strip(), freq)
                frequency_counts[freq] += 1
                if most_common_frequency(frequency_counts)[1] > 1:
                    print(f'The first frequency reached twice is: {most_common_frequency(frequency_counts)}')
                    exit()



if __name__ == "__main__":
    main('input.txt')
