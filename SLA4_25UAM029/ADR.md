# SLE-4: Architecture Decision Record (ADR)

## Project Title
**BFS vs DFS Graph Search and Performance Profiling System**

## 1. Context
This project compares Breadth-First Search (BFS) and Depth-First Search (DFS) on a graph containing 15 nodes. The starting node is A, and the target node is O.

The system measures the number of expanded nodes and the best, average, and worst execution times. SLE-2 focused on performance profiling, while SLE-3 represented the system using C4 architecture diagrams.

## 2. Decision
The selected decision is to keep `bfs()` and `dfs()` as separate search functions and use a separate `profile_algorithm()` function for performance measurement.

Both algorithms use the same graph, starting node, and target node to ensure a fair comparison.

## 3. Alternatives Considered

### Option 1: Separate Search Functions — Selected
Keep `bfs()` and `dfs()` separate and use `profile_algorithm()` for performance measurement.

### Option 2: One Combined Function
Implement both algorithms in a single function using conditional statements.

### Option 3: Use Only One Algorithm
Implement and evaluate only BFS or DFS.

## 4. Rationale and Justification

The first option was selected because it improves readability, testing, debugging, and maintainability.

The SLE-2 experimental results were:

| Measurement | BFS | DFS |
|---|---:|---:|
| Best time | 0.002227 ms | 0.000673 ms |
| Average time | 0.002332 ms | 0.000742 ms |
| Worst time | 0.002719 ms | 0.000961 ms |
| Nodes expanded | 15 | 4 |

DFS showed lower execution times and fewer expanded nodes on the selected graph. However, the performance of both algorithms depends on graph structure and target position.

The separate profiling function keeps performance measurement independent of the search logic and supports the C4 architecture diagrams created in SLE-3.

## 5. Consequences and Trade-offs

### Benefits
- Improves code readability and maintainability.
- Allows BFS and DFS to be tested independently.
- Separates search logic from performance measurement.
- Makes the implementation easier to explain during the viva.

### Limitations
- Some logic, such as visited-node handling, may be repeated.
- Execution times may vary between runs and computers.
- A 15-node graph is not sufficient to generalise performance to all graphs.
- BFS finds a shortest path in an unweighted graph when implemented correctly, whereas DFS does not guarantee the shortest path.

## 6. References
1. SLE-2 BFS vs DFS Performance Profiling Report.
2. SLE-3 C4 Architecture Diagrams and Python Implementation.
3. Python Documentation — `time.perf_counter()`.
4. Graphviz Documentation.

## Conclusion
This ADR documents the decision to separate BFS and DFS search functions from performance profiling. The decision supports a clear architecture, easier testing, and a fair comparison based on the SLE-2 results and SLE-3 architecture diagrams.
