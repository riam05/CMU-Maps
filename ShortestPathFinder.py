import heapq
import json
import math

# Load JSON data
with open('wean_hall.json') as file:
    data = json.load(file)

nodes = {node['id']: (node['x'], node['y']) for node in data['nodes']}
edges = { (edge['source'], edge['target']): edge['weight'] for edge in data['edges']}

# Heuristic function: Euclidean distance
def heuristic(node1, node2):
    x1, y1 = nodes[node1]
    x2, y2 = nodes[node2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# A* Algorithm
def a_star(start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {node: float('inf') for node in nodes}
    g_score[start] = 0
    f_score = {node: float('inf') for node in nodes}
    f_score[start] = heuristic(start, goal)

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for (source, target), weight in edges.items():
            if source == current:
                tentative_g_score = g_score[current] + weight
                if tentative_g_score < g_score[target]:
                    came_from[target] = current
                    g_score[target] = tentative_g_score
                    f_score[target] = g_score[target] + heuristic(target, goal)
                    heapq.heappush(open_set, (f_score[target], target))

    return None

# Example usage
start_node = 4
goal_node = 7
path = a_star(start_node, goal_node)
print("Shortest path from node", start_node, "to node", goal_node, ":", path)
