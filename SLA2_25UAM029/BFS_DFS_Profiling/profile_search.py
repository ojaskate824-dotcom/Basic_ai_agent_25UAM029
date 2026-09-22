import time
from collections import deque


# Small 15-node graph
def get_small_graph():
    return {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': ['H', 'I'],
        'E': ['J', 'K'],
        'F': ['L', 'M'],
        'G': ['N', 'O'],
        'H': [], 'I': [], 'J': [], 'K': [],
        'L': [], 'M': [], 'N': [], 'O': []
    }


# Breadth-First Search
def bfs(graph, start, target):
    queue = deque([start])
    visited = set()
    nodes_expanded = 0

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            nodes_expanded += 1

            if node == target:
                return True, nodes_expanded

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return False, nodes_expanded


# Depth-First Search
def dfs(graph, start, target):
    stack = [start]
    visited = set()
    nodes_expanded = 0

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            nodes_expanded += 1

            if node == target:
                return True, nodes_expanded

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    stack.append(neighbor)

    return False, nodes_expanded


# Measure performance
def profile_algorithm(algo_func, graph, start, target, name,
                      measurements=5, runs_per_measurement=1000):

    times = []
    node_counts = []

    for _ in range(measurements):

        start_time = time.perf_counter()

        expanded = 0

        for _ in range(runs_per_measurement):
            _, nodes = algo_func(graph, start, target)
            expanded = nodes

        end_time = time.perf_counter()

        # Average time for one search
        total_time_ms = (end_time - start_time) * 1000
        average_run_time = total_time_ms / runs_per_measurement

        times.append(average_run_time)
        node_counts.append(expanded)

    best_time = min(times)
    average_time = sum(times) / len(times)
    worst_time = max(times)

    print(f"========== {name} ==========")
    print(f"Best Time       : {best_time:.6f} ms")
    print(f"Average Time    : {average_time:.6f} ms")
    print(f"Worst Time      : {worst_time:.6f} ms")
    print(f"Nodes Expanded  : {node_counts[0]}")
    print()


if __name__ == "__main__":

    graph = get_small_graph()

    print("BFS vs DFS Performance Comparison")
    print("Graph: Small 15-node graph")
    print("Start Node: A")
    print("Target Node: O")
    print()

    profile_algorithm(
        bfs,
        graph,
        'A',
        'O',
        "Breadth-First Search (BFS)"
    )

    profile_algorithm(
        dfs,
        graph,
        'A',
        'O',
        "Depth-First Search (DFS)"
    )