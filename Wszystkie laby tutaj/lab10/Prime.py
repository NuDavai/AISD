from model. undirectededge import UndirectedEdge
from model.edge import Edge
from Queue import PriorityQueue

class Prim(object ):
    """ Algorytm inspirowany implementacja z ksiazki
    Python Algorithms: Mastering Basic Algorithms in the Python
    Language, 2010 by Magnus Lie Hetland."""
    @staticmethod
    def execute(graph , root=None ):
        if root is None:
            root = graph. iternodes (). next () # get f irs t random element
        parents = {}
        pq = PriorityQueue ()
        pq.put ((0, None , root ))
        mst = set ()
        while not pq.empty ():
            weight , parent , node = pq.get ()
            if node in parents:
                continue
        parents[node] = parent
        if not parent is None:
            mst.add( UndirectedEdge (parent , node , weight ))
        for edge in graph. iteroutedges (node ):
            pq.put (( edge.weight , edge.source , edge.target ))
        return mst
    @staticmethod
    def execute2(graph , root=None ):
        """Prim's algorithm for finding MST in O(E log V) time."""
        if root is None:
            root = graph. iternodes (). next () # get f irs t random element
        minimum_weights = dict ((( node , float("inf")) for node in graph. iternodes ()))
        parents = {}
        minimum_weights [root] = 0
        pq = PriorityQueue ()
        pq.put ((0, root ))
        mst = set ()
        visited = set ()
        while not pq.empty ():
            weight , source = pq.get ()
            visited.add(source)
            for edge in graph. iteroutedges (source ):
                if (not edge.target in visited and edge.weight < minimum_weights [edge.target ]):
                    minimum_weights [edge.target] = edge.weight
                    pq.put (( edge.weight , edge.target ))
                    parents[edge.target] = edge.source
        for source , target in parents. iteritems ():
            mst.add( UndirectedEdge (source , target , minimum_weights [source ]))
        return mst
    @staticmethod
    def execute_best_with_complete_graph (graph , root=None ):
        """Prim's algorithm for finding MST in O(V∗∗2) time."""
        if root is None:
            root = graph. iternodes (). next () # get f irs t random element
        mst = set ()
        queue = {} # set can be used here
        minimum_weights = {}
        parents = {}
        for node in graph. iternodes ():
            queue[node] = None
            minimum_weights [node] = float("inf")
        minimum_weights [root] = 0
        while queue:
            source = min(queue , key= minimum_weights .get)
            del queue[source]
            for edge in graph. iteroutedges (source ):
                if (edge.target in queue and edge.weight < minimum_weights [edge.target ]):
                    minimum_weights [edge.target] = edge.weight
                    parents[edge.target] = edge.source
        for source , target in parents. iteritems ():
            mst.add( UndirectedEdge (source , target , minimum_weights [source ]))
        return mst

        @staticmethod
        def execute_trivial (graph , source=None ):
            """Prim's algorithm for finding MST in O(V∗E) time."""
            in_mst = dict ((node , False) for node in graph. iternodes ())
            if source is None: # get f irs t random node
                source = graph. iternodes (). next ()
            in_mst[source] = True

# Powyższy algorytm nie jest mojego wykonania, był za trundy dla mnie do zaimplementowania