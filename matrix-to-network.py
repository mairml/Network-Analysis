####Reads csv matrix and filters data based on user-based P-value or R score threshold. Outputs to network csv file.

def matrix_filter(infile, value, operand, outfile):
    outfile = open(outfile, 'w')
    removal = []
    #Open input csv document
    with open(infile, 'r') as file1:
    #Fill in columnList values
        column = file1.readline().strip() #column values are defined as the first line, new line character removed
        columnList = column.split(",") #creates a list of column names, each value separated via comma
        columnList.pop(0) #remove first value from column list, as data is null
        rowList = [] #define a list for row names, to be filled in later
        dataList = [] #define a list for data values, to be filled in later

    #For loop to fill in rowList and dataList values
        for line in file1:
            line.strip() #remove new line character from each line
            lineList = line.split(",") #creates a list out of each line, each item separated via comma
            rowList.append(lineList[0]) #the first item in the lineList is our row name, append into rowList
            dataList.append(lineList[1:len(lineList)]) #the remaining items are all data values, append to dataList


    #Find the row and column names for each data value under or over a given variable
    x = 0
    for item in dataList:
        data = dataList[x] #extracts a unique list from each sublist in dataList
        y = 0
        #1. Goes through each numerical value and selects above/below a threshold
        #2. If the column and row name corresponding with the value aren't the same, then it selects this value
        #3. If the column and row name corresponding with the value aren't already selected, then it adds it to a list for output
        #4. Finally, the code generates a network outfile in csv format
        for item in data:
            z = float(data[y])
            compare = str(z)+operand+str(value)
            if eval(compare) == True:
                if rowList[x] != columnList[y]:
                    genes = columnList[y] + rowList[x]
                    genesRev = columnList[x] + rowList[y]
                    if genes not in removal and genesRev not in removal:
                        removal.append(genes)
                        removal.append(genesRev)
                        output = rowList[x]+","+columnList[y]+","+data[y]
                        output = output.strip()
                        outfile.write(output+"\n")
            y = y+1
        x = x+1

    outfile.close()

#=====MAKE EDITS HERE=========#
#number value = threshold for filtering
#operator string = value in matrix less than/equal to/greater than threshold value 
matrix_filter("matrix_input.csv", 0.1, "=<", "network_output.csv")

