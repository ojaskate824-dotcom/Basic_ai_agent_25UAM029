# C1 - Context Diagram
# BFS vs DFS Graph Search and Performance Profiling System

from graphviz import Digraph

dot = Digraph("C1_Context")

# User
dot.node("User", "User", shape="actor")

# Main System
dot.node(
    "System",
    "BFS/DFS Graph Search\n& Performance Profiling System",
    shape="box"
)

# Input
dot.edge(
    "User",
    "System",
    label="Graph\nStart Node\nTarget Node\nBFS / DFS"
)

# Output
dot.edge(
    "System",
    "User",
    label="Search Result\nNodes Expanded\nBest / Average / Worst Time"
)

# Generate diagram
dot.render("../diagrams/c1_context_diagram", format="png", cleanup=True)