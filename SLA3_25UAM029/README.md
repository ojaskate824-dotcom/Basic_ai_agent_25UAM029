# SLA3 - Full C4 Architecture Design

## Project Title

**BFS vs DFS Graph Search and Performance Profiling System**

## Student Details

* **Name:** Ojas Yashwant Kate
* **PRN:** 25UAM029
* **Class:** SY B.Tech CSE (AI & ML)
* **Subject:** Introduction to Artificial Intelligence

---

## 1. System Description

The **BFS vs DFS Graph Search and Performance Profiling System** performs Breadth-First Search (BFS) and Depth-First Search (DFS) on a small 15-node graph.

The system takes a graph, start node, target node, and search algorithm as inputs. It performs the selected search and tracks the number of nodes expanded.

The system also measures the **best, average, and worst execution time** of BFS and DFS for performance comparison.

The architecture of the system is represented using all four levels of the **C4 model: Context, Container, Component, and Code**.

---

## 2. C4 Architecture

### C1 - Context Diagram

The C1 Context Diagram shows the interaction between the **User** and the **BFS/DFS Graph Search and Performance Profiling System**.

The user provides the graph, start node, target node, and selects BFS or DFS. The system returns the search result, number of nodes expanded, and performance results.

**Diagram:**
`diagrams/c1_context_diagram.png`

---

### C2 - Container Diagram

The C2 Container Diagram shows the major logical parts of the system:

1. **Graph & Input Setup**
2. **BFS Search**
3. **DFS Search**
4. **Performance Profiling & Output**

The Graph & Input Setup provides the graph, start node, and target node to the BFS and DFS search containers. The search results are then passed to the Performance Profiling & Output container.

**Diagram:**
`diagrams/c2_container_diagram.png`

---

### C3 - Component Diagram

The C3 Component Diagram shows the internal components of the BFS/DFS Search Engine:

1. **BFS Algorithm**
2. **DFS Algorithm**
3. **Queue Management (BFS)**
4. **Stack Management (DFS)**
5. **Visited Node Tracking & Node Expansion**
6. **Target Node Check**

BFS uses a queue for breadth-first traversal, while DFS uses a stack for depth-first traversal. Both algorithms track visited nodes, count expanded nodes, and check the target node.

**Diagram:**
`diagrams/c3_component_diagram.png`

---

### C4 - Code Diagram

The C4 Code Diagram shows the main functions used in the actual implementation:

* **`get_small_graph()`** - Creates the 15-node graph.
* **`bfs()`** - Performs Breadth-First Search.
* **`dfs()`** - Performs Depth-First Search.
* **`profile_algorithm()`** - Measures the performance of the search algorithms.

The `profile_algorithm()` function receives BFS or DFS as the algorithm function and measures its execution time.

**Diagram:**
`diagrams/c4_code_diagram.png`

---

## 3. Design Decisions

* BFS and DFS are implemented as separate search functions for direct comparison.
* A small **15-node graph** is used to make the search process easy to understand and analyze.
* BFS uses a **queue (`deque`)** for traversal.
* DFS uses a **stack** for traversal.
* A **visited set** is used to avoid processing the same node repeatedly.
* The number of **nodes expanded** is tracked during the search.
* Performance profiling is separated from the search algorithms using `profile_algorithm()`.
* The C4 architecture is based on the **actual functions and logic used in the implementation**.

---

## 4. Relation with SLA2

The SLA2 project experimentally compared **BFS and DFS performance** using the same 15-node graph.

The SLA3 architecture represents the structure of the system used for that performance analysis.

The C4 model provides a structured view of the same implementation at four levels:

* **C1:** System and user interaction
* **C2:** Major system containers
* **C3:** Internal search components
* **C4:** Main implementation functions

---

## 5. Conclusion

The full C4 architecture provides four levels of understanding of the BFS/DFS Performance Profiling System.

The **C1 diagram** shows the system and its interaction with the user. The **C2 diagram** shows the major logical containers. The **C3 diagram** explains the internal components of the BFS/DFS search engine. The **C4 diagram** shows the main functions used in the actual implementation.

This architecture provides a clear connection between the system requirements, design, and the implementation developed during SLA2.

---

## 6. AI Contribution

AI assistance was used for architectural organization, documentation, and reviewing the C4 diagrams.

The final architecture was reviewed against the actual BFS/DFS implementation before inclusion in the project.

The diagrams were generated using **Graphviz** and verified for consistency with the implemented functions and relationships.
