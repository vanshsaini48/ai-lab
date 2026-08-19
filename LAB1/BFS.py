from collections import deque


# Function to perform BFS using a queue
def bfs(graph, start_node):
    visited = set([start_node])
    queue = deque([start_node])
    traversal_order = []

    while queue:
        # Dequeue the front node
        node = queue.popleft()
        traversal_order.append(node)

        # Enqueue unvisited neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order


# Graph represented as an adjacency list
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": [],
}

# Perform BFS starting from node 'A'
result = bfs(graph, "A")
print(result)