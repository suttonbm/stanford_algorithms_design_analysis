from UnionFind import UnionFind

def simpleTests():
    test = range(10)
    uf = UnionFind()
    for t in test:
        uf.makeSet(t)
    # END for
    for t in test:
        assert uf.find(t) == t, "Parent not initialized correctly."
    # END for
    assert uf.countGroups() == 10, "Counted wrong number of groups."

    uf.union(0,1)
    assert uf.find(1) == 0, "Parent not updated correctly."
    assert uf.data[0][1] == 1, "Order not updated for equal trees correctly."
    assert uf.countGroups() == 9, "Counted wrong number of groups."

    uf.union(1,2)
    assert uf.find(2) == 0, "Parent not updated correctly."
    assert uf.data[0][1] == 1, "Order not updated for unequal trees correctly."
    assert uf.countGroups() == 8, "Counted wrong number of groups."

    uf.union(3,4)
    uf.union(4,5)
    uf.union(0,3)
    assert uf.data[0][1] == 2, "Order not updated for unequal trees."
    assert uf.data[5][0] == 3, "Parent should not be updated until find operation."
    assert uf.find(5) == 0, "Find operation returned wrong parent."
    assert uf.data[5][0] == 0, "Parent should have been updated."
    assert uf.countGroups() == 5, "Counted wrong number of groups."

def main():
    

if __name__ == '__main__':
    main()
