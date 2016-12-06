from copy import copy
from DictBinHeap import DictBinHeap

def primMST_Basic(al):
    # Prim's MST algorithm with quadratic time
    V = copy(al.nodes)
    X = set([V.pop()])
    T = dict()
    while len(V) > 0:
        #print "X Contains: {0}".format(X)
        minEdgeLength = float('inf')
        minEdge = (-1, -1)
        newNode = -1
        for node in X:
            nodeEdges = al.edges[node]
            for e in nodeEdges:
                if e[0] in X:
                    continue
                if e[1] < minEdgeLength:
                    minEdgeLength = e[1]
                    minEdge = (node, e[0])
                    newNode = e[0]
                # END if
            # END for
        # END for

        #print "Adding min edge {0} with cost {1}".format(minEdge, minEdgeLength)
        T[minEdge] = minEdgeLength
        X.add(newNode)
        V.remove(newNode)
        # END if
    # END while

    return sum(T.values())
# END primMST_Basic

def primMST_Heap1(al):
    # Prim's MST algorithm with m*log(n) time using heap with edges
    V = copy(al.nodes)
    X = set([V.pop()])

    edges = []
    for node in X:
        for edge in al.edges[node]:
            e = ((node, edge[0]), edge[1])
            edges.append(e)
        # END for
    # END for
    edgeHeap = DictBinHeap()
    edgeHeap.heapify(edges)

    T = dict()
    while len(V) > 0:
        edge, cost = edgeHeap.pop()
        if edge[1] in X:
            continue

        newNode = edge[1]
        T[edge] = cost
        X.add(newNode)
        V.remove(newNode)

        for edge in al.edges[newNode]:
            edgeHeap.push((newNode, edge[0]), edge[1])
        # END for
    # END while

    return sum(T.values())
# END primMST_Heap1



def primMST_Heap2(al):
    # TODO: Implement prim's MST algorithm with vertices and edges in a heap
    V = copy(al.nodes)
    X = set([V.pop()])

    #print "Initializing Edge Heaps by Node"
    nodeHeaps = dict()
    for node in V:
        h = DictBinHeap()
        e = []
        for edge in al.edges[node]:
            if edge[0] in V:
                e.append((edge[0], float('inf')))
            else:
                e.append((edge[0], edge[1]))
            # END if
        # END for
        h.heapify(e)
        nodeHeaps[node] = h
    # END for

    #print "Initializing Min Edge Heap"
    tmp = []
    for node in V:
        (_, cost) = nodeHeaps[node].peek()
        tmp.append((node, cost))
    # END for
    E = DictBinHeap()
    E.heapify(tmp)

    T = dict()
    while len(V) > 0:
        newNode, cost = E.pop()
        n, _ = nodeHeaps[newNode].peek()
        #print "Adding Node {0}".format(newNode)
        #E.dump()

        T[(n, newNode)] = cost
        X.add(newNode)
        V.remove(newNode)
        del nodeHeaps[newNode]

        for edge in al.edges[newNode]:
            if edge[0] not in X:
                #print "Updating Edge ({0} -> {1}), Cost {2}".format(node, edge[0], edge[1])
                nodeHeaps[edge[0]].updateValue(newNode, edge[1])
                _, cost = nodeHeaps[edge[0]].peek()
                E.updateValue(edge[0], cost)
            # END if
        # END for
    # END while

    return sum(T.values())
# END primMST_Heap2
