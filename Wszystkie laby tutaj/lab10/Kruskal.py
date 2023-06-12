from utils. disjointset import DisjointSet
from model. undirectededge import UndirectedEdge
class Kruskal(object ):
    @staticmethod
    def execute(graph ):
        mst = set ()
        disjointset = DisjointSet ()
        for node in graph. iternodes ():
            disjointset .create(node)
        # sort edges by weight
        sorted_edges = sorted(graph. iteredges (), key=lambda edge: edge.weight)
        for edge in sorted_edges :
            if disjointset .find(edge.source) != disjointset .find(edge.target ):
                mst.add( UndirectedEdge (edge.source , edge.target , edge.weight ))
                disjointset .union(edge.source , edge.target)
        return mst


# Powyższy algorytm nie jest mojego wykonania, był za trundy dla mnie do zaimplementowania