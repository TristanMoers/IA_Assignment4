import sys
import graph
from clause import *

"""
For the graph coloring problem, the only code you have to do is in this file.

You should replace

# your code here

by a code generating a list of clauses modeling the graph coloring problem
for the input graph and give number of colors.

You should build clauses using the Clause class defined in clause.py

Read the comment on top of clause.py to see how this works.
"""
def get_clauses(G, nb_colors):
    clauses = []
    for node in range(1, G.nb_nodes + 1):
        clause = Clause(nb_colors)
        for c in color(nb_colors):
            clause.add_positive(node, c)
            cl = Clause(nb_colors)
            for i in color(nb_colors):
                if (i != c):
                    cl.add_negative(node, i)
            clauses.append(cl)
        clauses.append(clause)

    for edge in G.edges:
        for c in color(nb_colors):
            clause = Clause(nb_colors)
            clause.add_negative(edge[0], c)
            clause.add_negative(edge[1], c)
            clauses.append(clause)
    for i in clauses:
        print(i)
    return clauses


def color(n):
  return range(1, n+1)


if __name__ == '__main__':
  G = graph.Graph(sys.argv[1])
  nb_colors = int(sys.argv[2])
  clauses = get_clauses(G, nb_colors)
  for clause in clauses:
    print(clause)
