maze = []

with open("maze.txt") as f:
    for l in f.readlines():
        maze.append(l.split())
"""
matrix of bits -> graph (w/ redundancy) -> remove redundancy
matrix of bits -> graph (w/ redundancy) (BFS ver.):
queue = [start coordinates]
start_node = node()

while queue has elements:
    remove element e
    look at the neighbors of e: (neighbors are up, down, left, right)
        if the neighbor is a zero, add a node and edge to e's node and add to the queue

remove redundancy:
what nodes are necessary? remember nodes encode decisions
start node, end node
dead ends
nodes w/ one child (or two edges) aren't necessary because only one possible decision
"""
