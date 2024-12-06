import matplotlib.pyplot as plt
import random
import time
from kruskal import *

def generate_edges(n, m):
    edges = []
    for i in range(m):
        u, v = random.sample(range(n), 2)
        w = random.randint(1, 100)
        edges.append((i, u, v, w))
    return edges

# Measure runtime
ns = [10, 50, 100, 200, 500, 1000]
runtimes = []

for n in ns:
    m = 5 * n  # Assuming sparse graph
    edges = generate_edges(n, m)
    start_time = time.time()
    KruskalMST(edges)
    runtimes.append(time.time() - start_time)

# Plot
plt.plot(ns, runtimes, marker='o')
plt.title('Runtime of Kruskal\'s Algorithm')
plt.xlabel('Number of Vertices (n)')
plt.ylabel('Runtime (seconds)')
plt.grid()
plt.show()
