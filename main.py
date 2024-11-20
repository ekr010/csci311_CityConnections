'''
City Connections Project Due 12/06/2024

Project by: Bryce Babcock, Tj Freeman, and Emily Rivera

Tasks:
    Emily: read in the file and create the menu
    Bryce: Breadth First Search
    Tj: Depth First Search
'''
import sys

def main():
    ''' 
    Should be able to call code from terminal as python main.py input.txt output.txt
    '''
    # Check for correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: python main.py input_file output_file")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Read the input graph
    graph = read_graph_from_file(input_file)

    # Find the depth first search solution
    depth_first = DFS(graph)

    # Find the breadth first search solution
    breadth_first = BFS(graph)

    # Write both solutions to the output file
    write_solutions_to_file(output_file, depth_first, breadth_first)

    print(f"Graph read from {input_file}")
    print(f"Solution written to {output_file}")

if __name__ == "__main__":
    main()

def read_graph_from_file(filename):
    '''
    Read the graph from a file and return it as a dictionary.
    '''
    graph = {}
    
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith('#'):
                edge_id, start_node, end_node, length = line.split()
                edge_id = int(edge_id)
                start_node = int(start_node)
                end_node = int(end_node)
                length = float(length)
                
                # Add edge to graph structure
                if start_node not in graph:
                    graph[start_node] = []

def write_solutions_to_file(filename, depth_first_solution, breadth_first_solution):
    '''
    Write both solutions to a file in the same format as the input file.
    '''
    with open(filename, 'w') as file:
        file.write("Depth First Search Solution:\n")
        for edge in depth_first_solution:
            file.write(f"{edge[0]} {edge[1]} {edge[2]}\n")
        
        file.write("\nBreadth First Search Solution:\n")
        for edge in breadth_first_solution:
            file.write(f"{edge[0]} {edge[1]} {edge[2]}\n")

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
