# SLA-2: Empirical Performance Profiling Report
**Author:** Ojas Kate  
**Roll No:** 25UAM029  
**Class:** SY BTECH CSE(AIML)  

## 1. Introduction
This empirical study evaluates the real-world hardware performance of Breadth-First Search (BFS) and Depth-First Search (DFS). While asymptotic Big-O bounds describe theoretical scalability, this report measures actual execution latency and physical RAM allocation bottlenecks when exploring an identical 250x250 node grid graph.

## 2. Empirical Results
The empirical metrics captured using Python's `time.perf_counter` and `tracemalloc` resource monitors are summarized below:

| Performance Metric | Breadth-First Search (BFS) | Depth-First Search (DFS) |
| :--- | :--- | :--- |
| **Execution Time (ms)** | 26.8595 ms | 0.2382 ms |
| **Peak Memory Usage (KB)** | 2563.07 KB | 41.61 KB |

## 3. Beyond Big-O Hardware Analysis
* **Memory Constraints:** BFS allocated substantially higher peak RAM than DFS. This occurs because the BFS FIFO queue retains all open frontier nodes at the current depth level in memory simultaneously, causing heavy data bloat on dense structures.
* **CPU Cache Locality:** DFS uses a LIFO stack behavior that exhibits tighter data access patterns, leading to cleaner hardware caching and fewer cache misses.
