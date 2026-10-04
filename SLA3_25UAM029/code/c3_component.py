# C3 - Component Diagram
# Components of the BFS/DFS Search Engine

from graphviz import Digraph

dot = Digraph("C3_Component")

dot.attr(rankdir="TB")

# Main search engine
dot.node(
    "Engine",
    "BFS / DFS SEARCH ENGINE",
    shape="box",
    style="rounded"
)

# BFS components
dot.node(
    "BFS",
    "BFS ALGORITHM",
    shape="box"
)

dot.node(
    "Queue",
    "QUEUE MANAGEMENT\n(BFS)",
    shape="box"
)

dot.node(
    "BFS_Target",
    "TARGET NODE CHECK",
    shape="box"
)

# DFS components
dot.node(
    "DFS",
    "DFS ALGORITHM",
    shape="box"
)

dot.node(
    "Stack",
    "STACK MANAGEMENT\n(DFS)",
    shape="box"
)

dot.node(
    "DFS_Target",
    "TARGET NODE CHECK",
    shape="box"
)

# Common component
dot.node(
    "Visited",
    "VISITED NODE TRACKING\n& NODE EXPANSION",
    shape="box",
    style="rounded"
)

# Engine to algorithms
dot.edge(
    "Engine",
    "BFS",
    label="Uses"
)

dot.edge(
    "Engine",
    "DFS",
    label="Uses"
)

# BFS flow
dot.edge(
    "BFS",
    "Queue",
    label="Manages"
)

dot.edge(
    "BFS",
    "BFS_Target",
    label="Checks"
)

# DFS flow
dot.edge(
    "DFS",
    "Stack",
    label="Manages"
)

dot.edge(
    "DFS",
    "DFS_Target",
    label="Checks"
)

# Common tracking
dot.edge(
    "Queue",
    "Visited",
    label="Processes"
)

dot.edge(
    "Stack",
    "Visited",
    label="Processes"
)

# Generate diagram
dot.render(
    "../diagrams/c3_component_diagram",
    format="png",
    cleanup=True
)