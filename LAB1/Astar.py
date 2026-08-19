import heapq


# Function to perform A* Search
def a_star_search(graph, heuristics, start, goal):
    # Priority queue stores tuples of: (f_score, current_node, path, g_score)
    open_set = [(heuristics[start], start, [start], 0)]
    visited = {}

    while open_set:
        f_score, current, path, g_score = heapq.heappop(open_set)

        # Goal reached
        if current == goal:
            return path, g_score

        # Skip if a cheaper path to current node was already processed
        if current in visited and visited[current] <= g_score:
            continue
        visited[current] = g_score

        # Explore neighbors
        for neighbor, weight in graph.get(current, []):
            tentative_g = g_score + weight
            h_score = heuristics.get(neighbor, 0)
            total_f = tentative_g + h_score

            # Add neighbor to priority queue
            heapq.heappush(
                open_set, (total_f, neighbor, path + [neighbor], tentative_g)
            )

    return None, float("inf")


# Weighted graph represented as an adjacency list: node -> [(neighbor, weight)]
graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("C", 2), ("D", 5)],
    "C": [("D", 1)],
    "D": [],
}

# Heuristic estimated distance to goal 'D'
heuristics = {"A": 5, "B": 3, "C": 1, "D": 0}

# Run A* Search from 'A' to 'D'
path, cost = a_star_search(graph, heuristics, "A", "D")
print(f"Path: {path}, Cost: {cost}")