# C1 - Context Diagram
# BFS vs DFS Graph Search and Performance Profiling System

from graphviz import Digraph

dot = Digraph("C1_Context")

# User
dot.node(
    "User",
    "USER",
    shape="ellipse"
)

# Inputs
dot.node(
    "GraphInput",
    "Graph + Start Node\n+ Target Node",
    shape="box"
)

dot.node(
    "AlgorithmInput",
    "BFS / DFS\nSelection",
    shape="box"
)

# Main System
dot.node(
    "System",
    "BFS / DFS SEARCH\n& PERFORMANCE PROFILING\nSYSTEM",
    shape="box",
    style="rounded"
)

# Outputs
dot.node(
    "SearchResult",
    "Search Result",
    shape="box"
)

dot.node(
    "NodesExpanded",
    "Nodes Expanded",
    shape="box"
)

dot.node(
    "Performance",
    "Best / Average /\nWorst Time",
    shape="box"
)

# User provides inputs
dot.edge(
    "User",
    "GraphInput",
    label="Provides"
)

dot.edge(
    "User",
    "AlgorithmInput",
    label="Selects"
)

# Inputs go to system
dot.edge(
    "GraphInput",
    "System",
    label="Input Data"
)

dot.edge(
    "AlgorithmInput",
    "System",
    label="Search Method"
)

# System produces outputs
dot.edge(
    "System",
    "SearchResult",
    label="Produces"
)

dot.edge(
    "System",
    "NodesExpanded",
    label="Tracks"
)

dot.edge(
    "System",
    "Performance",
    label="Measures"
)

# Generate diagram
dot.render(
    "../diagrams/c1_context_diagram",
    format="png",
    cleanup=True
)