# Function to perform DFS iteratively using a stack
def dfs(graph, start_node):
    visited = set()
    stack = [start_node]
    traversal_order = []

    while stack:
        # Pop the last element added
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            traversal_order.append(node)

            # Add unvisited neighbors to the stack
            # Reversed to maintain left-to-right order
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal_order


# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Perform DFS starting from node 'A'
result = dfs(graph, 'A')
print(result)