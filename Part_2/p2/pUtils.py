
def getHamming(x, y, maxDist=float('inf')):
    assert len(x) == len(y), "String length mismatch\nStr1: {0}\nStr2: {1}".format(x, y)

    count, z = 0, int(x,2)^int(y,2)
    while z:
        count += 1
        z &= z-1
        if count >= maxDist:
            return maxDist
    return count
# END getHamming

def main():
    test = ['00000000', \
            '00000001', \
            '00000011', \
            '00000111', \
            '00001111', \
            '00011111', \
            '00111111', \
            '01111111', \
            '11111111', \
            '01010101', \
            '10101010']

    for i in range(8):
        for j in range(8):
            dist = getHamming(test[i], test[j])
            assert dist == abs(i-j), "Incorrect result."
        # END for
    # END for

    assert getHamming(test[9], test[10]) == 8
    assert getHamming(test[0], test[9]) == 4
    assert getHamming(test[8], test[10]) == 4

if __name__ == "__main__":
    main()
