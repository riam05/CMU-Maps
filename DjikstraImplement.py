import heapq
import json

# Load JSON data
with open('wean_hall_expanded_1.json') as file:
    data = json.load(file)

# Build adjacency list
graph = {}
for node in data["nodes"]:
    graph[node["id"]] = {}  # Initialize adjacency list

for edge in data["edges"]:
    source, target, weight = edge["source"], edge["target"], edge["weight"]

    # Add bidirectional edges
    graph[source][target] = weight
    graph[target][source] = weight

# Dijkstra's Algorithm
def dijkstra(start_id, goal_id):
    queue = [(0, start_id)]  # (distance, node)
    distances = {node: float('inf') for node in graph}
    distances[start_id] = 0
    previous_nodes = {}

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_node == goal_id:
            path = []
            while current_node in previous_nodes:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            path.append(start_id)
            return path[::-1], distances[goal_id]

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return None, float('inf')  # No path found

# Example usage
start_id = "4301"
goal_id = "4701A"      

path, distance = dijkstra(start_id, goal_id)
if path:
    print(f"Shortest path from {start_id} to {goal_id}: {path} with total distance {distance}")
else:
    print(f"No path found from {start_id} to {goal_id}.")
