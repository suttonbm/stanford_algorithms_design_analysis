from p1_graphs import tests as p1t
from p2_graphs import tests as p2t

from p2_answer import cluster_A, cluster_B

p1_datafile = 'clustering1.txt'
p2_datafile = 'clustering_big.txt'

def run_A(graph, k, ans=None):
    result = cluster_A(graph, k)
    if ans is not None:
        assert result == ans, "Got {0}, Expected {1}".format(result, ans)
        print "Pass"
    else:
        print "Result: {0}".format(result)
    pass

def run_B(graph, minDist, ans=None):
    result = cluster_B(graph, minDist)
    if ans is not None:
        assert result == ans, "Got {0}. Expected {1}".format(result, ans)
        print "Pass"
    else:
        print "Result: {0}".format(result)
    pass

def main():
    print "Running Tests for Part A"
    for test in p1t:
        run_A(test['graph'].split('\n'), test['k'], ans=test['dist'])

    print "Running Tests for Part B"
    for test in p2t:
        run_B(test['graph'].split('\n'), test['minDist'], ans=test['k'])

    print "Running Quiz for Part A"
    with open(p1_datafile, 'r') as datafile:
        run_A(datafile.readlines(), 4)

    print "Running Quiz for Part B"
    with open(p2_datafile, 'r') as datafile:
        run_B(datafile.readlines(), 3)

if __name__ == '__main__':
    main()
