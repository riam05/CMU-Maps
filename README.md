CMURoam - Wean Hall Navigation System

CMURoam is a pathfinding system designed to help students, faculty, and visitors navigate the complex hallways of Wean Hall at Carnegie Mellon University. Our prototype focuses on the 4th and 5th floors and finds the shortest path between locations using graph-based navigation.

Project Overview

CMURoam is a hallway navigation system that:
- Computes the shortest path between rooms, hallways, and intersections.
- Helps students efficiently navigate Wean Hall.
- Uses Dijkstra’s Algorithm to determine the best route.
- Supports future expansion to other buildings and real-time navigation.

Technology Stack

- 3D Scanning: Polycam
- Visualization: Three.js
- Pathfinding: Dijkstra’s Algorithm (Python)
- Frontend Development: HTML, JavaScript
- Data Storage: JSON (Graph Representation)

How It Works

Graph Representation

The hallways are structured as a graph, where:
- Nodes represent hallway intersections, doors, and important points.
- Edges represent hallways connecting nodes, weighted by distance.

Node Naming Convention

- Classrooms: Based on room number (e.g., 4201).
- Hallways: Based on floor and hallway number (e.g., H4_3 for hallway 400, node 3).
- Hallway Intersections: Labeled based on connected hallways (e.g., H0_H3).
- Building Connections: Named based on connected floors/buildings (e.g., WEH4_NSH4 for Wean Hall 4th floor to Newell-Simon 4th floor).

Pathfinding Algorithm

We use Dijkstra’s Algorithm to:
- Expand the shortest known path first (priority queue).
- Keep track of distances from the starting node.
- Maintain a previous_nodes dictionary to reconstruct the path.
- Stop once the destination is reached.

Route Visualization

- Nodes are placed into a 3D environment using Three.js.
- Path highlighting shows the best route between rooms.

How to Run the Project

1. Clone the repository:
   git clone https://github.com/riam05/CMU-Maps

2. Run the pathfinding algorithm:
   python DjikstraImplement.py

Enter the start and end locations to get the shortest path.

Challenges We Faced

1. Node Collection/Creation
- Currently manual: Inputting nodes and edges into .json is tedious.
- Future solution: AI-based nodal mapping from CMU floor plans.

2. Live View Navigation
- Current implementation lacks real-time user tracking.
- Augmented Reality (AR) integration could be a future step.

3. Excessive Node Count
- Some hallways have too many nodes, making the graph inefficient.
- Need optimization strategies for better maintainability.

Future Plans

- Route Constraints: Avoid congested hallways, pass by a coffee shop, target elevators/stairs.
- Expand to More Floors & Buildings: Include staircases, elevators, and skybridges.
- Real-Time Live Navigation: Mobile app with Augmented Reality (AR) directions.
- AI-based system to automatically map nodal paths from floor plans.

Acknowledgments

Special thanks to:
- TartanHacks & Sponsors for making this possible.
- Poly.cam & FlutterFlow for enabling 3D scanning and visualization.

Contributors:
- Ayaan Shaikh
- Ria Mehta
- Shravani Vedagiri
- Shreya Kalavur

CMURoam - Making Navigation Easier for Everyone!
