def getSplitInversions(B, C):
    result = []
    inv = 0
    while B:
        if len(C) == 0:
            result.append(B.pop(0))
        elif B[0] <= C[0]:
            result.append(B.pop(0))
        else:
            result.append(C.pop(0))
            inv += len(B)
        # END if
    # END while
    if len(C) > 0:
        result += C

    return (result, inv)
# END getSplitInversions

def getInversions(data):
    if len(data) == 1:
        return (data, 0)
    else:
        mid = len(data)/2
        (B, X) = getInversions(data[:mid])
        (C, Y) = getInversions(data[mid:])
        (D, Z) = getSplitInversions(B, C)
    return (D, X+Y+Z)
#END getInversion
