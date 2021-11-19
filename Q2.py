import itertools
import networkx as nx
from networkx.algorithms.community.centrality import girvan_newman
from networkx.algorithms.community import greedy_modularity_communities
import networkx.algorithms.community as nx_comm
import numpy as np
from sklearn.cluster import SpectralClustering
import networkx as nx

print("----------- Stats on Karate Club -----------")
kat = nx.read_gml("karate.gml", label='id')
print(nx.info(kat))
print("Avg path length : ", nx.average_shortest_path_length(kat))
avg = nx.average_clustering(kat)
print("Avg clustering coefficient : ", avg)
print("-----------------------------------------------------------------------------------------------------------------")

print("-----------Stats on Jazz  -----------")
f = open("jazz.net","r")
lines = f.readlines()
f.close()
nf = open("jazz.net","w")
for i in lines:
    if i != lines[0] and i != lines[1] and i != lines[2]:
        nf.write(i)
nf.close()
jaz = nx.read_weighted_edgelist("jazz.net")
print(nx.info(jaz))
print("Avg path length : ", nx.average_shortest_path_length(jaz))
avg = nx.average_clustering(jaz)
print("Avg clustering coefficient : ", avg)
print("-------------------------------------------------------------------------------------------------------------------")


dol = nx.read_gml("dolphins.gml")
print("----------- Stats on Dolphins -----------")
print(nx.info(dol))
print("Avg path length : ", nx.average_shortest_path_length(dol))
avg = nx.average_clustering(dol)
print("Avg clustering coefficient : ", avg)
print("-------------------------------------------------------------------------------------------------------------")