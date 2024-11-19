'''
City Connections Project Due 12/06/2024

Project by: Bryce Babcock, Tj Freeman, and Emily Rivera

Tasks:
    Emily: read in the file and create the menu
    Bryce: Bredth First Search
    Tj: Depth First Search
'''

def main():

  # shows a welcome header
  print("╔" + 48 * "═" + "╗")
  print(f"║{'Welcome to the Connecting a City project!':^48}║")
  print("╚" + 48 * "═" + "╝")

  # Get file from user
  #getfile()
  menu()


def read_graph_from_file():
  '''
The format we will use for storing graphs in this project stores edges explicitly and vertices implicitly. This does not allow
any vertices which have no incident edges, but such a vertex would be unconnectable, so we will assume there are none in
our graph.

Each line in the data file will represent one edge in the graph (except for comments, which are lines starting with #). It
stores four pieces of information about each edge, separated by spaces:
1. Edge ID: A unique integer for each edge.
2. Start Node ID: The integer ID of the first vertex the edge touches.
3. End Node ID: The integer ID of the second vertex the edge touches.
4. Length: The floating-point length of the edge.

You should read in an input file in this format, build a representation of the graph, compute your shortest connecting set
of edges, and write it out as a file in the same format.

Several sample datasets are available at https://www.cs.utah.edu/~lifeifei/SpatialDataset.htm [1]. Use files
named “XXX Network’s Edges (Edge ID, Start Node ID, End Node ID, L2 Distance)”. The one pictured above is map
4, City of San Joaquin Valley, and should be a good starting test.

I should be able to call your code from a bash prompt (or script!) as languageCommand programName inputfile outputfile
or ./programName inputfile outputfile, where
2
– languageCommand is “python”, “java”, or similar,
– programName is your executable (If you’re using python, this is just your code file. If you’re using Java, C/C++,
etc., this will be the output of the compiler.), and
– inputfile contains the graph you need to connect, and your code should write its set of output edges to
outputfile.
  '''
    pass


def BFS():
    '''
    Bredth First Search 
    '''
    pass

def DFS():
    '''
    Depth First Search 
    '''
    pass

