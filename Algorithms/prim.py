from collections import defaultdict

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


#new prim with hard coded pq class
def prim(graph, start_node=0):

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




