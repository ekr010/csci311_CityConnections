import heapq
from collections import defaultdict

def read_graph_from_file(filename):
    '''
    Read the graph from a file and return it as a list of edges.
    '''
    graph = []
    
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith('#'):
                edge_id, start_node, end_node, length = line.split()
                edge_id = int(edge_id)
                start_node = int(start_node)
                end_node = int(end_node)
                length = float(length)
                
                # Add edge to graph structure
                graph.append((edge_id, start_node, end_node, length))
    return graph

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)
        self.queue.sort(key=lambda x: x[0])  

    def pop(self):
        return self.queue.pop(0) if self.queue else None

    def __bool__(self):
        return bool(self.queue)




def prim2(graph, start_node=0):

#new prim with hard coded pq class

    adj_list = defaultdict(list)
    for edge_id, u, v, w in graph:
        adj_list[u].append((w, edge_id, v))  
        adj_list[v].append((w, edge_id, u))  

    mst = []  
    visited = set()  
    pq = PriorityQueue()  
    visited.add(start_node)

    for weight, edge_id, neighbor in adj_list[start_node]:
        pq.push((weight, edge_id, start_node, neighbor))

    while pq and len(visited) < len(adj_list):
        weight, edge_id, u, v = pq.pop()
        if v not in visited:
            mst.append((edge_id, u, v, weight))
            visited.add(v)
            for next_weight, next_edge_id, neighbor in adj_list[v]:
                if neighbor not in visited:
                    pq.push((next_weight, next_edge_id, v, neighbor))
                    
    return mst


prim2(read_graph_from_file('cityData.txt'))




