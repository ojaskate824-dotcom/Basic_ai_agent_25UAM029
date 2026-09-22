
# SLE-2: Profiling Report

## Course
02AML204 – Introduction to Artificial Intelligence

## Student Details
- **PRN:** 25UAM029
- **Name:** Ojas Yashwant Kate
- **Division:** A

## Project Overview
This project focuses on empirical performance analysis of two search algorithms: Breadth-First Search (BFS) and Depth-First Search (DFS).

The purpose of SLE-2 is to measure algorithm performance using execution time and the number of nodes expanded.

## Algorithms Compared

### 1. Breadth-First Search (BFS)
BFS explores a graph level by level using a queue. It visits neighboring nodes before moving to the next level.

### 2. Depth-First Search (DFS)
DFS explores one path as deeply as possible before backtracking. It uses a stack for traversal.

## Problem Used
- Graph Size: 15 nodes
- Start Node: A
- Target Node: O
- Algorithms: BFS and DFS

Both algorithms were tested using the same graph, start node, and target node.

## Profiling Method
- **Programming Language:** Python
- **Profiling Tool:** `time.perf_counter()`
- **Measurements:** 5
- **Performance Metrics:** Execution time and nodes expanded

## Results

| Metric | BFS | DFS |
|---|---:|---:|
| Best Time (ms) | 0.003177 | 0.001022 |
| Average Time (ms) | 0.003310 | 0.001055 |
| Worst Time (ms) | 0.003405 | 0.001171 |
| Nodes Expanded | 15 | 4 |

## Observation
For the selected graph, DFS recorded a lower average execution time and expanded fewer nodes than BFS.

The results depend on the graph structure and target node position.

## Justification
DFS reached the target node after expanding fewer nodes in this experiment. BFS expanded all 15 nodes because of its traversal order.

The measured results show that execution time and node expansion can vary between search algorithms. DFS is not always faster; performance depends on the input graph.

## AI Contribution Note
AI tools were used for guidance in understanding the profiling requirements, organizing the report, and explaining BFS and DFS performance.

The profiling experiment and result interpretation were performed as part of the project work.

## Conclusion
This project demonstrates the performance comparison of BFS and DFS using a small graph.

Profiling helps measure execution time and nodes expanded, providing numerical evidence for analyzing search algorithms.

## Repository Structure

```text
SLA2_25UAM029/
└── BFS_DFS_Profiling/
    ├── profile_search.py
    ├── REPORT.md
    └── AI_CONTRIBUTION_LOG.md
```

## GitHub Repository
<<<<<<< HEAD
https://github.com/ojaskate824-dotcom/Basic_ai_agent_25UAM029
=======
https://github.com/ojaskate824-dotcom/Basic_ai_agent_25UAM029
>>>>>>> 40b5d2a (Update BFS DFS profiling files)
