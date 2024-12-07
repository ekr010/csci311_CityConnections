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
from Algorithms.prim import *

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
        #sum = 0
        for edge in algorithm_solution:
            #sum += edge[3]
            file.write(f"{edge[0]} {edge[1]} {edge[2]} {edge[3]}\n")
        print(f"Solution written to {filename}")
        #print("Total Weight: "+ str(sum))

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
    print(f"Graph read from {input_file}")

    # Perform Correct Algorithm by choice
    if alg_choice == "01":
        print("Using Prim's Algorithm")
        primSol = prim(graph)
        write_solutions_to_file(output_file, primSol)
    elif alg_choice == "02":
        print("Using Kruskal's Algorithm")
        KruskalSol = KruskalMST(graph)
        write_solutions_to_file(output_file, KruskalSol)
    else:
        print("Invalid choice. Please enter 01 for Prim's Algorithm or 02 for Kruskal's Algorithm.")

if __name__ == "__main__":
    main()
