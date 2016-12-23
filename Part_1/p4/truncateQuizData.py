with open('SCC.txt', 'r') as ifile:
    data = ifile.readlines()

for maxVert in [10000, 100000, 400000]:
    with open('SCC_{0}.txt'.format(maxVert), 'w') as ofile:
        for line in data:
            toks = map(int, line.split())
            if toks[0] <= maxVert and toks[1] <= maxVert:
                ofile.write('{0} {1}\n'.format(toks[0], toks[1]))
            # END if
        # END for
    # END with
# END for
