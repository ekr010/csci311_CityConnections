'''
Kruskal Algorithm for Minimum Spanning Tree

TJ Freeman
'''

'''
DisjointSet Class

Used for finding safe edges within the Minimum Spanning Tree

Properties:
    find
    union

Taken from https://en.wikipedia.org/wiki/Disjoint-set_data_structure
'''
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    '''
    Returns the set that contains the given vertex
    '''
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u]) 
        return self.parent[u]

    '''
    Unions two given sets into one set
    Uses union by rank
    '''
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def getWeight(e):
    return e[2]

'''
V: [u,v,w]
E: [[u,v,weight],[v,w,weight]]
'''
def KruskalMST(E):
    # Sort edges based on weight
    E.sort(key=lambda e: getWeight(e))

    # Initialize Disjoint Set
    ds = DisjointSet(len(E)+1)

    mst = []  # stores edges of the MST

    # Iterate over sorted edges
    for id,u,v,w in E:
        # Make sure this edge doesn't make a cycle
        # If u and v are not in the same set, add edge to MST
        if ds.find(u) != ds.find(v):
            mst.append((id, u, v, w)) # Add edge
            ds.union(u, v)  # Union sets

    return mst


