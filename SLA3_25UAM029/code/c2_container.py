# C2 - Container Diagram
# BFS vs DFS Graph Search and Performance Profiling System

from graphviz import Digraph

dot = Digraph("C2_Container")

# Top-to-bottom layout
dot.attr(rankdir="TB")

# Main containers
dot.node(
    "Input",
    "GRAPH & INPUT SETUP",
    shape="box",
    style="rounded"
)

dot.node(
    "BFS",
    "BFS SEARCH",
    shape="box",
    style="rounded"
)

dot.node(
    "DFS",
    "DFS SEARCH",
    shape="box",
    style="rounded"
)

dot.node(
    "Profile",
    "PERFORMANCE PROFILING\n& OUTPUT",
    shape="box",
    style="rounded"
)

# Input to search containers
dot.edge(
    "Input",
    "BFS",
    label="Graph, Start, Target"
)

dot.edge(
    "Input",
    "DFS",
    label="Graph, Start, Target"
)

# Search results to profiling
dot.edge(
    "BFS",
    "Profile",
    label="Search Result"
)

dot.edge(
    "DFS",
    "Profile",
    label="Search Result"
)

# Generate diagram
dot.render(
    "../diagrams/c2_container_diagram",
    format="png",
    cleanup=True
)