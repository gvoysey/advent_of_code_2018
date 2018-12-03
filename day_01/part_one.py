import operator


def get_operation(line: str):
    """Return the operator designated by the first character of the input string."""
    return {
        '+'  : operator.add
        , '-': operator.sub
    }.get(line[0])


def process_line(curr_line: str, running_value: int):
    """Process the current line and tally with the running sum."""
    return get_operation(curr_line)(running_value, int(curr_line[1:]))


def main(filename):
    """Parse the entire file of frequency changes."""
    freq = 0
    with open(filename, 'r') as f:
        for delta_frequency in f:
            freq = process_line(delta_frequency.strip(), freq)
    print(freq)


if __name__ == "__main__":
    main('input.txt')
