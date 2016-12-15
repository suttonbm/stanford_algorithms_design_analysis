def swap(v, i, j):
    tmp = v[i]
    v[i] = v[j]
    v[j] = tmp
# END swap

def pivot(data, pivot):
    # Swap the pivot element to the front of the list
    swap(data, 0, pivot)
    val = data[0]
    i=1
    for j in range(1, len(data)):
        #print "i={0}, j={1}".format(i,j)
        if data[j] <= val:
            swap(data, i, j)
            i += 1
        # END if
        #print val, "-->", data
    # END for
    swap(data, 0, i-1)
    return (data[:i-1], data[i:])
# END pivot

def quickSort(data, getPivot):
    if len(data) <= 1:
        return (data, 0)
    else:
        # Increment count
        c = len(data)-1

        # Get the pivot element to use
        p = getPivot(data)
        pval = data[p]

        # Perform the pivot operation
        (x, y) = pivot(data, p)

        # Perform quicksort recursively
        (a, n) = quickSort(x, getPivot)
        (b, m) = quickSort(y, getPivot)
    return (a+[pval]+b, n+m+c)
# END quickSort

def pickFirst(data):
    return 0
# END pickFirst

def pickLast(data):
    return -1
# END pickLast

def midThree(data):
    ary = []
    ary.append(data[0])
    ary.append(data[-1])
    mid = (len(data)-1)/2
    ary.append(data[mid])

    ary.sort()
    val = ary[1]
    if val == data[0]:
        return 0
    elif val == data[-1]:
        return -1
    else:
        return mid
# END midThree

def p2a(data):
    s, result = quickSort(data, pickFirst)
    return result
# END p2a

def p2b(data):
    s, result = quickSort(data, pickLast)
    return result
# END p2b

def p2c(data):
    s, result = quickSort(data, midThree)
    return result
# END p2c
