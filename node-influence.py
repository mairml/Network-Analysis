
#Calculate Node Influence Values
from collections import Counter
import math
nodes = {}
file=open("2mo_Rsq8P01.csv",'r') #Your network file
runningtotal = 0
LIs={}
for line in file:
    lines = line.strip("\n")
    lines = lines.split("\t")
    if lines[0] not in nodes:
        nodes[lines[0]]=[lines[1]]
        if lines[1] not in nodes:
            nodes[lines[1]]=[lines[0]]
        else:
            nodes[lines[1]].append(lines[0])
    else:
        nodes[lines[0]].append(lines[1])
        if lines[1] not in nodes:
            nodes[lines[1]]=[lines[0]]
        else:
            nodes[lines[1]].append(lines[0])
list = []
previous = []
print nodes
for node in nodes:
    for values in nodes[node]:
        list.append(node)
        list.append(values)
    for key, val in nodes.items():
        current = nodes[node]
        next = val
        if current is not next:
            items = set(current).intersection(next)
            if key in current:
                for x in items:
                    one = key,x
                    two = x,key
                    if one not in previous:
                        if two not in previous:
                            list.append(x)
                            list.append(key)
                            previous.append(one)
                            previous.append(two)
    previous = []
    counts = Counter(list)
    total = 0
    logs = 0
    for val in counts.values():
        total = total+val
        logs =  logs + val*math.log(val,10)

    final = math.log(total,10)-logs/total
    runningtotal = runningtotal+1
    list = []
    length = len(counts)
    LIs[node]=final
    print node+","+str(length-1)+","+str(final)
    counts = []
print LIs
#Find the Indirect Influence

list = []
previous = []
print nodes
for node in nodes:
    tot = 0
    for values in nodes[node]:
        list.append(node)
        list.append(values)
    for key, val in nodes.items():
        current = nodes[node]
        next = val
        if current is not next:
            items = set(current).intersection(next)
            if key in current:
                for x in items:
                    one = key,x
                    two = x,key
                    if one not in previous:
                        if two not in previous:
                            list.append(x)
                            list.append(key)
                            previous.append(one)
                            previous.append(two)
    previous = []
    counts = Counter(list)
    t=0
    for n in counts:
        if n != node:
            t = t+1
            if t==1:
                tot = tot+LIs[node]*LIs[n]
            elif t == len(counts)-1:
                tot = tot + LIs[node] * LIs[n]
            tot = tot+LIs[node] * LIs[n]

    print "Indirect Influence:"
    print node, tot/len(nodes[node])
    list = []
    counts = []
#two hop neighbors
total = 0
for node in nodes:
    total=0
    twohops={}#store paths to 2 hop neighbors
    byways={}
    current=node
    for values in nodes[node]:#look at each one-hop neighbors
        val = nodes[values] #all the neighbors of one-hop neighbors
        for node2 in nodes:
            if node2 != current:
                if node2 in val:
                    if node2 not in nodes[node]:
                        total = total+1
                        if node2 not in twohops:
                            twohops[node2]=1
                            byways[node2] = [values]
                        else:
                            twohops[node2]=twohops[node2]+1
                            byways[node2].append(values)

    total=0
    for item in byways:
        val = byways[item]
        for v in val:
            total = total + ((LIs[node] * LIs[v])/twohops[item])
    if len(twohops)>0:
        print "Direct Influence"
        print node+","+str(float(total)/float(len(twohops)))
        print "Total Influence"
        print node+","+str(float(total)/float(len(twohops))*0.4+0.6*LIs[node])

