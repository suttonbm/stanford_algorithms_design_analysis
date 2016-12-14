def readData(filename):
    with open(filename, 'r') as ifile:
        data = ifile.readlines()
        (capacity, items) = map(int, data[0].split())

        values = []
        weights = []
        for line in data[1:]:
            (v, w) = map(int, line.split())
            values.append(v)
            weights.append(w)
        # END for
    # END with

    return (capacity, values, weights)
# END readData
