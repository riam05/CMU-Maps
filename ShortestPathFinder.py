import json
import heapq

def dijkstra(graph, start):
    queue = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()

    while queue:
        (dist, current_node) = heapq.heappop(queue)
        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances

# Load JSON data from file
with open('wean_hall.json', 'r') as f:
    graph_data = json.load(f)

# Create graph
graph = {node['id']: {} for node in graph_data['nodes']}
for edge in graph_data['edges']:
    graph[edge['source']][edge['target']] = edge['weight']
    graph[edge['target']][edge['source']] = edge['weight']  # Ensure bidirectional pathways

# Example: Find shortest distances from node 0
start_node = 0
distances = dijkstra(graph, start_node)
print("Shortest distances from node {start_node}: {distances}")
