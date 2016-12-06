from mst_graphs import tests
from Kruskal import Kruskal

def testKruskal(graph, ans=None):
    k = Kruskal(graph)
    result = k.mstKruskal()
    if ans is not None:
        assert result == ans
    else:
        print "Result: {0}".format(result)
    # END if


def main():
    for t in tests:
        testKruskal(t['graph'].split('\n'), ans=t['ans'])

    with open('../p1/edges.txt', 'r') as datafile:
        testKruskal(datafile.readlines(), -3612829)

    print "All Tests Pass"

if __name__ == '__main__':
    main()
