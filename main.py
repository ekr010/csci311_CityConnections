'''
City Connections Project Due 12/06/2024

Project by: Bryce Babcock, Tj Freeman, and Emily Rivera

Tasks:
    Emily: read in the file 
    Bryce: Breadth First Search
    Tj: Kruskal's Algorithm
'''
import sys
from Algorithms.kruskal import *

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

def write_solutions_to_file(filename, algorithm_solution):
    '''
    Write both solutions to a file in the same format as the input file.

    a line for each edge
    '''
    with open(filename, 'w') as file:        
        for edge in algorithm_solution:
            file.write(f"{edge[0]} {edge[1]} {edge[2]} {edge[3]}\n")

def BFS(graph):
    '''
    Breadth First Search 
    '''
    print("Breadth First Search Solution:")

def DFS(graph):
    '''
    Perform Depth First Search to find a subset of edges that connect all nodes.
    This function returns a list of edges that form a Depth First Search tree.
    '''
    print("Depth First Search Solution:")

def main():
    ''' 
    Should be able to call code from terminal as python main.py input.txt output.txt choice 
    '''
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: python main.py input_file output_file alg_choice")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    alg_choice = sys.argv[3]

    # Read the input graph
    graph = read_graph_from_file(input_file)

    # Perform Correct Algorithm by choice
    if alg_choice == "01":
        depth_first = DFS(graph)
        write_solutions_to_file(output_file, depth_first)
    elif alg_choice == "02":
        print("Using Kruskal's Algorithm")
        breadth_first = KruskalMST(graph)
        write_solutions_to_file(output_file, breadth_first)
    else:
        print("Invalid choice. Please enter 01 for Depth First Search or 02 for Breadth First Search.")

    print(f"Graph read from {input_file}")
    print(f"Solution written to {output_file}")

if __name__ == "__main__":
    main()
