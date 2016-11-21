import random

class AdjacencyList:
    vertices = []
    edges = []
    
    def __init__(self):
        pass
    
    def read(self, data):
        '''
        :param data: a list of strings, each string tab-delimited, with the first token being the
            name of a vertex, and the remaining tokens being the names of adjacent vertices
        '''
        for line in data:
            tokens = [int(t) for t in line.split('\t')]
            vertex = tokens[0]
            self.vertices.append(vertex)
            for adj in tokens[1:]:
                # Don't add duplicate entries -> only add edges where the adjacent vertex is larger.
                if adj > vertex:
                    self.edges.append((vertex, adj))
                # END if
            # END for
        # END for
        pass
    # END read