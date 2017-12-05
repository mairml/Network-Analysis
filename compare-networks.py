#This file can compare 2 csv networks with the following input file structure:
#gene1, gene2, value
#or:
#gene1, gene2

def compare(network1,network2,networkBoth_file,network1_file,network2_file):

    #open all the files for use
    network1 = open(network1, 'r')
    network2 = open(network2, 'r')
    networkBoth_file = open(networkBoth_file, 'w')
    network1_file = open(network1_file, 'w')
    network2_file = open(network2_file, 'w')

    #takes all the network connections in network1
    IDsList = []
    for line in network1:
        line = line.strip()
        lineList = []
        lineList.append(line)
        lineList = line.split(",") #build list of row/column IDs + value
        #Remove the node value-- we just want the connection
        if len(lineList)>2:
            lineList.pop()
        IDsList.append(lineList)
        IDsList.append(lineList[::-1])

    # takes all the network connections in network2
    IDsList2 = []
    for line in network2:
        line = line.strip()
        lineList = []
        lineList.append(line)
        lineList = line.split(",") #build list of row/column IDs + value
        if len(lineList)>2:
            lineList.pop()
        IDsList2.append(lineList)
        IDsList2.append(lineList[::-1])

    #Find all identical or different connections between the network lists
    same = []
    differences = []
    for item in IDsList:
        if item in IDsList2:
            same.append(item)
        else:
            differences.append(item)

    #Items in both lists are output to file
    filter1 = []
    for item in same:
        if item[::-1] not in filter1:
            filter1.append(item)
    for item in filter1:
        newstring = str(item).replace("[","")
        newstring = newstring.replace("]","")
        newstring = newstring.replace("'","")
        newstring = newstring.replace(" ","")
        newstring = newstring.replace(",", "\t")
        networkBoth_file.write(str(newstring) + "\n")

    #Items in only a single list are output to respective files
    filter2 = []
    for item in differences:
        if item[::-1] not in filter2:
            filter2.append(item)
    for item in filter2:
        if item in IDsList:
            newstring = str(item).replace("[", "")
            newstring = newstring.replace("]", "")
            newstring = newstring.replace("'", "")
            newstring = newstring.replace(" ", "")
            network1_file.write(newstring + "\n")
        elif item in IDsList2:
            newstring = str(item).replace("[", "")
            newstring = newstring.replace("]", "")
            newstring = newstring.replace("'", "")
            newstring = newstring.replace(" ", "")
            network2_file.write(newstring + "\n")


#=====MAKE EDITS HERE=========#
#first 2 files should be input files, last three are output
compare("network1.csv","network2.csv","in_both.csv","in_network1.csv","in_network2.csv")
