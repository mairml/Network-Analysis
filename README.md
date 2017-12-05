# Network-Analysis
Create gene co-expression network files from Ingenuity array data, compare different networks for shared and differential nodes/edges, and generate degree distribution output.

======COMPONENTS=====

matrix-to-network.py: 
1) Reads csv-formated matrix file and filters data based on user-based P-value or R score threshold
2) Outputs filtered data into a network-formatted csv file containing degrees that match the desired threshold
