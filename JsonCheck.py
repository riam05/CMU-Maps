import json

# Load JSON from an external file
json_file_path = "wean_hall_expanded_1.json"  # Replace with your file name or path
try:
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)
        print("JSON data loaded successfully!")
except FileNotFoundError:
    print(f"Error: File '{json_file_path}' not found.")
    exit(1)
except json.JSONDecodeError as e:
    print(f"Error: Failed to decode JSON. Check the file format.\n{e}")
    exit(1)

# Check for duplicate paths with different weights
edge_weights = {}
duplicate_paths = []
for edge in json_data["edges"]:
    path = tuple(sorted([edge["source"], edge["target"]]))  # Sort to handle bidirectional edges
    weight = edge["weight"]
    if path in edge_weights and edge_weights[path] != weight:
        duplicate_paths.append((path, edge_weights[path], weight))
    else:
        edge_weights[path] = weight

# Check for disconnected nodes
connected_nodes = set()
for edge in json_data["edges"]:
    connected_nodes.add(edge["source"])
    connected_nodes.add(edge["target"])

disconnected_nodes = [node["id"] for node in json_data["nodes"] if node["id"] not in connected_nodes]

# Output results
print("Duplicate Paths with Different Weights:")
if duplicate_paths:
    for path, weight1, weight2 in duplicate_paths:
        print(f"Path: {path}, Weights: {weight1} and {weight2}")
else:
    print("No duplicate paths with different weights found.")

print("\nDisconnected Nodes:")
if disconnected_nodes:
    for node in disconnected_nodes:
        print(f"Node: {node}")
else:
    print("No disconnected nodes found.")
