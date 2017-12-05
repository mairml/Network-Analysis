# Network-Analysis
Create gene co-expression network files from Ingenuity array data, compare different networks for shared and differential nodes/edges, and generate degree distribution output.

======COMPONENTS=====

matrix-to-network.py: 
1) Reads csv-formated matrix file and filters data based on user-based P-value or R score threshold
2) Outputs filtered data into a network-formatted csv file containing degrees that match the desired threshold

compare-networks.py
1) Compares 2 network files and outputs files containing:
  A) All the node pairs shared by the network
  B) Connections specific to network 1
  C) Connections specific to network 2

degree-distribution.py:
1) Takes in a network file and file containing a list of nodes
2) Creates a file giving the degree distribution data -- perfect for power curve analysis in gnuplot


=====IMPLEMENTATION====

For use of these scripts, edit the given program files below the point that says:
#=====MAKE EDITS HERE=========#

Further, specific directions are given in the files
