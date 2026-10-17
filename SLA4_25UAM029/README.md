# SLE-4: Architecture Decision Record (ADR)

## Project Title
**BFS vs DFS Graph Search and Performance Profiling System**

## 1. Overview
This project compares Breadth-First Search (BFS) and Depth-First Search (DFS) on a small graph containing 15 nodes. The starting node is A, and the target node is O.

The system counts expanded nodes and measures the best, average, and worst execution time of both algorithms.

## 2. Objective
The objective of SLE-4 is to document and justify an important software architecture decision based on the implementation and experimental results from SLE-2 and the architecture diagrams from SLE-3.

## 3. Architecture Decision
The selected decision is to keep `bfs()` and `dfs()` as separate search functions and use a separate `profile_algorithm()` function for performance measurement.

This approach separates search logic from performance profiling and makes the implementation easier to understand, test, and maintain.

## 4. Alternatives Considered
- **Option 1 — Selected:** Keep BFS and DFS separate and use a separate profiling function.
- **Option 2:** Combine both algorithms into one function using conditional branches.
- **Option 3:** Implement and profile only one search algorithm.

Option 1 was selected because it supports a clearer comparison between the two algorithms and keeps the code organised.

## 5. Experimental Results

| Measurement | BFS | DFS |
|---|---:|---:|
| Best execution time | 0.002227 ms | 0.000673 ms |
| Average execution time | 0.002332 ms | 0.000742 ms |
| Worst execution time | 0.002719 ms | 0.000961 ms |
| Nodes expanded | 15 | 4 |

These values are from the SLE-2 experiment. DFS showed lower execution times and expanded fewer nodes on the selected graph. These results do not mean that DFS is always faster than BFS.

## 6. Consequences and Trade-offs

### Benefits
- Improves code readability and maintainability.
- Makes BFS and DFS easier to test independently.
- Separates performance measurement from search logic.
- Supports clear documentation and architecture diagrams.

### Limitations
- Some logic may be repeated in both search functions.
- Small execution-time measurements can vary across runs and computers.
- A 15-node graph cannot represent every possible graph structure.
- DFS does not guarantee the shortest path, whereas BFS finds a shortest path in an unweighted graph when implemented correctly.

## 7. Relationship with Previous SLEs
- **SLE-1:** Explored and documented a basic AI agent workflow.
- **SLE-2:** Compared BFS and DFS using execution-time measurements and node-expansion counts.
- **SLE-3:** Represented the system using C1, C2, C3, and C4 architecture diagrams.
- **SLE-4:** Documented and justified the decision to separate the search functions from performance profiling.

## 8. Tools and Technologies
- Python
- Graphviz
- Python `time.perf_counter()` for execution-time measurement
- Git and GitHub for version control

## 9. Conclusion
This ADR documents the design decision, alternatives, justification, and trade-offs of the BFS vs DFS Graph Search and Performance Profiling System. It connects the experimental results from SLE-2 and the architecture design from SLE-3 to the final implementation decision.

## 10. References
1. SLE-2 Profiling Report: BFS vs DFS Graph Search and Performance Analysis.
2. SLE-3 C4 Architecture Diagrams and Python Implementation.
3. Graphviz Documentation.
4. Python Documentation.
