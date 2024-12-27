# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")##################################################################################
#
#  Project: Tests on the popularity driven random walk
#  File:    skewgraph.py
#  Rev.     1.2
#  Date:    12/19/2024
#           7/09/2024
#
#  Builds the structure of a "skew" graph. This is similar to a
#  Barabasi graph with a crucial change In the Barabasi graph the
#  probability of connecting node i to node j is proportional to d[j]
#  (to the value that d[j] has at the moment of creation of node i,
#  with j<i). In this case we have a parameter nu, and the probability
#  is proportional to d[j]^nu
#
#  These are the basic functions needed to create the graph. They
#  returns a simple structure: for a graph of N nodes a list of N
#  lists, one per node, and in each list the indices of the neighbors
#  of the node. The graph is undirected, so if j in adj[i], then i in
#  adj[j]
#
#  Example: the graph
#
#    0 ------- 1 
#    |\        |
#    | \       |
#    |  \      |
#    2---3-----4
#
# is represented by the list
#
#  [ [1, 2, 3],   # Node 0
#    [0, 4],      # Node 1
#    [0, 3],      # Node 2
#    [0, 2, 4],   # Node 3
#    [3, 1]       # Node 4
#  ]
#
#  Rev. 1.1
#  Added the function G_order, which orders the graph so that lower
#  indices correspond to nodes with higher degree
#
#  Rev. 1.2
#  Added the function Barabasi, which creates a Barabasi graph (skewed
#  graph with nu=1)
#
#
#   (C) Simone Santini, 2024
# 
#

import random

#
# Given a list of values, picks one at random with probability
# proportional to the value
#
def select_one(cnt):
    r = random.uniform(0,sum(cnt))
    s = 0
    for k in range(len(cnt)):
        s += cnt[k]
        if r <= s:
            return k

#
#  Selects m distinct nodes in a graph with at least m nodes using the skewed
#  rich gets richer strategy
#
#  G:  the graph (see above for the format) with at least m nodes. If
#      the graph has less or equal m nodes the whole set of nodes is returned
#  m:  the number of nodes to select
#  nu: the skew parameter
#
#  Returns:
#  A list of numbers in [0,len(G)-1] with the indices of the nodes selected
#
def m_select(G, m, nu):
    if m >= len(G):
        return list(range(len(G)))
    cnt = [float(len(g))**nu for g in G]  # array with the degree of each node of the graph

    res = []
    for k in range(m):
        k = select_one(cnt)
        res += [k]
        cnt = cnt[:k] + cnt[k+1:]
    return res


#
#
#  Creates a skewed graph with N nodes and parameters m and nu
#
def skewed_g(N, m, nu):
    G = [ [k for k in range(m) if k != i] for i in range(m)]   # fully connected graph with m node to get things started

    for n in range(m,N):
        lst = m_select(G, m, nu)
        for u in lst:
            G[u] += [n]
        G += [lst]
    return G

#
# Orders the nodes of a graph so that nodes with lower indices have
# higher degree
#
#
def G_order(G):
    n = len(G)

    q = sorted([(k, len(G[k])) for k in range(n)], key=lambda x : -x[1])
    dct = {}
    for (i, v) in enumerate(q):
        dct[v[0]] = i

    res = n*[[]]
    for (k, adj) in enumerate(G):
        p = [dct[a] for a in adj]
        res[dct[k]] = p
    return res

#
#  Creates a Barabasi-Albert graph with parameters
#
#  N:  number of nodes
#  m:  number of edges created upon each node creation
#
def Barabasi(N, m):
#    return skewed_g(N, m, 1)
    return skewed_g(N, m, 1)


if __name__ == "__main__":
    G = Barabasi(1000, 10)
    for (k, g) in enumerate(G):
        print (k, g)
