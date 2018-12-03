def load(infile):
    with open(infile, 'r') as f:
        return [x.strip() for x in f]
