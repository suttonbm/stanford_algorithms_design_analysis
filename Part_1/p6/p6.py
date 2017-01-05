from collections import defaultdict

def exists2sum(filename, t):
    ht = defaultdict(bool)
    result = False
    print "Searching for 2Sum for t={0}".format(t)
    with open(filename, 'r') as ifile:
        for line in ifile:
            n = int(line)
            if ht[t-n]:
                result = True
                break
            else:
                ht[n] = True
            # END if
        # END while
    # END with
    return result
# END exists2sum

def find2sum(filename, tmin, tmax):
    count = 0
    for t in range(tmin, tmax+1):
        if exists2sum(filename, t):
            count += 1
        # END if
    # END for
    return count
# END find2sum

def findMedian(filename):
    pass
# END findMedian
