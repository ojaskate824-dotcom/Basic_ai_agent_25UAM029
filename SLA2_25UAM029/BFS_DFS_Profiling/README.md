# SLE-2: Profiling Report

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**PRN:** 25UAM029  
**Name:** Ojas Yashwant Kate  
**Division:** A  
**Date:** 21/09/2026  
**GitHub Link:** https://github.com/ojaskate824-dotcom/Basic_ai_agent_25UAM029

---

## 1. Algorithms / Versions Profiled

### Algorithm A: Breadth-First Search (BFS)

BFS explores the graph level by level using a queue. It visits the neighboring nodes before moving to the next level.

### Algorithm B: Depth-First Search (DFS)

DFS explores one path as deeply as possible before backtracking. It uses a stack for traversal.

### Problem

A small 15-node graph was used for the experiment.

- **Start Node:** A
- **Target Node:** O
- **Graph Size:** 15 nodes
- **Algorithms Compared:** BFS and DFS

The same graph, start node, and target node were used for both algorithms to make the comparison fair.

---

## 2. Profiling Method

The performance of BFS and DFS was measured using Python's `time.perf_counter()` function.

Each algorithm was measured for **5 measurements**, and the average execution time was calculated.

The number of nodes expanded by each algorithm was also counted during the search.

The experiment was performed using the same input graph for both BFS and DFS.

---

## 3. Results

| Metric | BFS | DFS |
|---|---:|---:|
| Best Time (ms) | 0.003177 | 0.001022 |
| Average Time (ms) | 0.003310 | 0.001055 |
| Worst Time (ms) | 0.003405 | 0.001171 |
| Nodes Expanded | 15 | 4 |

### Observation

From the measured results, DFS required less execution time than BFS for this particular graph. DFS expanded only 4 nodes before reaching the target node O, whereas BFS expanded all 15 nodes.

The result depends on the structure of the graph and the position of the target node. Therefore, this experiment represents the performance of BFS and DFS on the selected graph and should not be considered a general result for all graphs.

---

## 4. Justification & Analysis

BFS searches the graph level by level. In this experiment, the target node O was located near the end of the BFS traversal order, so BFS expanded all 15 nodes before reaching it.

DFS followed a path toward the target and reached O after expanding only 4 nodes. Therefore, the measured execution time of DFS was lower than BFS for this particular input.

The node count also supports the timing result because DFS expanded fewer nodes.

However, DFS does not always reach the target with fewer node expansions. Its performance depends on the order and structure of the graph.

BFS is useful when level-order exploration and shortest paths in an unweighted graph are required, while DFS is useful when depth-based exploration is suitable.

---

## 5. AI Contribution Note

AI tools were used during the development of this SLE-2 work for guidance related to the profiling experiment, report structure, and explanation of BFS and DFS performance.

The student independently created and organized the project files, executed the Python program, performed the profiling experiment, collected the actual results, and interpreted the measured values.

The final performance values in this report were obtained by running the program locally.

---

## 6. Conclusion

The experiment compared BFS and DFS using a common 15-node graph.

For the selected graph, DFS expanded fewer nodes and had a lower measured average execution time than BFS.

The experiment demonstrates that actual performance can depend on the graph structure, target position, and traversal order.

Profiling provides numerical evidence for comparing the performance of different search algorithms.
