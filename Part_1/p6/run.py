from p6 import find2sum, findMedian

q1 = { \
        'file': '2sum.txt', \
        'ans': 427 \
    }
q2 = { \
        'file': 'Median.txt', \
        'ans': 1213 \
    }

def test1(f, ans=None):
    result = find2sum(f, -10000, 10000)
    if ans is not None:
        assert result == ans, "Expected {0}, Got {1}".format(ans, result)
    else:
        print "Got {0}".format(result)
    # END if
# END test1

def test2(f, ans=None):
    result = findMedian(f)
    if ans is not None:
        assert result == ans, "Expected {0}, Got {0}".format(ans, result)
    else:
        print "Got {0}".format(result)
    # END if
# END test2

def main():
    test1(q1['file'], q1['ans'])
    test2(q2['file'], q2['ans'])
# END main

if __name__ == '__main__':
    main()
# END if
