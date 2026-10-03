# C2 - Container Diagram
# BFS vs DFS Graph Search and Performance Profiling System

from graphviz import Digraph

dot = Digraph("C2_Container")

# Containers
dot.node("Input", "Graph & Input Setup", shape="box")
dot.node("BFS", "BFS Search", shape="box")
dot.node("DFS", "DFS Search", shape="box")
dot.node("State", "Search State Management", shape="box")
dot.node("Profile", "Performance Profiling\n& Output", shape="box")

# Flow
dot.edge("Input", "BFS", label="Graph, Start, Target")
dot.edge("Input", "DFS", label="Graph, Start, Target")

dot.edge("BFS", "State", label="Visited\nNodes Expanded")
dot.edge("DFS", "State", label="Visited\nNodes Expanded")

dot.edge("State", "Profile", label="Search Data")

# Output
dot.edge(
    "Profile",
    "Input",
    label="Search Result\nBest / Average / Worst Time"
)

# Generate diagram
dot.render(
    "../diagrams/c2_container_diagram",
    format="png",
    cleanup=True
)