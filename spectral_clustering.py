from sklearn.cluster import SpectralClustering
import matplotlib.pyplot as plt
from numpy import random
import time
import networkx as nx
import networkx.algorithms.community as nx_comm

graph1 = nx.read_gml('karate.gml', label = 'id')
graph2 = nx.read_gml('dolphins.gml')
graph3 = nx.read_weighted_edgelist('jazz.net')

# Graph1
oldtime = time.time()
adj_mat = nx.to_numpy_matrix(graph1)



sc = SpectralClustering(n_clusters=4, affinity='precomputed', n_init=100)

# find communities 
sc.fit(adj_mat)

newtime = time.time()


# find the nodes of the communities
labels = sc.labels_

ls = [[] for i in range(4)]

i = 1
for x in labels:
    if(x == 0):
        ls[0].append(i)
        i += 1
    elif(x == 1):
        ls[1].append(i)
        i += 1
    elif(x == 2):
        ls[2].append(i)
        i += 1
    elif(x == 3):
        ls[3].append(i)
        i += 1
        

print("Clusters : ")
print(ls)
print("Number of Clusters Found : ")
print(len(ls)) 
print("Modularity Score: " + str(nx_comm.modularity(graph1, ls)))
print("Time taken : ", newtime - oldtime)
print("---------------------------------------------------------------------------------------------------------------")


# Graph2
oldtime = time.time()
adj_mat = nx.to_numpy_matrix(graph2)

#  graph to a list
lsg2 = list(graph2)



sc = SpectralClustering(n_clusters=4, affinity='precomputed', n_init=100)

# find communities 
sc.fit(adj_mat)

newtime = time.time()


# find the nodes of the communities
labels = sc.labels_

ls = [[] for i in range(4)]

i = 0
for x in labels:
    if(x == 0):
        ls[0].append(lsg2[i])
        i += 1
    elif(x == 1):
        ls[1].append(lsg2[i])
        i += 1
    elif(x == 2):
        ls[2].append(lsg2[i])
        i += 1
    elif(x == 3):
        ls[3].append(lsg2[i])
        i += 1
        

print("Clusters : ")
print(ls)
print("Number of Clusters Found : ")
print(len(ls)) 
print("Modularity Score : " + str(nx_comm.modularity(graph2, ls)))
print("Runtime : ", newtime - oldtime)
print("---------------------------------------------------------------------------------------------------------------")


# Graph3
oldtime = time.time()
adj_mat= nx.to_numpy_matrix(graph3)



sc = SpectralClustering(n_clusters=4, affinity='precomputed', n_init=100)

# find communities 
sc.fit(adj_mat)

newtime = time.time()


# find the nodes of the communities
labels = sc.labels_

ls = [[] for i in range(4)]

i = 1
for x in labels:
    if(x == 0):
        ls[0].append(str(i))
        i += 1
    elif(x == 1):
        ls[1].append(str(i))
        i += 1
    elif(x == 2):
        ls[2].append(str(i))
        i += 1
    elif(x == 3):
        ls[3].append(str(i))
        i += 1
        

print("Clusters : ")
print(ls)
print("Number of Clusters : ")
print(len(ls)) 
print("Modularity Score : " + str(nx_comm.modularity(graph3, ls)))
print("Runtime : ", newtime - oldtime)
print("--------------------------------------------------------------------------------------------------------")