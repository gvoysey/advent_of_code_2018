from aoc.utils import load


def remove_at(i, s):
    return s[:i] + s[i + 1:]


def main(infile):
    polymer_seq = load(infile)[0]
    while True:
        to_delete = []
        for (i1, one), (i2, two) in zip(enumerate(polymer_seq), enumerate(polymer_seq[1:])):
            if one.casefold() == two.casefold() and one != two:
                to_delete.extend([i1, i2 + 1])
        if to_delete:
            polymer_seq = ''.join((v for i, v in enumerate(polymer_seq) if i not in to_delete))
        else:
            break
    print(f'polymer residue length: {len(polymer_seq)}')


if __name__ == '__main__':
    main('input.txt')
