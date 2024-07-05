# Pseudocode:
# 1. Initialize unvisited nodes list with all nodes.
# 2. Initialize distances dictionary with 0 for the start node and infinity for others.
# 3. Initialize paths dictionary with empty lists for all nodes.
# 4. Set the path for the start node to itself.
# 5. While there are unvisited nodes:
#    a. Select the unvisited node with the smallest distance.
#    b. For each neighbor of the current node:
#       i. If the total distance to the neighbor through the current node is less than the known distance:
#          - Update the shortest distance to the neighbor.
#          - Update the path to the neighbor.
#    c. Remove the current node from the unvisited list.
# 6. Print the shortest distance and path for the target node if specified, or for all nodes.
# 7. Return the distances and paths dictionaries.

def shortest_path(graph, start, target=''):
    """
    Calculate the shortest paths from the start node to all other nodes using Dijkstra's algorithm.
    
    Parameters:
    graph (dict): A dictionary representing the graph where keys are nodes and values are lists of tuples (neighbor, distance).
    start (str): The starting node.
    target (str, optional): The target node for which to print the shortest path. If not specified, prints paths to all nodes.
    
    Returns:
    tuple: A tuple containing two dictionaries:
           - distances: Shortest distances from the start node to each node.
           - paths: Shortest paths from the start node to each node as lists of nodes.
    """
    
    unvisited = list(graph)  # List of unvisited nodes
    distances = {node: 0 if node == start else float('inf') for node in graph}  # Initialize distances
    paths = {node: [] for node in graph}  # Initialize paths
    paths[start].append(start)  # Start path with the start node
    
    while unvisited:
        current = min(unvisited, key=distances.get)  # Select the unvisited node with the smallest distance
        for node, distance in graph[current]:  # Iterate over neighbors of the current node
            if distance + distances[current] < distances[node]:  # Check if a shorter path is found
                distances[node] = distance + distances[current]  # Update shortest distance
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]  # Copy the current path to the neighbor
                else:
                    paths[node].extend(paths[current])  # Extend the current path to the neighbor
                paths[node].append(node)  # Add the neighbor to the path
        unvisited.remove(current)  # Remove the current node from unvisited list
    
    targets_to_print = [target] if target else graph  # Determine nodes to print
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    return distances, paths

# Define the graph as an adjacency list
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

# Call the function and print the shortest path from 'A' to 'F'
shortest_path(my_graph, 'A')
