from networkx.algorithms.community.modularity_max import greedy_modularity_communities
import time
import networkx as nx
import networkx.algorithms.community as nx_comm

graph1 = nx.read_gml('karate.gml', label = 'id')
graph2 = nx.read_gml('dolphins.gml')
graph3 = nx.read_weighted_edgelist('jazz.net')

# Graph1
oldtime = time.time()

# find communities 
comm1 = greedy_modularity_communities(graph1)

newtime = time.time()


# find the nodes of the community
group1 = (list(sorted(c) for c in comm1))

print("Clusters : ")
print(group1)   
print("Number of Clusters Found : ")
print(len(group1))  
print("Modularity Score: " + str(nx_comm.modularity(graph1, group1)))
print("Runtime: ",  newtime-oldtime)
print("\n===========================================================================================\n")

# Graph2
oldtime = time.time()

# find communities
comm2 = greedy_modularity_communities(graph2)

newtime = time.time()


# find the nodes of the community
group2 = (list(sorted(c) for c in comm2))

print("Clusters : ")
print(group2)   
print("Number of Clusters Found : ")
print(len(group2))  
print("Modularity Score: " + str(nx_comm.modularity(graph2, group2)))
print("Runtime: ",  newtime-oldtime)
print("\n===========================================================================================\n")


# Graph3
oldtime = time.time()

# find communities 
comm3 = greedy_modularity_communities(graph3)

newtime = time.time()

# find the nodes of the communities
group3 = (list(sorted(c) for c in comm3))

print("Clusters : ")
print(group3)   
print("Number of Clusters Found: ")
print(len(group3))  
print("Modularity Score: " + str(nx_comm.modularity(graph3, group3)))
print("Runtime: ",  newtime-oldtime)