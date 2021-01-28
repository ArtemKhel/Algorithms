from scipy.sparse.csgraph import minimum_spanning_tree
import os
import subprocess
import networkx as nx
import numpy as np
import random as rnd


# Иногда diff выдает небольшое различие, т.к. могут существовать разные ребра одной длины


os.chdir(os.path.dirname(os.path.abspath(__file__)))

vertices = 100
# edges = 100000
edges = vertices * (vertices - 1) // 2
dist = 1000000


with open('./_input.txt', 'w') as inp, open('./_answer.txt', 'w') as ans:
    print(vertices, edges, file=inp)
    
    g = nx.gnm_random_graph(vertices, edges)
    for (u,v,w) in g.edges(data=True):
        w['weight'] = rnd.randrange(dist)
    g = nx.to_numpy_matrix(g)

    # for i in range(vertices - 1):
    #     for j in range(i + 1, vertices):
    #         if g[i, j] != 0:
    #             print(i, j, int(g[i, j]), file=inp)
    for x in (f'{i} {j} {int(g[i, j])}' for i in range(vertices - 1) for j in range(i + 1, vertices) if g[i, j]):
        print(x, file=inp)


    t = minimum_spanning_tree(g).toarray()

    # for i in range(vertices):
    #     for j in range(vertices):
    #         if t[i, j] != 0:
    #             print(f'{i} - {j} {int(t[i,j])}', file=ans)
    for x in (f'{i} - {j} {int(t[i, j] + t[j, i])}' for i in range(vertices) for j in range(i + 1, vertices) if (t[j, i] or t[i, j])):
    	print(x, file=ans)


subprocess.run(['/usr/bin/time', '-f', '\nKruskal\nReal: %e\nUser: %U\nSys:  %S\nMem: %M Kb\n', './mst_kruskal.out'])
subprocess.run(['diff', './_answer.txt', './_output_kruskal.txt'])

subprocess.run(['/usr/bin/time', '-f', '\nPrim\nReal: %e\nUser: %U\nSys:  %S\nMem: %M Kb\n', './mst_prim.out'])
subprocess.run(['diff', './_answer.txt', './_output_prim.txt'])


