from ClusterHamming import ClusterHamming

def testPermutations():
    test = ['1 8','00000000']
    ch = ClusterHamming(test)
    p = ch.getHammingPermutations('00000000', 3)
    for item in p:
        print item

def main():
    testPermutations()

if __name__ == '__main__':
    main()
