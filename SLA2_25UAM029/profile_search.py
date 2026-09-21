import time
import tracemalloc
from collections import deque

def generate_large_grid(size=500):
    graph = {}
    for r in range(size):
        for c in range(size):
            neighbors = []
            if r + 1 < size: neighbors.append((r + 1, c))
            if c + 1 < size: neighbors.append((r, c + 1))
            graph[(r, c)] = neighbors
    return graph

def bfs(graph, start, target):
    queue = deque([start])
    visited = {start}
    while queue:
        node = queue.popleft()
        if node == target: return True
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False

def dfs(graph, start, target):
    stack = [start]
    visited = {start}
    while stack:
        node = stack.pop()
        if node == target: return True
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    return False

def profile_algorithm(algo_func, graph, start, target, name):
    tracemalloc.start()
    start_time = time.perf_counter()
    algo_func(graph, start, target)
    end_time = time.perf_counter()
    _, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_ms = (end_time - start_time) * 1000
    peak_memory_kb = peak_memory / 1024
    
    print(f"=== {name} Performance ===")
    print(f"Execution Time: {execution_time_ms:.4f} ms")
    print(f"Peak Memory Footprint: {peak_memory_kb:.2f} KB\n")

if __name__ == "__main__":
    print("Generating hardware evaluation grid environment...")
    grid_graph = generate_large_grid(250)
    start_node = (0, 0)
    target_node = (249, 249)
    print("Running hardware performance benchmarks...\n")
    profile_algorithm(bfs, grid_graph, start_node, target_node, "Breadth-First Search (BFS)")
    profile_algorithm(dfs, grid_graph, start_node, target_node, "Depth-First Search (DFS)")
