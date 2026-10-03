# C4 - Code Level Diagram
# Main functions used in the BFS/DFS Performance Profiling System

from graphviz import Digraph

dot = Digraph("C4_Code")

# Main functions
dot.node(
    "Graph",
    "get_small_graph()\nCreates the 15-node graph",
    shape="box"
)

dot.node(
    "BFS",
    "bfs()\nPerforms Breadth-First Search",
    shape="box"
)

dot.node(
    "DFS",
    "dfs()\nPerforms Depth-First Search",
    shape="box"
)

dot.node(
    "Profile",
    "profile_algorithm()\nMeasures performance",
    shape="box"
)

# Function relationships
dot.edge("Graph", "BFS", label="Graph")
dot.edge("Graph", "DFS", label="Graph")

dot.edge("BFS", "Profile", label="Algorithm Function")
dot.edge("DFS", "Profile", label="Algorithm Function")

# Generate diagram
dot.render(
    "../diagrams/c4_code_diagram",
    format="png",
    cleanup=True
)