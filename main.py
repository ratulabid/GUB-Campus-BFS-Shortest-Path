from collections import deque

graph = {
    "Main Gate": [
        "Security Checkpoint",
        "Transport & Parking Area"
    ],

    "Security Checkpoint": [
        "Main Gate",
        "Administrative Building",
        "Academic Building 1"
    ],

    "Administrative Building": [
        "Security Checkpoint",
        "Admission & Information Desk",
        "Central Library"
    ],

    "Admission & Information Desk": [
        "Administrative Building"
    ],

    "Central Library": [
        "Administrative Building",
        "Academic Building 1",
        "IT Center"
    ],

    "Academic Building 1": [
        "Security Checkpoint",
        "Central Library",
        "Academic Building 2",
        "Academic Building 3"
    ],

    "Academic Building 2": [
        "Academic Building 1",
        "Academic Building 4",
        "Programming Laboratory"
    ],

    "Academic Building 3": [
        "Academic Building 1",
        "Academic Building 5",
        "AI & Machine Learning Laboratory"
    ],

    "Academic Building 4": [
        "Academic Building 2",
        "Academic Building 6",
        "Networking Laboratory"
    ],

    "Academic Building 5": [
        "Academic Building 3",
        "Academic Building 7",
        "IT Center"
    ],

    "Academic Building 6": [
        "Academic Building 4",
        "Academic Building 8",
        "Multipurpose Hall"
    ],

    "Academic Building 7": [
        "Academic Building 5",
        "IT Center",
        "Green Cafeteria"
    ],

    "Academic Building 8": [
        "Academic Building 6",
        "Green Cafeteria",
        "Student Activity Area"
    ],

    "IT Center": [
        "Central Library",
        "Academic Building 5",
        "Academic Building 7",
        "Programming Laboratory"
    ],

    "Programming Laboratory": [
        "Academic Building 2",
        "IT Center",
        "AI & Machine Learning Laboratory"
    ],

    "AI & Machine Learning Laboratory": [
        "Academic Building 3",
        "Programming Laboratory",
        "Networking Laboratory"
    ],

    "Networking Laboratory": [
        "Academic Building 4",
        "AI & Machine Learning Laboratory",
        "Multipurpose Hall"
    ],

    "Multipurpose Hall": [
        "Academic Building 6",
        "Networking Laboratory",
        "Green Auditorium"
    ],

    "Green Auditorium": [
        "Multipurpose Hall",
        "Green Cafeteria",
        "Student Activity Area"
    ],

    "Green Cafeteria": [
        "Academic Building 7",
        "Academic Building 8",
        "Green Auditorium",
        "Medical Center"
    ],

    "Medical Center": [
        "Green Cafeteria",
        "Gymnasium",
        "Playground"
    ],

    "Gymnasium": [
        "Medical Center",
        "Student Activity Area",
        "Playground"
    ],

    "Student Activity Area": [
        "Academic Building 8",
        "Green Auditorium",
        "Gymnasium"
    ],

    "Playground": [
        "Medical Center",
        "Gymnasium",
        "Transport & Parking Area"
    ],

    "Transport & Parking Area": [
        "Main Gate",
        "Playground"
    ]
}


# Finds the shortest path using Breadth-First Search (BFS)
def bfs_shortest_path(graph, start, target):

    queue = deque([start])
    visited = {start}
    parent = {start: None}
    bfs_order = []

    while queue:
        current = queue.popleft()
        bfs_order.append(current)

        # Stop when target is found
        if current == target:
            break

        # Visit all unvisited neighbors
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    # Target is unreachable
    if target not in parent:
        return None

    # Reconstruct shortest path
    path = []
    current = target

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    return path, bfs_order


# Program heading
print("GUB Campus Navigation & Shortest Path Finder")
print("=" * 50)

# Display all available locations
print("\nAvailable Locations:")

for i, location in enumerate(graph.keys(), 1):
    print(f"{i}. {location}")


# Take start and target locations from the user
start_input = input("\nEnter Start Location: ").strip()
target_input = input("Enter Target Location: ").strip()


# Make location input case-insensitive
location_map = {location.lower(): location for location in graph}

start = location_map.get(start_input.lower())
target = location_map.get(target_input.lower())


# Check for invalid locations
if start is None or target is None:

    print("\nInvalid location!")

else:

    # Handle same start and target
    if start == target:

        print("\nStart and Target are the same location.")
        print("\nPath Array:")
        print([start])

        print("\nBFS Traversal Order:")
        print([start])

        print("\nTotal Edge Steps: 0")

    else:

        # Find shortest path using BFS
        result = bfs_shortest_path(graph, start, target)

        if result is None:

            print("\nNo path found.")

        else:

            path, bfs_order = result

            # Display BFS traversal
            print("\nBFS Traversal Order:")
            print(" -> ".join(bfs_order))

            # Display path as an array
            print("\nPath Array:")
            print(path)

            # Display shortest path
            print("\nShortest Path:")
            print(" -> ".join(path))

            # Number of edges in the shortest path
            print("\nTotal Edge Steps:", len(path) - 1)
