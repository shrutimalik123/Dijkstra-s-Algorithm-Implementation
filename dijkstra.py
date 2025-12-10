import heapq

def dijkstra(graph, start, end):
    """
    Finds the shortest path between start and end nodes in a graph.

    Args:
        graph: A dictionary representing the graph where keys are node names
               and values are dictionaries of {neighbor: weight}.
        start: The starting node name.
        end: The target node name.

    Returns:
        A tuple (distance, path).
        distance: The total weight of the shortest path. infinity if no path.
        path: A list of nodes representing the path. Empty list if no path.
    """
    
    # Priority queue to store (current_distance, current_node)
    # Ordered by current_distance (min-heap)
    pq = [(0, start)]
    
    # Dictionary to keep track of the shortest distance found so far to each node
    # Initialize with infinity for all nodes except start
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Dictionary to reconstruct the path: predecessors[node] = previous_node_in_path
    predecessors = {node: None for node in graph}
    
    visited = set()

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # If we reached the destination, we can reconstruct the path and return
        if current_node == end:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = predecessors[current_node]
            return current_distance, path[::-1] # Return reversed path

        if current_node in visited:
            continue
        visited.add(current_node)

        # Explore neighbors
        if current_node in graph:
            for neighbor, weight in graph[current_node].items():
                if neighbor in visited:
                    continue
                
                new_distance = current_distance + weight
                
                # If a shorter path to neighbor is found
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(pq, (new_distance, neighbor))
    
    return float('inf'), []

if __name__ == "__main__":
    # Sample Graph: Cities and Distances
    # A --1--> B --4--> C
    # |        |        ^
    # 2        1        | 3
    # v        v        |
    # D --5--> E --1-----
    
    city_graph = {
        'A': {'B': 1, 'D': 2},
        'B': {'C': 4, 'E': 1},
        'C': {}, # Destination, no outgoing edges in this specific path example check
        'D': {'E': 5},
        'E': {'C': 3}
    }
    
    # Adding a few more connections to make it bidirectional or more complex if needed.
    # For this example, let's treat it as directed as implied by logic, but works for undirected too if edges mirrored.
    # Let's verify with a slightly more common undirected "Map" example style.
    
    cities = {
        'New York': {'Boston': 215, 'Philadelphia': 95},
        'Boston': {'New York': 215, 'Montreal': 310},
        'Philadelphia': {'New York': 95, 'Washington DC': 140, 'Pittsburgh': 305},
        'Washington DC': {'Philadelphia': 140, 'Charlotte': 400},
        'Pittsburgh': {'Philadelphia': 305, 'Columbus': 185},
        'Montreal': {'Boston': 310},
        'Charlotte': {'Washington DC': 400},
        'Columbus': {'Pittsburgh': 185}
    }

    start_city = 'New York'
    end_city = 'Columbus'
    
    print(f"Finding shortest path from {start_city} to {end_city}...")
    dist, path = dijkstra(cities, start_city, end_city)
    
    if dist != float('inf'):
        print(f"Shortest Distance: {dist}")
        print(f"Path: {' -> '.join(path)}")
    else:
        print(f"No path found between {start_city} and {end_city}")

    # Another test case
    print("-" * 20)
    start_city = 'Boston'
    end_city = 'Washington DC'
    print(f"Finding shortest path from {start_city} to {end_city}...")
    dist, path = dijkstra(cities, start_city, end_city)

    if dist != float('inf'):
        print(f"Shortest Distance: {dist}")
        print(f"Path: {' -> '.join(path)}")
    else:
        print(f"No path found between {start_city} and {end_city}")
