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
  # your code here
  return clauses

if __name__ == '__main__':
  G = graph.Graph(sys.argv[1])
  nb_colors = int(sys.argv[2])
  clauses = get_clauses(G, nb_colors)
  for clause in clauses:
    print(clause)
