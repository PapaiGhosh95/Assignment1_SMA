import numpy as np
import networkx as nx
from tabulate import tabulate
import matplotlib.pyplot as plt
import networkx.algorithms.community as nx_comm
import time


def edge_to_remove(graph):
    G_dict = nx.edge_betweenness_centrality(graph)
    edge = ()

  #  finds the edge with highest edge betweenness centrality score
    for key, value in sorted(G_dict.items(), key=lambda item: item[1], reverse = True):
        edge = key
        break
        
    return edge


def girvan_newman(graph):
    # find the number of connected components
    sg = nx.connected_components(graph)
    sg_count = nx.number_connected_components(graph)

    while(sg_count == 1):
        graph.remove_edge(edge_to_remove(graph)[0], edge_to_remove(graph)[1])
        sg = nx.connected_components(graph)
        sg_count = nx.number_connected_components(graph)

    return sg

graph1 = nx.read_gml('karate.gml', label = 'id')
graph2 = nx.read_gml('dolphins.gml')
graph3 = nx.read_weighted_edgelist('jazz.net')

# Graph1
oldtime = time.time()

# find communities
comm1 = girvan_newman(graph1.copy())

# find the nodes of the communities
groups1 = []

for i in comm1:
    groups1.append(list(i))

newtime = time.time()


print("Clusters : ")
print(groups1)   
print("Number of Clusters Found : ")
print(len(groups1))   
print("Modularity Score: " + str(nx_comm.modularity(graph1, groups1)))
print("Runtime : ", newtime - oldtime)
print("--------------------------------------------------------------------------------------------------------------")

# Graph2
oldtime = time.time()

# find communities
comm2 = girvan_newman(graph2.copy())

# find the nodes of the communities
groups2 = []

for i in comm2:
    groups2.append(list(i))

newtime = time.time()


print("Clusters : ")
print(groups2)    
print("Number of Clusters Found : ")
print(len(groups2))  
print("Modularity Score : " + str(nx_comm.modularity(graph2, groups2)))
print("Runtime: ", newtime - oldtime)
print("\n---------------------------------------------------------------------------------------------------------\n")

# Graph3
oldtime = time.time()

# find communities 
comm3 = girvan_newman(graph3.copy())

# find the nodes of the communities
groups3 = []

for i in comm3:
    groups3.append(list(i))

newtime = time.time()


print("Clusters : ")
print(groups3)  
print("Number of Clusters Found : ")
print(len(groups3))  
print("Modularity Score: " + str(nx_comm.modularity(graph3, groups3)))
print("Runtime : ", newtime - oldtime)