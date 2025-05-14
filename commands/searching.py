def edge_exists(graph, graph_type, start_vertex, end_vertex):
    start_vertex -= 1
    end_vertex -= 1
    if graph_type == 'matrix':
        return graph[start_vertex][end_vertex] == 1
    else:
        return end_vertex in graph[start_vertex]


def get_neighbors_matrix(graph, node):
    neighbors = []
    for i, val in enumerate(graph[node]):
        if val == 1:
            neighbors.append(i)
    return neighbors
        
def get_neighbors_list(graph, node):
    return graph[node]

def bfs(graph, start, neighbors_func):
    visited = set()
    queue = [start]
    result = []
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            result.append(node + 1)
            neighbors = neighbors_func(graph, node)
            for neighbor in neighbors:
                queue.append(neighbor)
    print("inline:", ' '.join(map(str, result)))

def dfs(graph, start, neighbors_func):
    visited = set()
    stack = [start]
    result = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node + 1)
            neighbors = neighbors_func(graph, node)
            for neighbor in reversed(neighbors):
                stack.append(neighbor)
    print("inline:", ' '.join(map(str, result)))