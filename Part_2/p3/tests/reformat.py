tests = ['p01','p02','p03','p04','p05', \
        'p06','p07','p08']

def main():
    with open('../tests.py', 'w') as pytestfile:
        pytestfile.write('tests = [')
        for test in tests:
            with open('{0}.txt'.format(test),'w') as ofile:
                with open('{0}_c.txt'.format(test), 'r') as cfile:
                    capacity = int(cfile.readline().strip())
                with open('{0}_p.txt'.format(test), 'r') as vfile:
                    values = []
                    data = vfile.readlines()
                    for line in data:
                        line.strip()
                        if len(line) != 0:
                            values.append(int(line))
                        # END if
                    # END for
                with open('{0}_w.txt'.format(test), 'r') as wfile:
                    weights = []
                    data = wfile.readlines()
                    for line in data:
                        line.strip()
                        if len(line) != 0:
                            weights.append(int(line))
                        # END if
                    # END for
                # END with

                assert len(values) == len(weights)
                ofile.write('{0} {1}\n'.format(capacity, len(values)))
                for v, w in zip(values, weights):
                    ofile.write('{0} {1}\n'.format(v, w))
                # END for
            # END with

            with open('{0}_s.txt'.format(test),'r') as sfile:
                soln = sfile.readlines()
                total = 0
                for p, v in zip(soln, values):
                    total += int(p) * v
                # END for
            # END with

            pytestfile.write("{")
            pytestfile.write('"file": "tests/{0}", "soln": {1}'.format('{0}.txt'.format(test), total))
            pytestfile.write("}, \\\n")
        # END for
    # END with

if __name__ == '__main__':
    main()
