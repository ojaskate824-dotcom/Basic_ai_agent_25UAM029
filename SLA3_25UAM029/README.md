# SLA3 - Full C4 Architecture Design

## Project Title
BFS vs DFS Graph Search and Performance Profiling System

## Student Details
- Name: Ojas Yashwant Kate
- PRN: 25UAM029
- Class: SY B.Tech CSE (AI & ML)
- Subject: Introduction to Artificial Intelligence

## 1. System Description

This system performs BFS and DFS graph search on a small 15-node graph.
It takes a graph, start node, target node, and search algorithm as inputs.
The system performs the selected search and tracks the number of nodes expanded.
It also measures the best, average, and worst execution time of BFS and DFS.
The architecture is represented using all four levels of the C4 model.

## 2. C4 Architecture

### C1 - Context
Shows the interaction between the user and the BFS/DFS Graph Search
and Performance Profiling System.

Diagram:
`diagrams/c1_context_diagram.png`

### C2 - Container
Shows the major logical containers of the system:

1. Graph & Input Setup
2. BFS Search
3. DFS Search
4. Search State Management
5. Performance Profiling & Output

Diagram:
`diagrams/c2_container_diagram.png`

### C3 - Component
Shows the internal components of the main BFS/DFS Search Engine:

1. BFS Algorithm
2. DFS Algorithm
3. Queue Management
4. Stack Management
5. Visited Node Tracking & Node Expansion
6. Target Node Check

Diagram:
`diagrams/c3_component_diagram.png`

### C4 - Code
Shows the main functions used in the implementation:

- `get_small_graph()` - Creates the 15-node graph.
- `bfs()` - Performs Breadth-First Search.
- `dfs()` - Performs Depth-First Search.
- `profile_algorithm()` - Measures search performance.

Diagram:
`diagrams/c4_code_diagram.png`

## 3. Design Decisions

- BFS and DFS are kept as separate search algorithms for direct comparison.
- A small 15-node graph is used so that the search process is easy to understand.
- A visited set is used to track explored nodes.
- Performance profiling is separated from the search logic.
- The C4 architecture is based on the actual functions used in the implementation.

## 4. Relation with SLE-2

SLE-2 experimentally profiled BFS and DFS using the same 15-node graph.
The SLE-3 architecture describes the structure of the system used for
that performance analysis.

## 5. Conclusion

The full C4 model provides four levels of architectural understanding:
Context, Container, Component, and Code. It shows how the user interacts
with the system, how the system is divided into logical containers,
how the search engine is internally organized, and which main functions
implement the system.