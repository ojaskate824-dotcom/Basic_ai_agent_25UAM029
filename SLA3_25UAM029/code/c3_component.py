# C3 - Component Diagram
# Components of the BFS/DFS Search Engine

from graphviz import Digraph

dot = Digraph("C3_Component")

# Components inside the main Search Engine
dot.node("BFS", "BFS Algorithm", shape="box")
dot.node("DFS", "DFS Algorithm", shape="box")
dot.node("Queue", "Queue Management\n(BFS)", shape="box")
dot.node("Stack", "Stack Management\n(DFS)", shape="box")
dot.node("Visited", "Visited Node Tracking\n& Node Expansion", shape="box")
dot.node("Target", "Target Node Check", shape="box")

# BFS flow
dot.edge("BFS", "Queue", label="Uses")
dot.edge("Queue", "Visited", label="Processes Nodes")

# DFS flow
dot.edge("DFS", "Stack", label="Uses")
dot.edge("Stack", "Visited", label="Processes Nodes")

# Common search operations
dot.edge("Visited", "Target", label="Checks")
dot.edge("Target", "BFS", label="Search Result")
dot.edge("Target", "DFS", label="Search Result")

# Generate diagram
dot.render(
    "../diagrams/c3_component_diagram",
    format="png",
    cleanup=True
)