# SLA-2: Empirical Performance Profiling Report
**Author:** Ojas Kate  
**Roll No:** 25UAM029  
**Class:** SY BTECH CSE(AIML)  

## 1. Introduction
This empirical study evaluates the real-world hardware performance of Breadth-First Search (BFS) and Depth-First Search (DFS). While asymptotic Big-O bounds describe theoretical scalability, this report measures actual execution latency and physical RAM allocation bottlenecks when exploring an identical 250x250 node grid graph over 5 consecutive trials.

## 2. Empirical Results
The empirical metrics captured across 5 iterative execution test cycles are summarized below:

| Metric Criteria | Breadth-First Search (BFS) | Depth-First Search (DFS) |
| :--- | :--- | :--- |
| **Best Execution Time (ms)** | 19.1878 ms | 0.1041 ms |
| **Worst Execution Time (ms)** | 25.2236 ms | 0.2058 ms |
| **Average Execution Time (ms)** | 22.1120 ms | 0.1274 ms |
| **Peak Memory Footprint (KB)** | 2563.04 KB | 41.57 KB |

## 3. Beyond Big-O Hardware Analysis
* **Memory Constraints:** BFS allocated substantially higher peak RAM (2563.04 KB) compared to DFS (41.57 KB). This occurs because the BFS FIFO queue retains all open frontier nodes at the current depth level in memory simultaneously, causing heavy data bloat on dense structures.
* **CPU Cache Locality:** DFS uses a LIFO stack behavior that exhibits tighter data access patterns, leading to cleaner hardware caching and fewer cache misses.
* **Execution Variance:** The difference between the Best and Worst execution times is a result of underlying operating system background tasks handling scheduling, thread switching, and hardware cache updates during runtime.
