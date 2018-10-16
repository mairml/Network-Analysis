#Mair ML
#Generate an adjacency matrix in CSV format from a network file
#Can combine matrices from two networks

file1= open("networkFILE1.csv",'r') #First network file
#OPTIONAL: remove if you do not want an overlayed matrix 
file2= open("OPTIONALnetworkFILE2.csv",'r') #Second network file 


network = [] #holds node-node pairs (edges)
nodes = [] #holds the nodes in the network

for line in file1:
    line = line.strip()
    items = line.split("\t")
    key = items[0] #first node
    val = items[1] #second node in interaction
    add1 = key+val #we want both orders
    add2 = val+key #we want both orders
    network.append(add1)
    network.append(add2)
    if key not in nodes: #no duplicates
        nodes.append(key)
    if val not in nodes: #no duplicates 
        nodes.append(val)

#OPTIONAL BLOCK: remove if you do not want an overlayed matrix
for line in file2: 
    line = line.strip()
    items = line.split("\t")
    key = items[0]
    val = items[1]
    if key not in nodes:
        nodes.append(key)
    if val not in nodes:
        nodes.append(val)

#Get the header
line = ""
for h in nodes:
    line = line+h+","
line = line.strip(",") 
print line #print the header

#Get the column/matrix content
for h in nodes:
    line = h+","
    for v in nodes: #parse through nodes to get the network "match"
        if h == v: 
            line = line+ str(0) + "," #CHANGE THIS to str(1) if you want to include self-self interactions
        elif h+v in network and v+h in network: #If the node-node interaction exists, put 1 in matrix
            line = line + str(1) + ","
        elif h+v not in network: #If no node-node interaction exists, put 0 in matrix 
            line = line + str(0) + ","
    line = line.strip(",")
    print line #prints out each line in the matrix 
