from Kruskal import Kruskal
from ClusterHamming import ClusterHamming

def cluster_A(data, k):
    krusty = Kruskal(data)
    return krusty.clusterKruskal(k)

def cluster_B(data, minDist):
    ham = ClusterHamming(data)
    result = ham.run(minDist)
    #ham.printSummary()
    #ham.uf.dump()
    return result
