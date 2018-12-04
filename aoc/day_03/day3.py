from aoc.utils import load

import numpy as np
import attr

FABRIC_SIZE = 1000


@attr.s
class Claim:
    claim_id = attr.ib()
    x = attr.ib()
    y = attr.ib()
    width = attr.ib()
    height = attr.ib()

    @property
    def index_width(self):
        return self.x + self.width

    @property
    def index_height(self):
        return self.y + self.height


def parse_claim(claim_line: str):
    claim_id, _, remainder = claim_line.rpartition('@')
    top_left, _, dims = remainder.rpartition(':')
    top_left_x, top_left_y = (int(x) for x in top_left.split(','))
    width, height = (int(x) for x in dims.split('x'))

    return Claim(claim_id.strip(), top_left_x, top_left_y, width, height)


def find_claims(infile):
    fabric = np.zeros((FABRIC_SIZE, FABRIC_SIZE))
    claim_list = load(infile)
    claims = [parse_claim(x) for x in claim_list]

    for claim in claims:
        fabric[claim.y:claim.index_height, claim.x:claim.index_width] += 1

    print(f'{len(fabric[fabric >= 2])} square inches of fabric are within two or more claims.')

    for claim in claims:
        vals = fabric[claim.y:claim.index_height, claim.x:claim.index_width]
        if np.array_equal(vals, np.ones_like(vals)):
            print(f'{claim.claim_id} has no overlaps')


if __name__ == "__main__":
    find_claims('input.txt')
